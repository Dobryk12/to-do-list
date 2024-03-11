from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ["status", "-date"]

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
