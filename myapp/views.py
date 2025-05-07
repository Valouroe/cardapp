from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.core.serializers import serialize
from .models import Member, Ema, Card, Feedback
from .forms import MemberForm, AddrForm, CardForm
import json


def home(request):
    card_name = request.session.get('card_name')
    if not card_name:
        return redirect('select_card')  # no card selected yet

    card = get_object_or_404(Card, name=card_name)
    messl = Member.objects.filter(card=card).values('name', 'message')

    email = request.session.get('email')
    if email:
        ema = Ema.objects.filter(addr=email, card=card).first()
        if ema:
            member = Member.objects.filter(ema=ema).first()
        else:
            member = None
    else:
        member = None

    return render(request, 'index.html', {
        'messl': list(messl),
        'member': member
    })

def sign_up(request):
    if request.method == "POST":
        card_name = request.POST.get('card_name')
        email = request.POST.get('email')

        if Card.objects.filter(name=card_name).exists():
            messages.error(request, "Card already exists! Try signing in.")
            return redirect('sign_up')

        card = Card.objects.create(name=card_name)
        ema = Ema.objects.create(addr=email, card=card)
        Member.objects.create(name="", message="", ema=ema, card=card)

        request.session['card_name'] = card_name
        request.session['email'] = email

        return redirect('home')

    return render(request, 'sign_up.html')

def sign_in(request):
    if request.method == "POST":
        card_name = request.POST.get('card_name')
        email = request.POST.get('email')

        card = Card.objects.filter(name=card_name).first()
        if not card:
            messages.error(request, "Card does not exist! Try signing up.")
            return redirect('sign_in')

        ema = Ema.objects.filter(addr=email, card=card).first()
        if not ema:
            ema = Ema.objects.create(addr=email, card=card)
            Member.objects.create(name="", message="", ema=ema, card=card)

        request.session['card_name'] = card_name
        request.session['email'] = email

        return redirect('home')

    return render(request, 'sign_in.html')

def update_message(request):
    email = request.session.get('email')
    card_name = request.session.get('card_name')

    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')

        card = Card.objects.filter(name=card_name).first()
        ema = Ema.objects.filter(addr=email, card=card).first()
        member = Member.objects.filter(ema=ema).first()

        if member:
            member.name = name
            member.message = message
            member.save()
            messages.success(request, "Message updated successfully!")

    return redirect('home')

def select_card(request):
    return render(request, 'select_card.html')

def logout_view(request):
    logout(request)
    return redirect('select_card') 

def instructions(request):
    return render(request,'instructions.html')

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        if name and message:
            Feedback.objects.create(name=name, message=message)
            messages.success(request, 'Thank you for your feedback!')
            return redirect('select_card')  # or wherever you want to redirect after
        else:
            messages.error(request, 'Both fields are required.')

    return redirect('select_card')
# def si(request):
#     return render(request, "join.html", {})

# def join(request):
#     csrf="{{csrf_token}}"
#     print("k")
#     print(request.POST)
#     if request.method=="POST":
#         print("POST:", request.POST)
#         form = MemberForm(request.POST or None)
#         if form.is_valid():
#             print("j")
#             form.save()
#         else:
#              print("ERRORS!")
#              print(form.errors)
#         return render(request, "index.html", {})

# def home(request):
#     # allm=Member.objects.all
#     # print(request.GET)
#     messl = Member.objects.all().values("message", "name")  # Convert to list of dicts
#     messl_list = list(messl)  # Ensure it's a JSON serializable list
#     # messl=Member.objects.all()
#     return render(request, "index.html", {'messl': messl_list})

# def show(request):
#     messl=Member.objects.all()
#     return render(request, "show.html", {'messl':messl})

# def sign(request):
#     csrf="{{csrf_token}}"
#     print("k")
#     print(request.POST)
#     if request.method=="POST":
#         print("POST:", request.POST)
#         form = AddrForm(request.POST or None)
#         if form.is_valid():
#             print("j")
#             form.save()
            
#         else:
#              print("ERRORS!")
#              print(form.errors)
#     return redirect("home")   


# def make(request):
#      return HttpResponse("Let's Go!")
#      messages.success(request, ("Successful"))
#      return redirect("admin")
#      name=request.POST['name']
#      messages.success(request, ("Error"))
#      return render(request, index.html, {'name':name})
#      value="{{ name }}"


# Create your views here.
