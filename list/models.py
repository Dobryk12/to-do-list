from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)
    deadline = models.DateField(auto_now=True, blank=True, null=True)
    status = models.BooleanField
    tags = models.ManyToManyField("Tags", related_name="tasks")

    class Meta:
        ordering = ["status", "-date"]

    def __str__(self):
        return self.content


class Tags(models.Model):
    name = models.CharField(max_length=255)
