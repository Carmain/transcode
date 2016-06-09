from django.conf import settings
from django.core.mail import send_mail

def get_price(duration):
  price = settings.CONVERT_PRICE_PER_MINUTE * duration
  return max(price, 0.01)

def send_completion_mail(user, transcode_file):
  textual_mail_body = "You can view your transcoded files on the homepage when you are connected."
  html_mail_body = """
    <html>
      <body>
        <h1>Your file is ready!</h1>
        <p>
          Download your transcoded file <a href='http://{}/'>here</a>! (Don't forget to log in)
        </p>
      </body>
    </html>
  """.format(settings.BASE_DOMAIN)

  send_mail(
    "Your file has been successfully transcoded.",
    textual_mail_body,
    "Transcode <transcode@gmail.com>",
    [user.email],
    fail_silently=True,
    html_mail=html_mail_body
  )
