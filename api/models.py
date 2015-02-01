from base.models import UserProfile, Project, Feature, GitServer
from rest_framework import serializers


class GitServerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitServer


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project


class FeatureModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature


class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
