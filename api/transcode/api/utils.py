from django.conf import settings
from django.core.mail import send_mail

def get_price(duration):
  return settings.CONVERT_PRICE_PER_MINUTE * duration

def send_completion_mail(user, transcode_file):
  send_mail(
    "Your file has been successfully transcoded.",
    transcode_file.uuid,
    "Transcode <transcode@gmail.com>",
    [user.email],
    fail_silently=True
  )
