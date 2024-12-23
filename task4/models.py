from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=255)
    age = models.IntegerField()

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class GameBuyer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
