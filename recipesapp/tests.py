from io import BytesIO
from PIL import Image

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase, Client

from .models import Recipe, RecipeIngredient
from ingredientsapp.models import Ingredient


class TesstRecipeEndpoints(TestCase):
    def setUp(self):
        self.client = Client()

        im = Image.new(mode="RGB", size=(200, 200))
        im_io = BytesIO()
        im.save(im_io, "JPEG")
        im_io.seek(0)

        self.image = InMemoryUploadedFile(
            im_io, None, "test.jpg", "image/jpeg", len(im_io.getvalue()), None
        )

    def test_create_recipe(self):
        ingredient = Ingredient.objects.create(
            name="test", article_number="1234564", cost=2.5, amount=1, unit="KG"
        )
        form_data = {
            'form-0-DELETE': '',
            'form-0-amount': '100',
            'form-0-id': '',
            'form-0-ingredient': ingredient.id,
            'form-0-unit': 'G',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '1000',
            'form-MIN_NUM_FORMS': '0',
            'form-TOTAL_FORMS': '1',
            'name': 'test',
            'preparation_time': '45',
            'image_file': self.image
        }
        self.assertEqual(Recipe.objects.all().count(), 0)
        self.assertEqual(RecipeIngredient.objects.all().count(), 0)

        response = self.client.post('/new', data=form_data)

        self.assertEqual(Recipe.objects.all().count(), 1)
        self.assertEqual(RecipeIngredient.objects.all().count(), 1)
        self.assertEqual(response.status_code, 302)


    def test_update_recipe(self):
        ingredient = Ingredient.objects.create(
            name="test", article_number="1234564", cost=2.5, amount=1, unit="KG"
        )
        recipe = Recipe.objects.create(name="test", preparation_time="30",)
        form_data = {
            'form-0-DELETE': '',
            'form-0-amount': '100',
            'form-0-id': '',
            'form-0-ingredient': ingredient.id,
            'form-0-unit': 'G',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '1000',
            'form-MIN_NUM_FORMS': '0',
            'form-TOTAL_FORMS': '1',
            'name': 'Chocolate Cake',
            'preparation_time': 45,
            'image_file': self.image
        }

        response = self.client.post(f'/edit/{recipe.id}', data=form_data)

        new_recipe = Recipe.objects.first()
        self.assertEqual(Recipe.objects.all().count(), 1)
        self.assertEqual(RecipeIngredient.objects.all().count(), 1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(form_data['name'], new_recipe.name)
        self.assertEqual(form_data['preparation_time'], new_recipe.preparation_time)

    def test_delete_recipe(self):
        recipe = Recipe.objects.create(name="test", preparation_time="30",)
        self.assertEqual(Recipe.objects.all().count(), 1)

        response = self.client.post(f'/delete/{recipe.id}')

        self.assertEqual(Recipe.objects.all().count(), 0)
        self.assertEqual(response.status_code, 302)
