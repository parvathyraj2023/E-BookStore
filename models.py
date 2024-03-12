from django.db import models

# Create your models here.
class categorydb(models.Model):
    # Book_Name = models.CharField(max_length=50, null=True, blank=True)
    # Author_Name = models.CharField(max_length=50, null=True, blank=True)
    Category = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    # Language = models.CharField(max_length=50, null=True, blank=True)
    Category_Image = models.ImageField(upload_to="Profile", null=True, blank=True)

    # Price = models.IntegerField(null=True, blank=True)

class bookdb(models.Model):
    Category = models.CharField(max_length=50, null=True, blank=True)
    Book_Name = models.CharField(max_length=50, null=True, blank=True)
    Author_Name = models.CharField(max_length=50, null=True, blank=True)
    Language = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    Price = models.CharField(max_length=50, null=True, blank=True)
    Book_Image = models.ImageField(upload_to="Profile", null=True, blank=True)


