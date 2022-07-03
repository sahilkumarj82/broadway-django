from xml.etree.ElementTree import Comment
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=300)
    post = models.CharField(max_length=254)
    Comment = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name

class Information(models.Model):
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)
    time = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.address1}, {self.address2}, {self.phone},{self.time}, {self.email}"


class Services(models.Model):
    title = models.TextField()
    comment = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.title