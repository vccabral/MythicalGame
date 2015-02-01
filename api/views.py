from base.models import UserProfile
from base.models import Project
from base.models import Feature
from base.models import GitServer
from api.models import ProjectModelSerializer
from api.models import FeatureModelSerializer
from api.models import GitServerModelSerializer
from api.models import UserProfileModelSerializer
from rest_framework import routers
from rest_framework import viewsets
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.permissions import DjangoModelPermissions


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectModelSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Project.objects.all()

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


class FeatureViewSet(viewsets.ModelViewSet):
    serializer_class = FeatureModelSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = Feature.objects.all()

    def get_queryset(self):
        return Feature.objects.filter(project__owner=self.request.user)


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileModelSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = UserProfile.objects.all()

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)


class GitServerViewSet(viewsets.ModelViewSet):
    serializer_class = GitServerModelSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = GitServer.objects.all()


router = routers.DefaultRouter()
router.register(r'project', ProjectViewSet, base_name='project')
router.register(r'feature', FeatureViewSet, base_name='feature')
router.register(r'userprofile', UserProfileViewSet, base_name='userprofile')
router.register(r'server', GitServerViewSet, base_name='server')
