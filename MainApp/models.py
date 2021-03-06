from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """
    A simple model with some text and then the date.
    """

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """
    A class to add entries to each topic as neeeded
    """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # class Meta

    def __str__(self):
        return self.text
