import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Puppy
from ..serializers import PuppySerializer

# initialize the APIClient app
client = Client()

class GetAllPuppiesTest(TestCase):
    """
    Test module for GET all puppies API
    """
    def setUp(self) -> None:
        Puppy.objects.create(
            name = 'Casper',
            age = 3,
            breed = 'Bull Dog',
            color = 'Black'
        )
        Puppy.objects.create(
            name = 'Muffin',
            age = 1,
            breed = 'Gradane',
            color = 'Brown'
        )
        Puppy.objects.create(
            name = 'Rambo',
            age = 2,
            breed = 'Labrador',
            color = 'Black'
        )
        Puppy.objects.create(
            name = 'Ricky',
            age = 6,
            breed = 'Labrador',
            color = 'Brown'
        )
    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_puppy'))
        
        # get data from db
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSinglePuppyTest(TestCase):
    """
    Test module for GET single puppy API
    """
    def setUp(self) -> None:
        self.casper = Puppy.objects.create(
            name = 'Casper',
            age = 3,
            breed = 'Bull Dog',
            color = 'Black'
        )
        self.muffin = Puppy.objects.create(
            name = 'Muffin',
            age = 1,
            breed = 'Gradane',
            color = 'Brown'
        )
        self.rambo = Puppy.objects.create(
            name = 'Rambo',
            age = 2,
            breed = 'Labrador',
            color = 'Black'
        )
        self.ricky = Puppy.objects.create(
            name = 'Ricky',
            age = 6,
            breed = 'Labrador',
            color = 'Brown'
        )
    def test_get_valid_puppy(self):
        response = client.get(reverse('get_delete_update_puppy', kwargs={'pk': self.rambo.pk}))
        puppy = Puppy.objects.get(pk = self.rambo.pk)
        serializer = PuppySerializer(puppy)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_invalid_single_puppy(self):
        response = client.get(reverse('get_delete_update_puppy', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
class CreateNewPuppyTest(TestCase):
    """
    Test module for POST a new puppy
    """
    def setUp(self) -> None:
        self.valid_puppy = {
            'name' : 'Rambo',
            'age' : 2,
            'breed' : 'Labrador',
            'color' : 'Black'
        }
        self.duplicated_puppy1 = self.duplicated_puppy2 = {
            'name' : 'Casper',
            'age' : 3,
            'breed' : 'Bull Dog',
            'color' : 'Black'
        }
        self.invalid_puppy = {
            'name' : '',
            'age' : 4,
            'breed' : 'Labrador',
            'color' : 'Black'
        }
    def test_post_valid_puppy(self):
        response = client.post(
            reverse('get_post_puppy'),
            data=json.dumps(self.valid_puppy),
            content_type='application/json'
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_post_invalid_puppy(self):
        response = client.post(
            reverse('get_post_puppy'),
            data=json.dumps(self.invalid_puppy),
            content_type='application/json'
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        

class UpdateSinglePuppyTest(TestCase):
    """
    Test module for PUT a new puppy
    """
    def setUp(self) -> None:
        self.valid_puppy = {
            'name' : 'Rambo',
            'age' : 2,
            'breed' : 'Labrador',
            'color' : 'Black'
        }
        self.invalid_puppy = {
            'name' : '',
            'age' : 4,
            'breed' : 'Labrador',
            'color' : 'Black'
        }
        self.casper = Puppy.objects.create(
            name = 'Casper',
            age = 3,
            breed = 'Bull Dog',
            color = 'Black'
        )
        self.muffin = Puppy.objects.create(
            name = 'Muffin',
            age = 1,
            breed = 'Gradane',
            color = 'Brown'
        )
    def test_put_valid_puppy(self):
        response = client.put(
            reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.valid_puppy),
            content_type='application/json'
            )
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_put_invalid_puppy(self):
        response = client.put(
            reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.invalid_puppy),
            content_type='application/json'
            )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
class DeleteSinglePuppyTest(TestCase):
    """
    Test module for DELETE a puppy
    """
    def setUp(self) -> None:
        self.casper = Puppy.objects.create(
            name = 'Casper',
            age = 3,
            breed = 'Bull Dog',
            color = 'Black'
        )
        self.muffin = Puppy.objects.create(
            name = 'Muffin',
            age = 1,
            breed = 'Gradane',
            color = 'Brown'
        )
    def test_delete_valid_puppy(self):
        response = client.delete(reverse('get_delete_update_puppy', kwargs={'pk':self.casper.pk}))        
        self.assertTrue(response.status_code, status.HTTP_204_NO_CONTENT)
    def test_delete_invalid_puppy(self):
        response = client.delete(reverse('get_delete_update_puppy', kwargs={'pk':444}))        
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)

