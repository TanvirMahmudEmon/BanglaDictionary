from django.db import models

# Create your models here.


class Dictionary(models.Model):   # Article = myblog
    word = models.CharField(max_length=200)  # title = word
    mean = models.TextField()  # body = mean
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)  # For Video No: 12

    def __unicode__(self):  # python: 2.7
        return self.word

    # vido 16 complete


