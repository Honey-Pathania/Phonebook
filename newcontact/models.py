from django.db import models

class Phonebook(models.Model):
    Name = models.CharField(max_length=30)
    Contact = models.CharField(unique=True, max_length=12)

    def __str__(self):
        return self.Name
