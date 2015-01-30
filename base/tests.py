from django.test import TestCase
from database.models import UserProfile

class ModelsTestCase(TestCase):
	def test_profile(self):
		self.assertEqual(0, UserProfile.objects.all().count())
				
