from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Resource(models.Model):
  # Title
  title = models.CharField(max_length=200)
  # Link
  link = models.URLField(null=True, blank=True)
  # Slug
  slug = models.SlugField(unique=True, max_length=200, verbose_name="Slug")
  # Author
  author = models.CharField(max_length=200)
  # Body
  body = RichTextField()
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

  def __str__(self):
    return self.title