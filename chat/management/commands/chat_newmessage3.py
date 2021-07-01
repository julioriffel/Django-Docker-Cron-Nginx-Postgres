#  Copyright (c) 2021. Julio Cezar Riffel
#  https://github.com/julioriffel
#

from django.core.management.base import BaseCommand

from chat.models import Mymessage


class Command(BaseCommand):
    help = 'Inserir Nova Mensagem'

    def handle(self, *args, **options):
        Mymessage.objects.create(msg='3 Minutos')

        return
