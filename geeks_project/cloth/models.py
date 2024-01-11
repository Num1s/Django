from django.db import models

class CustomerCloth(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True, default='+996')

    def __str__(self):
        return self.name


class TagCloth(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'#{self.name}'


class ProductCloth(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    tags = models.ManyToManyField(TagCloth)

    def __str__(self):
        return self.name


class OrderCloth(models.Model):
    STATUS = (
        ('на обработке', 'на обработке'),
        ('выехал', 'выехал'),
        ('доставлен', 'доставлен'),
    )
    customer = models.ForeignKey(CustomerCloth, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductCloth, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, default='на обработке')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
