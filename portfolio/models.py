from django.db import models


# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/', blank=True, null=True) # noqa 
    url = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True)
    conclusion_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
