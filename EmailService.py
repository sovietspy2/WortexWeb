import smtplib
import WortexLogger as logger
from email.message import EmailMessage
def send_activation_code(email, code):

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("send.mail.www.http", "")

  msg = EmailMessage()
  msg['Subject'] = 'Registrion to wortex.stream'
  msg['From'] = 'info@wortex.stream'
  msg['To'] = email

  msg.set_content('Welcome! Please activate your account in 7 days to finnish your registration! http://wortex.stream/activate?code=' + code)
  server.send_message(msg)
  logger.logging.info(msg)
  server.quit()


