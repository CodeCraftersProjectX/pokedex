from django.db import models

class Pokemon(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    description = models.TextField()

    class Meta:
        """
        メタクラス
        """
        db_table = 'pokemon'
        verbose_name = 'ポケモン'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

