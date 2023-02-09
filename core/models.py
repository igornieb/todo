from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.db.models.signals import post_save
from django.conf import settings

User = get_user_model()


class Account(models.Model):
    def __str__(self):
        return self.user.username

    def media_path(self, filename):
        return f'static/media/{self.pk}/{filename}'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to=media_path, default='static/media/blank.png')


def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance).save()


post_save.connect(create_account, sender=User)


class Task(models.Model):
    def edit_date(self):
        return self.date

    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    task = models.TextField()
    is_done = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now())

