import smtplib
import WortexLogger as logger

def send_emails(send,title,msg):
    server = smtplib.SMTP_SSL('smtp.yandex.com.tr:465')
    server.ehlo()
    server.login("sovietspy2@yandex.com","")
    message = 'Subject: {}\n\n{}'.format(title,msg)
    server.sendmail("sovietspy2@yandex.com",send,message)
    server.quit()
    logger.logging.info("Email was sent to: "+send)

def send_activation_code(email, code):
    send_emails(email,'wortex.stream account activation ', 'Welcome! Please activate your account in 7 days to finnish your registration! http://wortex.stream/activate?'+code+'''
    
    Render Aid
Jedi were obliged to help those in need of aid whenever possible, and were expected to be able to prioritize quickly. Jedi were taught that while saving one life was important, saving many lives was even more so. This principle did not mean a Jedi had to abandon other goals in every circumstance, but merely that a Jedi must do his or her best to make sure that they aided those who were most in need of assistance.[4]

Defend The Weak
Similarly, a Jedi was expected to defend the weak from those who oppressed them, ranging from small-scale suffering at the hands of an individual to large-scale enslavement of entire species. However, Jedi were taught to remember that all may not have been as it seemed, and that they should respect other cultures, even if they clashed with a Jedi's moral or ethical code. Jedi were also warned not to act in areas out of their jurisdiction, and to always consider the consequences of their actions.[4]
    ''')