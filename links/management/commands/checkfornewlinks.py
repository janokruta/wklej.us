from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.template.loader import get_template
from django.utils import timezone

from links.models import Link


class Command(BaseCommand):
    help = """This command send email to admin if there is a new link added
              within 24 hours"""

    def handle(self, *args, **options):
        yesterday = timezone.now() - timedelta(days=1)
        links = Link.objects.filter(timestamp__gte=yesterday).values('slug')

        if links.exists():
            urls = [f"wklej.us/{link['slug']}" for link in links]
            subject = 'Nowe linki na stronie!' if links.count() > 1 else 'Nowy link na stronie!'
            message = get_template('links/mailing/checkfornewlinks.txt').render({'urls': urls})
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['jan.okruta@gmail.com']
            html_message = get_template('links/mailing/checkfornewlinks.html').render({'urls': urls})
            send_mail(subject, message, from_email, recipient_list, html_message=html_message)
