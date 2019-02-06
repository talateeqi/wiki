from django.db import models
from django.urls import reverse 
# Create your models here.
class Page(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	last_update = models.DateTimeField(auto_now=True)

	def  get_absolute_url(self):
		return reverse("page-detail", kwargs={'page_id': self.id})
