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
    
class product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE,null=False,default='')
    subcategory=models.ForeignKey(subcategory,on_delete=models.CASCADE,null=False,default='')
    image=models.ImageField(upload_to="ecomers/ping")
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name