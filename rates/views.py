from django.shortcuts import render
from rest_framework import viewsets

from .models import Rate
from .serializers import RateSerializer
#from  .utilis import rates_list

# Create your views here.
class RateViewSet(viewsets.ReadOnlyModelViewSet):
    '''Get all rates from beginning of time and order by created date'''

    queryset = Rate.objects.order_by('-created_date')
    serializer_class = RateSerializer




