import json

from tqdm import tqdm
from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredient, Tag


class Command(BaseCommand):
    help = 'Downloading ingredients and tags.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Command start'))
        with open(
                f'{settings.BASE_DIR}/data/ingredients.json',
                encoding='utf-8') as data_file_ingredients:
            ingredient_data = json.loads(data_file_ingredients.read())
            Ingredient.objects.bulk_create(
                Ingredient(**ingredients)
                for ingredients in tqdm(ingredient_data)
            )

        with open(
                f'{settings.BASE_DIR}/data/tags.json',
                encoding='utf-8') as data_file_tags:
            tags_data = json.loads(data_file_tags.read())
            Tag.objects.bulk_create(Tag(**tags) for tags in tqdm(tags_data))

        self.stdout.write(self.style.SUCCESS('Данные загружены'))
