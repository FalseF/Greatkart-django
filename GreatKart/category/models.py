from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    cat_photo=models.ImageField(upload_to='photos/categories/', blank=True)
    description=models.TextField(max_length=200, blank=True)
    #database e model er name tik rakhar jonno nicher code likhte hoy
    #ar na likhle atuo name er sathe s add kore plural kore nibe
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    # category te link deoyar jonno nicher code 
    # ekhane "products_by_category" asche store urls.py er  name ="products_by_category" theke
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
        
    def __str__(self):
        return self.category_name