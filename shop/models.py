from django.db import models

class Product(models.Model):
	
	name = models.CharField(max_length=30)
	image = models.ImageField(upload_to='images/')
	desc = models.TextField()
	price = models.PositiveIntegerField()
	discount = models.PositiveIntegerField()
	rating = models.FloatField()
	stock = models.PositiveIntegerField()
	is_available = models.BooleanField()
	def __str__(self):
		return self.name

class Order(models.Model):
	product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
	delivery_address = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)



