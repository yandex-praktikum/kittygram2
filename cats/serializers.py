import datetime as dt

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import CHOICES, Achivement, AchivementCat, Cat, User


class UserSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'cats')


class AchivementSerializer(serializers.ModelSerializer):
    achivement_name = serializers.CharField(source='name')

    class Meta:
        model = Achivement
        fields = ('id', 'achivement_name')


class CatSerializer(serializers.ModelSerializer):
    achivements = AchivementSerializer(many=True, required=False)
    color = serializers.ChoiceField(choices=CHOICES)
    age = serializers.SerializerMethodField()
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year',
                  'achivements', 'owner', 'age')

    def get_age(self, obj):
        return dt.datetime.now().year - obj.birth_year

    def create(self, validated_data):
        if 'achivements' not in self.initial_data:
            cat = Cat.objects.create(**validated_data)
            return cat
        else:
            achivements = validated_data.pop('achivements')
            cat = Cat.objects.create(**validated_data)
            for achivement in achivements:
                current_achivement, status = Achivement.objects.get_or_create(
                    **achivement)
                AchivementCat.objects.create(
                    achivement=current_achivement, cat=cat)
            return cat
