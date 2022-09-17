from django.template import context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_mails(group_name, post_title, body, recipients):
    context = {
        'group_name': group_name,
        'post_title': post_title,
        'body': body
    }
    email_body = render_to_string('email_template.txt', context)

    email = EmailMessage(
        subject = 'This was sent from BitByBit',
        body= email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipients,
        reply_to=['etimi5319@gmail.com']
    )

    return email.send(fail_silently=False)



#used to welcome users
def send_welcome_mail(recipient):
    
    email_body = render_to_string('welcome_mail.txt')

    email = EmailMessage(
        subject = 'This was sent from BitByBit',
        body= email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipient,
        reply_to=['bitbybit421@gmail.com']
    )

    return email.send(fail_silently=False)






def welcome_subscriber_mail(recipient, custom_message):

    context = {'custom_message': custom_message}

    email_body = render_to_string('new_subscriber.txt', context)

    email = EmailMessage(
        subject = 'This was sent from BitByBit',
        body= email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipient,
        reply_to=['bitbybit421@gmail.com']
    )

    return email.send(fail_silently=False)