from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    task = models.ManyToManyField(Task)
