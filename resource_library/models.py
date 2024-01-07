from django.db import models

# Create your models here.

class Resource(models.Model):
  # Title
  title = models.CharField(max_length=200)
  # Link
  link = models.URLField()
  # Slug
  slug = models.SlugField(unique=True, max_length=200, verbose_name="Slug")
  # Author
  author = models.CharField(max_length=200)
  # Resource Type
  RESOURCE_TYPES = {
    "pdf": "PDF",
    "video": "Video",
    "podcast": "Podcast",
    "website": "Website",
    "book": "Book"
  }
  type = models.CharField(choices=RESOURCE_TYPES, max_length=50)
  # Date Published
  pub_date = models.DateField("date published")