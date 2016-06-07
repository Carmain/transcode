from django.conf import settings

def get_price(duration):
  return CONVERT_PRICE_PER_MINUTE * duration
