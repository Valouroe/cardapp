from django import forms
# from .models import Addr
from .models import Member,Ema,Card

class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=['name', 'message']


class AddrForm(forms.ModelForm):
    class Meta:
        model=Ema
        fields=['addr']

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name']
