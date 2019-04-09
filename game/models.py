from django.db import models
from django.contrib.auth.models import User


class Click(models.Model):

    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=50)
    click_count = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

