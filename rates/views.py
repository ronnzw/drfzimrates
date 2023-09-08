import requests
import schedule
import time

from bs4 import BeautifulSoup
from django.shortcuts import render
from rest_framework import viewsets

from .models import Rate
from .serializers import RateSerializer
#from  .utilis import rates_list

# Create your views here.
class RateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rate.objects.order_by('-created_date')
    serializer_class = RateSerializer




