from django.core.management.base import BaseCommand
from tasks.models import Category


CATEGORIES = [
    "Personal",
    "Work",
    "Shopping",
]


class Command(BaseCommand):
    help = "Seed default categories (Personal, Work, Shopping)"

    def handle(self, *args, **options):
        created = 0
        for name in CATEGORIES:
            obj, was_created = Category.objects.get_or_create(name=name)
            if was_created:
                created += 1

        total = Category.objects.filter(name__in=CATEGORIES).count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded categories. Newly created: {created}. Present total: {total}."
            )
        )
