from django.db import models

# add model size
class Size(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# add model size
class Pizza(models.Model):
    topping1 = models.CharField(max_length=200)
    topping2 = models.CharField(max_length=200)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
