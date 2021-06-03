import datetime as dt

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import CHOICES, achievement, achievementCat, Cat, User


class UserSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'cats')


class achievementSerializer(serializers.ModelSerializer):
    achievement_name = serializers.CharField(source='name')

    class Meta:
        model = achievement
        fields = ('id', 'achievement_name')


class CatSerializer(serializers.ModelSerializer):
    achievements = achievementSerializer(many=True, required=False)
    color = serializers.ChoiceField(choices=CHOICES)
    age = serializers.SerializerMethodField()
    
    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year', 'achievements', 'owner',
                  'age')

    def get_age(self, obj):
        return dt.datetime.now().year - obj.birth_year

    def create(self, validated_data):
        if 'achievements' not in self.initial_data:
            cat = Cat.objects.create(**validated_data)
            return cat
        else:
            achievements = validated_data.pop('achievements')
            cat = Cat.objects.create(**validated_data)
            for achievement in achievements:
                current_achievement, status = achievement.objects.get_or_create(
                    **achievement)
                achievementCat.objects.create(
                    achievement=current_achievement, cat=cat)
            return cat
