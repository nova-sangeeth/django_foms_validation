from django.core.management.base import BaseCommand
from core.models import Jornal, Category, Author
import random
import datetime

categories = [
    'Sport',
    'Lifestyle',
    'music',
    'Coding',
    'travelling'
]

authors = [
    'John', 'Michael', 'luke', 'sally', 'jane', 'joe', 'Nova', 'guy'
]


# generate random data from the given text file.

# generate random author name
def generate_author_name():
    index = random.randint(0, 7)
    return authors[index]


# generate random categories
def generate_category_name():
    index = random.randint(0, 4)
    return categories[index]


# generate random views
def generate_view_count():
    return random.randint(0, 100)


# generate_random_views
def generate_is_reviewed():
    val = random.randint(0, 1)
    if val == 0:
        return False
    return True


# generate_random_dates
def generate_publish_date():
    year = random.randint(2000, 2020)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='this is the help area')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                title = row
                author_name = generate_author_name()
                category_name = generate_category_name()
                publish_date = generate_publish_date()
                views = generate_view_count()
                reviewed = generate_is_reviewed()

                author = Author.objects.get_or_create(
                    name=author_name
                )

                jornal = Jornal(
                    title=title,
                    author=Author.objects.get(name=author_name),
                    publish_date=publish_date,
                    views=views,
                    reviewed=reviewed
                )

                jornal.save()

                category = Category.objects.get_or_create(name=category_name)

                jornal.categories.add(Category.objects.get(name=category_name))

            self.stdout.write(self.style.SUCCESS('data imported successfully'))
