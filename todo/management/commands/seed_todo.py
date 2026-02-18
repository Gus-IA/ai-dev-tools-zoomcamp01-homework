from django.core.management.base import BaseCommand
from todo.models import Todo
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Seeds the database with fake TODO data'

    def handle(self, *args, **kwargs):
        Todo.objects.all().delete()
        
        quests = [
            {
                'title': 'Slay the Bug Dragon',
                'description': 'Find and fix the mysterious race condition in the authentication logic.',
                'due_date': timezone.now() + datetime.timedelta(days=2),
                'is_completed': False
            },
            {
                'title': 'Brew the Espresso Potion',
                'description': 'Master the art of the perfect extraction to boost developer energy.',
                'due_date': timezone.now() + datetime.timedelta(hours=5),
                'is_completed': True
            },
            {
                'title': 'Map the Documentation Forest',
                'description': 'Explore the undocumented functions and create a guide for future travelers.',
                'due_date': timezone.now() + datetime.timedelta(days=7),
                'is_completed': False
            },
            {
                'title': 'Refactor the Legacy Dungeon',
                'description': 'Clean up the spaghetti code in the core engine module.',
                'due_date': timezone.now() + datetime.timedelta(days=3),
                'is_completed': False
            },
            {
                'title': 'Summit the Deployment Peak',
                'description': 'Automate the production pipeline for faster delivery.',
                'due_date': timezone.now() + datetime.timedelta(days=1),
                'is_completed': False
            }
        ]

        for quest in quests:
            Todo.objects.create(**quest)
            self.stdout.write(self.style.SUCCESS(f"Successfully created quest: {quest['title']}"))
