from django.db import models

class category(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name


class subcategory(models.Model):
    name=models.CharField(max_length=150)
    category=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name