from django.db import models
from django.utils import timezone

# Create your models here.
class Rate(models.Model):
    black_market = models.CharField(max_length=250,blank=True)
    black_market_buy = models.CharField(max_length=250,blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.black_market