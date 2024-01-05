from django.db import models
from ckeditor.fields import RichTextField

# Define Blog Models Here
class Blog:


  def __str__(self):
    # Title
    title = models.CharField(max_length=200)
    # Date Published
    pub_date = models.DateField("date published")
    # Body

