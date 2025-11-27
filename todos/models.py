from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)          # заголовок
    description = models.TextField(blank=True)        # описание (может быть пустым)
    due_date = models.DateTimeField(null=True, blank=True)  # дедлайн
    is_done = models.BooleanField(default=False)      # выполнено / нет

    def __str__(self):
        return self.title
