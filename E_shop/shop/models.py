from django.db import models

class category(models.Model):
    name=models.CharField(max_length=150)


class subcategory(models.Model):
    name=models.CharField(max_length=150)
    category=models.ForeignKey(category,on_delete=models.CASCADE)