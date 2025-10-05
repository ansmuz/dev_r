from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tool_images/', null=True, blank=True)  # Image field
    link = models.URLField()
    how_can_i_use_it = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='library_images/', null=True, blank=True)  # Image field
    link = models.URLField()
    how_can_i_use_it = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
