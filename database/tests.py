from django.test import TestCase


class SettingsTestCase(TestCase):
	def test_settings(self):
		from django.conf import settings

		self.assertEqual(settings.TEST_RUNNER, 'django_nose.NoseTestSuiteRunner')
