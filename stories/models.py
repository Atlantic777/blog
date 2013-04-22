from django.db import models
from django.contrib import admin
from taggit.managers import TaggableManager
from markdown import markdown

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=60)
	text	= models.TextField()
	rendered = models.TextField(editable=False, null=True, blank=True)
	datetime  = models.DateTimeField()
	tags = TaggableManager()

	def save(self):
		self.rendered = markdown(self.text, ['codehilite'])
		super(Post, self).save()

class Image(models.Model):
	image = models.ImageField(upload_to="images/")

admin.site.register(Post)
admin.site.register(Image)
