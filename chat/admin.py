#  Copyright (c) 2021. Julio Cezar Riffel
#  https://github.com/julioriffel

from django.contrib import admin

from chat.models import Mymessage


@admin.register(Mymessage)
class Mymessageadmin(admin.ModelAdmin):
    list_display = ('id', 'msg', 'created_at')
    list_filter = ('msg',)
