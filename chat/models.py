from django.db import models
# Imports reverse to return url after Room is created
from django.urls import reverse
# Timezone for chats
from django.utils import timezone


class Room(models.Model):
    name = models.CharField(max_length = 20)
    # Absolute url redirect after creation
    def get_absolute_url(self):
        return reverse("room-detail", kwargs={"pk": self.pk})
    

# Basic Blog-Style Comment Model
class Comment(models.Model): 
    post = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=20) 
    comment = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now) 

    class Meta: 
        ordering = ('date',) 
    