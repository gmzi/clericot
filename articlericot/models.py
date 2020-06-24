from django.db import models
from datetime import datetime
from django.forms import URLField
# from django.http import JsonResponse (to be added)


class Statistics(models.Model):
    entry_id = models.AutoField(primary_key=True)
    link = models.URLField()
    created_at = models.DateTimeField()





