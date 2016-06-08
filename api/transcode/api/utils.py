from django.conf import settings
from django.core.mail import send_mail

def get_price(duration):
  price = settings.CONVERT_PRICE_PER_MINUTE * duration
  return max(price, 0.01)

def send_completion_mail(user, transcode_file):
  send_mail(
    "Your file has been successfully transcoded.",
    transcode_file.uuid,
    "Transcode <transcode@gmail.com>",
    [user.email],
    fail_silently=True
  )
