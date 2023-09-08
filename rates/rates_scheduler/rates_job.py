from  rates.utilis import rates_list
from rates.models import Rate


def save_todays_rate():
    rates_obj = rates_list()
    if rates_obj is not None:
        try:
            rated = Rate.objects.create(black_market=rates_obj['Black Market Sell Rate'], 
                                        black_market_buy=rates_obj['Black Market Buy Rate'])
            print(rated.black_market)
            print(rated.black_market_buy)
            rated.save()
        except:
            pass