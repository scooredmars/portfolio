from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Portfolio(models.Model):
    image = models.ImageField(upload_to="projects",
                              default='/projects/work.jpg')
    title = models.CharField(verbose_name=_("Title"), max_length=50)
    gh_link = models.URLField(blank=True, null=True, max_length=100)
    web = models.URLField(blank=True, null=True, max_length=100)
    text = models.TextField(verbose_name=_("Text"), max_length=300)
    gh_not_link = models.BooleanField(default=True)
    in_progress = models.BooleanField(default=True)
    in_que = models.BooleanField(default=True)

    def __str__(self):
        return self.title
