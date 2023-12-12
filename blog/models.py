from django.db import models

# Create your models here.

class postzinho(models.Model):
  title = models.CharField(max_length=100)
  texto = models.TextField(max_length=1000)
  image = models.ImageField(null=True, blank=True, upload_to="images/")
  color = models.CharField(max_length=7, default="#FFFFFF")
  signt = models.CharField(max_length=50, default="anon")

  def __str__(self):
    return self.title