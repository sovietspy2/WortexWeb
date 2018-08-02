import smtplib
import WortexLogger as logger
def send_activation_code(email, code):

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("", "")

  msg = 'Welcome! Please activate your account in 7 days to finnish your registration! http://wortex.stream/activate?' + code
  server.sendmail("info@wortex.stream", email, msg)
  server.quit()


