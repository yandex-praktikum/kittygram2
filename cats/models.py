from django.contrib.auth import get_user_model
from django.db import models

CHOICES = (
    ('Gray', 'Серый'),
    ('Black', 'Чёрный'),
    ('White', 'Белый'),
    ('Ginger', 'Рыжий'),
    ('Mixed', 'Смешанный'),
)

User = get_user_model()


class Achivement(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16, choices=CHOICES)
    birth_year = models.IntegerField()
    owner = models.ForeignKey(
        User, related_name='cats', on_delete=models.CASCADE)
    achivements = models.ManyToManyField(Achivement, through='AchivementCat')

    def __str__(self):
        return self.name


class AchivementCat(models.Model):
    achivement = models.ForeignKey(Achivement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achivement} {self.cat}'
