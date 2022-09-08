import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

from settings import MAIL_EMAIL, MAIL_PASS
import utils.templates.html_temp as templates


def send_daily_report_on_mail(recipient_mail: str, recipient_name:str, filepath: str, filename_to_send:str):
    email = MAIL_EMAIL
    password = MAIL_PASS
    server = smtplib.SMTP_SSL('smtp.yandex.ru')
    server.set_debuglevel(1)
    server.secure = True
    server.login(email, password)
    server.ehlo(email)
    #

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filepath, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{filename_to_send}"')


    msg = MIMEMultipart('alternative')
    msg['Subject'] = "DAILY"
    msg['From'] = email
    msg['To'] = recipient_mail
    msg.attach(part)

    html_template = MIMEText(templates.get_html_template(recipient_name), 'html')
    msg.attach(html_template)

    server.sendmail(email, recipient_mail, msg.as_string())
    server.quit()
