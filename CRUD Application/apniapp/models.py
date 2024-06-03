from django.db import models

# Create your models here.
class Customer(models.Model):
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_DIAMOND = 'D'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_SILVER, 'SILVER'),
        (MEMBERSHIP_GOLD, 'GOLD'),
        (MEMBERSHIP_DIAMOND, 'DIAMOND'),
    ]
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=255)
    Email = models.EmailField(max_length=250)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_SILVER)
    points = models.IntegerField(default=50)
    password = models.CharField(max_length=128) 
    
    def __str__(self) -> str:
        return f'{self.First_name} {self.Last_name}'

    class Meta:
        ordering = ['First_name', 'Last_name']