#  Copyright (c) 2021. Julio Cezar Riffel
#  https://github.com/julioriffel

from django.db import models


class Mymessage(models.Model):
    msg = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id:.2f} - {self.msg} - {self.created_at.strftime('%d/%m/%Y %H:%M:%S')}"
