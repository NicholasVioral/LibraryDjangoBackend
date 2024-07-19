# api/models.py

from django.db import models

class Book(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    STATUS_CHOICES = [
        ('want_to_read', 'Want to Read'),
        ('currently_reading', 'Currently Reading'),
        ('read', 'Read')
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='want_to_read')

    def __str__(self):
        return self.title
