from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, unique=True)

# Create your models here.
class SecretSantaAssignment(models.Model):
    giver = models.ForeignKey(User, related_name='giver', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)

    def __str__(self):
        return self.giver + " gives to " + self.receiver
