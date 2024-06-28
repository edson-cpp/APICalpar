from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=100)
    disponivel = models.BooleanField()

    def __str__(self):
        return self.nome
