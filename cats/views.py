from rest_framework import viewsets

from .models import achievement, Cat, User

from .serializers import achievementSerializer, CatSerializer, UserSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class achievementViewSet(viewsets.ModelViewSet):
    queryset = achievement.objects.all()
    serializer_class = achievementSerializer
