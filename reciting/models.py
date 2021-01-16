from django.db import models


class Dictionary(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)


class Word(models.Model):
    text = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    dic = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    recited = models.IntegerField(default=0)
