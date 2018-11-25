from django.db import models

# Create your models here.
class path(models.Model):
    x = models.DecimalField(max_digits=32, decimal_places=8)
    y = models.DecimalField(max_digits=32, decimal_places=8)
    z = models.DecimalField(max_digits=32, decimal_places=8)
    next = models.ForeignKey('path', null=True, blank=True, on_delete=models.CASCADE)


class area(models.Model):
    path_root = models.ForeignKey('path', on_delete=models.CASCADE)
    collection = models.ForeignKey('collection', on_delete=models.CASCADE)


class point(models.Model):
    x = models.DecimalField(max_digits=32, decimal_places=8)
    y = models.DecimalField(max_digits=32, decimal_places=8)
    z = models.DecimalField(max_digits=32, decimal_places=8)
    collection = models.ForeignKey('collection', on_delete=models.CASCADE)


class collection(models.Model):
    name = models.TextField()
    map_type = models.TextField(choices=(('galaxy', 'GAL'),
                                         ('Pact Worlds', 'PCT'),))
    area_color = models.TextField()
    element_color = models.TextField()
    fill_color = models.TextField()

