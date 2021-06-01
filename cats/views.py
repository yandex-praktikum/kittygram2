from rest_framework import viewsets

from .models import Achivement, Cat, User

from .serializers import AchivementSerializer, CatSerializer, UserSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchivementViewSet(viewsets.ModelViewSet):
    queryset = Achivement.objects.all()
    serializer_class = AchivementSerializer
