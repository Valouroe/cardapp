from django.db import models
from django.core.exceptions import ObjectDoesNotExist

def get_default_card():
    try:
        return Card.objects.get(id=250)
    except ObjectDoesNotExist:
        # If the Card with id 250 doesn't exist, you could either return None or create a new one
        # For example, let's create a new Card instance if the specific id doesn't exist:
        return Card.objects.create(name='default_card')

class Card(models.Model):
    name = models.CharField(max_length=100, unique=True, default='hb')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Ema(models.Model):
    addr = models.EmailField(max_length=50, unique=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="emails", default=get_default_card)

    def __str__(self):
        return self.addr

class Member(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    ema = models.OneToOneField(Ema, blank=True, null=True, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="members", default=get_default_card)

    def __str__(self):
        return f"{self.name} ({self.card.name})"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name} on {self.submitted_at.strftime('%Y-%m-%d')}"
# class Ema(models.Model):
#     addr=models.EmailField(max_length=50, default="vokeyewurum@gmail.com")
#     def __str__(self):
#         return self.addr


# class Member(models.Model):
#     name=models.CharField(max_length=50)
#     message=models.CharField(max_length=200)
#     k=models.ForeignKey(Ema, blank=True, null=True, on_delete=models.CASCADE)
#     # email=models.EmailField(default="vokeyewurum@gmail.com")
#     def __str__(self):
#         return self.name


# class Addr(models.Model):
#     email=models.EmailField(max_length=50)
#     def __str__(self):
#         return self.email



# Create your models here.
