from django.db import models

# Create your models here.
class table(models.Model):
    text=models.TextField(max_length=100)
    date=models.DateField()
    def __str__(self):
        return self.text