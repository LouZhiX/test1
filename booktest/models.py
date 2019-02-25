from django.db import models

# Create your models here.
class Booktest(models.Model):
    btitle = models.CharField(max_length=50)
    #public_date = models.DateTimeField()

    def __str__(self):
        return self.btitle

class Hero(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hmajor = models.CharField(max_length=20)
    hbook = models.ForeignKey("Booktest")
    #first_time_occur = models.DateTimeField()

    def __str__(self):
        return self.hname

