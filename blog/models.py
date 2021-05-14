from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime, date

'''
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True) 
   

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
'''
class Order(models.Model):
    ORDER_CHOICES = [
        ('A1', 'Уход за ногтями'),
        ('A2', 'Легкий маникюр'),
        ('A3', 'Педикюр'),
        ('A4', 'Наращивание'),
        ('A5', 'Уходы'),
        ('A6', 'Педикюр + '),
        ('A7', 'Маникюр + гель лак'),
    ]
    MASTER_CHOICES = [
        ('B1', 'Алина Биккинина'),
        ('B2', 'Марина Касаткина'),
        ('B3', 'Екатерина Колесникова'),
        ('B4', 'Альфина Юнусова'),
        ('B5', 'Аделина Илькаева'),
        ('B6', 'Ильвира Зорина'),
        ('B7', 'Анна Баникова'),
        ('B8', 'Валерия Хайруллина'),
    ]
    name = models.CharField("Имя",max_length=100)
    email = models.EmailField("почта", max_length=100)
    phone = models.CharField(max_length=20)
    master  = models.CharField(max_length=2, choices=MASTER_CHOICES)
    good = models.CharField(max_length=2, choices=ORDER_CHOICES)
    purchase_date = models.DateField("Дата Date(mm/dd/2021)", auto_now_add=False, auto_now=False, blank=True, null=True)

    message = models.TextField()

    def __str__(self):
        return self.title
