from django.db import models


class Musician(models.Model):

    name = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Имя исполнителя')
    

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class Album(models.Model):

    name = name = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Название альбома')

    musician = models.ForeignKey(
        Musician,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель')
    
    year = models.PositiveSmallIntegerField(
        verbose_name='Год выхода')
    
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ["musician"]

    def __str__(self):
        return self.name


class Song(models.Model):

    name = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Название песни')
    
    musician = models.ForeignKey(
        Musician,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель')
    
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        verbose_name='Альбом')

    number = models.PositiveSmallIntegerField(
        verbose_name='Порядковый номер в альбоме')
    
    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(fields=['album', 'number'],
                                    name='unique_album_number')
        ]

    def __str__(self):
        return  f'{self.name} - {self.musician} - {self.album}'
