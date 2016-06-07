from django.conf import settings

def get_price(duration):
  return settings.CONVERT_PRICE_PER_MINUTE * duration
