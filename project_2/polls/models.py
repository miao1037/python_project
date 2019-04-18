from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class Options(models.Model):
    one = models.CharField(max_length=20)
    ovote = models.IntegerField(default=0)
    Oquestion = models.ForeignKey("Questions",on_delete=models.CASCADE)
    def __str__(self):
        return self.one

    def option(self):
        return self.one
    option.short_description = '选项'

    def poll(self):
        return self.ovote
    poll.short_description = '票数'

