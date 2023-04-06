from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
    
    @property
    def songs(self):
        return self.song_set.all()


class Song(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')

    def __str__(self) -> str:
        return self.title
    