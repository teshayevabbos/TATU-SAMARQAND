from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    

class TeacherModell(models.Model):
    img = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=200)
    occupation = models.CharField(max_length=100)
    rate = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class InfoModell(models.Model):
    img = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=200)
    occupation = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    rate = models.CharField(max_length=50)
    teacher = models.ForeignKey(TeacherModell,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
