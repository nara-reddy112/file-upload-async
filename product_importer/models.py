from django.db import models
from django.contrib.postgres.fields import CICharField

class Product(models.Model):
	sku = CICharField(max_length=200, unique=True)
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	is_active = models.BooleanField(default=True)