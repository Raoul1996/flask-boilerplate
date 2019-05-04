from flask_mail import Message
from werkzeug.exceptions import InternalServerError
from api import mail
import smtplib


def send_mail(subject,
              html,
              sender,
              recipients):
    try:
        msg = Message(
            subject=subject,
            sender=sender,
            recipients=recipients,
            html=html
        )
        mail.send(msg)
        return {"message": "Send mail successfully", "code": 0}
    except smtplib.SMTPAuthenticationError:
        raise InternalServerError(description="SMTP Authentication failed", response=500)
    except smtplib.SMTPRecipientsRefused:
        raise InternalServerError(description="Unable to send email to {}".format(recipients), response=500)
    except Exception as e:
        raise e
