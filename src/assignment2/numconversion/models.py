from django.db import models
from audiofield.fields import AudioField
# Create your models here.
class converted(models.Model):
    audio=AudioField(upload_to="", blank=True,ext_whitelist=(".mp3", ".wav", ".ogg"),help_text=("Allowed type - .mp3, .wav, .ogg"))