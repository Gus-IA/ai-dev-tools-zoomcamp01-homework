from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    def test_todo_creation(self):
        todo = Todo.objects.create(
            title="Test Task",
            description="Test Description",
            is_completed=False
        )
        self.assertEqual(todo.title, "Test Task")
        self.assertFalse(todo.is_completed)
        self.assertIsNotNone(todo.created_at)

    def test_todo_str(self):
        todo = Todo.objects.create(title="String Test")
        self.assertEqual(str(todo), "String Test")
