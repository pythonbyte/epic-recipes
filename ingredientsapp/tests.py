from django.test import TestCase, Client
from .models import Ingredient


class TesstIngredientEndpoints(TestCase):

    def setUp(self):
        self.client = Client()

    def test_list_ingredient(self):
        Ingredient.objects.create(
            name='test',
            article_number='1234564',
            cost=2.5,
            amount=1,
            unit='KG'
        )
        response = self.client.get('/ingredients/')
        query = response.context_data['object_list']
        self.assertEqual(query.count(), 1)
        self.assertEqual(response.status_code, 200)


    def test_create_ingredient(self):
        correct_data = {
            'name': 'Teste',
            'article_number': '5653463543535',
            'cost': 3.0,
            'amount': 1,
            'unit': 'G'
        }
        self.assertEqual(Ingredient.objects.all().count(), 0)

        response = self.client.post('/ingredients/new', data=correct_data)
        ingredient = Ingredient.objects.first()
        self.assertEqual(Ingredient.objects.all().count(), 1)
        self.assertEqual(response.status_code, 302)
        for k,v in correct_data.items():
            self.assertEqual(getattr(ingredient, k), v)

    def test_create_ingredient_invalid_data(self):
        incorrect_data = {
            'name': 'Teste',
            'article_number': '',
            'cost': 3.0,
            'amount': 1,
            'unit': 'G'
        }
        self.assertEqual(Ingredient.objects.all().count(), 0)

        response = self.client.post('/ingredients/new', data=incorrect_data)
        self.assertEqual(Ingredient.objects.all().count(), 0)
        self.assertEqual(response.status_code, 200)

    def test_update_ingredient(self):
        old_ingredient = Ingredient.objects.create(
            name='test',
            article_number='1234564',
            cost=2.5,
            amount=1,
            unit='KG'
        )
        new_data = {
            'name': 'test',
            'article_number': '1234564',
            'cost': 3.0,
            'amount': 2,
            'unit': 'G'
        }

        response = self.client.post(f'/ingredients/edit/{old_ingredient.id}', data=new_data)
        self.assertEqual(response.status_code, 302)
        updated_ingredient = Ingredient.objects.get(id=old_ingredient.id)
        for k,v in new_data.items():
            self.assertEqual(getattr(updated_ingredient, k), v)

    def test_delete_ingredient(self):
        ingredient = Ingredient.objects.create(
            name='test',
            article_number='1234564',
            cost=2.5,
            amount=1,
            unit='KG'
        )
        self.assertEqual(Ingredient.objects.all().count(), 1)

        response = self.client.post(f'/ingredients/delete/{ingredient.id}')
        self.assertEqual(Ingredient.objects.all().count(), 0)
        self.assertEqual(response.status_code, 302)
