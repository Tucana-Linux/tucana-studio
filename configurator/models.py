from django.db import models

# Create your models here.
class Config(models.Model):
    name = models.CharField(max_length=200)
    userID = models.CharField()
    desktop = models.CharField(max_length=10)
    packages = models.JSONField()
    # meta includes autostart apps, systemd services enabled, and what shell the user wants to use
    # any 'new' settings that need to be added later can be added to this json
    meta = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    