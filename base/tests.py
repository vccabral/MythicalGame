from django.test import TestCase
from base.models import UserProfile

class ModelsTestCase(TestCase):
	def test_profile(self):
		self.assertEqual(0, UserProfile.objects.all().count())
				
