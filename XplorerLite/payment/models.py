from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    bank_name = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='payment_images/')
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email