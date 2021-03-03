from django.db import models
import datetime

choice = [('AG', 'Agriculture'), ('HC', 'Handicraft'), ('RL', 'Religious'), ('FD', 'Food'), ('MD', 'Manufactured')]

class Products(models.Model):
    title = models.CharField(max_length=200)
    product_type = models.CharField(choices=choice, max_length=2)
    description = models.TextField()
    price = models.FloatField()
    image = models.URLField()
    origin = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.title