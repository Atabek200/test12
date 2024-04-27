from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    full_text = models.TextField(max_length=200)
    date = models.DateTimeField('Дата публикаци')

    def __str__(self):
        return self.name
