from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Music(models.Model):

    userId = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    songTitle = models.CharField(max_length=100, default='')
    Artist = models.CharField(max_length=100, default='')

    dateCreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.songTitle
    def get_absolute_url(self):
        return reverse('music-detail', kwargs={'pk': self.pk})
