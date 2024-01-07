from django.db import models
from ckeditor.fields import RichTextField

# Define Blog Models Here
class Blog:
  # Title
  title = models.CharField(max_length=200)
  # Date Published
  pub_date = models.DateField("date published")
  # Body
  body = models.TextField()
  # Slug
  slug = models.SlugField(unique=True, max_length=200, verbose_name="Slug")

  def __str__(self):
    return self.title