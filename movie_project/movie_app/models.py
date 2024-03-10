from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model




class User(models.Model):
    username=models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.username)

class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('movie_app:products_by_category', args=[self.slug, self.id])

    def __str__(self):
        return '{}'.format(self.name)
class products(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique=True)
    poster=models.ImageField(upload_to='poster')
    description=models.TextField()
    release_date=models.DateField()
    actors=models.CharField(max_length=255)
    category_id=models.ForeignKey(category,on_delete=models.CASCADE)
    trailer_link=models.URLField()
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        if not isinstance(self.user, get_user_model()):
            # Fetch the user instance based on the provided user information
            self.user = get_user_model().objects.get(username=self.user.username)

        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('movie_app:prodCatdetail',args=[self.category_id.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'


    def __str__(self):
        return '{}'.format(self.name)

    def average_rating(self):
        ratings = Rating.objects.filter(product=self)
        if ratings.exists():
            return sum(rating.rating for rating in ratings) / ratings.count()
        return 0

    def total_ratings(self):
        return Rating.objects.filter(product=self).count()


    
class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.rating}"
