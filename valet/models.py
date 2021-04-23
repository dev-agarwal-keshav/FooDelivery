from django.db import models
from django.contrib.auth.models import User
# Create your models here.
WORK=(
    ('10AM-10PM','10AM-10PM'),
    ('10PM-10AM','10PM-10AM')
)

class Valet(models.Model):
    user=models.ForeignKey(User, related_name='valet', on_delete=models.CASCADE)

    phone=models.IntegerField()
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zipcode=models.IntegerField()

    work_hr=models.CharField(max_length=100, choices=WORK, default="10AM-10PM")

    id_proof=models.TextField()
    dp=models.TextField()

    free=models.BooleanField(default=True)