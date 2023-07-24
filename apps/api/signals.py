from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from .models import Buyout, Product
from django.contrib.auth.models import User, Group

def get_admins():
    try:
        admins = Group.objects.get(name='Admin')
    except Group.DoesNotExist:
        return None
    return admins.user_set.all()

@receiver(post_save, sender=Buyout)
def send_buyout_notification_email(sender, instance, created, **kwargs):
    if created:
        admins = get_admins()
        mails = []
        for admin in admins:
            mails.append(admin.email)
        subject = 'Zebrands Buyout Confirmation'
        message = f'The user {instance.user.username} successfully purchased the product: {instance.product} for the price {instance.buyout_price}.'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = mails
        print(send_mail(subject, message, from_email, to_email, fail_silently=True))

@receiver(post_save, sender=Product)
def send_product_modified_notification_email(sender, instance, created, **kwargs):
    if not created:
        admins = get_admins()
        mails = [admin.email for admin in admins]
        subject = 'Zebrands Product Modified Notification'
        message = f'The product {instance.name} has been modified.'
        from_email = settings.DEFAULT_FROM_EMAIL

        for email in mails:
            print(send_mail(subject, message, from_email, [email], fail_silently=True))