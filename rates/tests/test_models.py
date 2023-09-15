import pytz
import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from freezegun import freeze_time

from rates.models import Rate

@freeze_time("2023-09-14 12:00:00")
class RateTests(TestCase):
    def setUp(self):
        Rate.objects.create(black_market='1234',
                            black_market_buy='5678',
                            created_date=timezone.now()
                            )

    def test_black_market(self):
        rate = Rate.objects.get(id=1)
        self.assertEqual(rate.black_market,"1234")

    def test_black_market_buy(self):
        rate = Rate.objects.get(id=1)
        self.assertEqual(rate.black_market_buy,"5678")

    def test_created_date(self):
        rate = Rate.objects.get(id=1)
        self.assertEqual(rate.created_date,timezone.now())
