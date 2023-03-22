from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name