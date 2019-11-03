from django.db import models


class TemplateFiles(models.Model):
    template_name = models.CharField(max_length=50)
    date_saved = models.DateTimeField(auto_now_add=True)
    template_file = models.FileField()
