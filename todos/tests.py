from django.test import TestCase
from django.urls import reverse

from .models import Todo


class HomeViewTests(TestCase):
    def test_create_todo_via_post(self):
        # arrange: никаких задач в базе
        self.assertEqual(Todo.objects.count(), 0)

        # act: отправляем POST-запрос (имитация формы)
        response = self.client.post(
            reverse("home"),
            {
                "title": "Learn AI dev tools",
                "description": "Finish Django TODO app with AI help",
                "due_date": "",  # без дедлайна
                "is_done": "",   # не отмечаем как done
            },
            follow=True,
        )

        # assert: редирект на home и одна задача создана
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 1)
        todo = Todo.objects.first()
        self.assertEqual(todo.title, "Learn AI dev tools")
        self.assertFalse(todo.is_done)
