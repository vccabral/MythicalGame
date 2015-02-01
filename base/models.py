from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


class UserProfile(models.Model):
	user = models.OneToOneField(User)
def user_saved(*args, **kwargs):
	from django.contrib.auth.models import User
	if kwargs["created"]:
		UserProfile.objects.create(user=kwargs["instance"])
post_save.connect(user_saved, User)


class GitServer(models.Model):
	fqdn = models.CharField(max_length=200)
	api_key = models.CharField(max_length=50)


class Project(models.Model):
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Feature(models.Model):
	project = models.ForeignKey(Project)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=1000, blank=True)
	estimated_test_cases = models.IntegerField(default=0)
	estimated_objects = models.IntegerField(default=0)
	estimated_methods = models.IntegerField(default=0)
	estimated_man_months = models.IntegerField(default=0)


