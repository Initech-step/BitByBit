from celery import shared_task
from celery.utils.log import get_task_logger
from .send_letter import send_mails, send_welcome_mail, welcome_subscriber_mail

logger = get_task_logger(__name__)

@shared_task
def add(x, y):
    return x + y


@shared_task(name='send_newsletter')
def send_newsletter(group_name, post_title, body, recipients):
    print('enter')
    logger.info('Email from BitByBit has been sent')
    return send_mails(group_name, post_title, body, recipients)




@shared_task(name='welcome_user')
def welcome_mail(recipient):
    logger.info('Welcome email has been sent')
    return send_welcome_mail(recipient)




@shared_task(name='new_subscriber_letter')
def new_subscriber_letter(recipient, custom_message):
    logger.info('Welcome subscriber email has been sent')
    return welcome_subscriber_mail(recipient, custom_message)