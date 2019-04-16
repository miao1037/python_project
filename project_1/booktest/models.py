from django.db import models

# Create your models here.

class BookInfo(models.Model):
    Btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    hbook = models.ForeignKey("BookInfo",on_delete=models.CASCADE)
    def __str__(self):
        return self.hname



