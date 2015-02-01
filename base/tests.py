from django.test import TestCase
from base.models import UserProfile, user_saved
from mock import Mock, patch


class ModelsTestCase(TestCase):

	@patch('base.models.UserProfile.objects.create')
	def test_user_created(self, user_profile):
		kwargs = {"created": True, "instance": Mock()}
		user_saved(*[], **kwargs)
		user_profile.assert_called_with(user=kwargs["instance"])
				

	@patch('base.models.UserProfile.objects.create')
	def test_user_updated(self, user_profile):
		kwargs = {"created": False, "instance": Mock()}
		user_saved(*[], **kwargs)
		self.assertEqual(user_profile.call_args_list, [])


	def test_urls(self):
		from mythicalcode.urls import urlpatterns


