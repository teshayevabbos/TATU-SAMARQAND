from django.db import models

class TeamModel(models.Model):
    ful_name = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='image/')
    subject = models.CharField(max_length=100)
    telegram = models.URLField('Your telegram profile')
    instagram = models.URLField('Your instagram profile',blank=True)
    github = models.URLField('Your GitHub profile')
    email = models.EmailField('Your Email')


    def __str__(self):
        return self.ful_name

