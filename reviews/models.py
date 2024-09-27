from django.contrib.auth.models import User
from django.db import models

class Review(models.Model):
    movie_title = models.CharField(max_length=255)
    review_content = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.movie_title} - {self.rating} stars'