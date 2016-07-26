from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    g_plus = models.CharField('G+ ID', max_length=32, blank=True)
    contact = models.CharField('Phone NUmber', max_length=32, blank=True)
    profile = models.ImageField('Profile Image', upload_to='uploads', blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def handle_user_save(sender, instance, created, **kwargs):
  if created:
    Developer.objects.create(user=instance)
