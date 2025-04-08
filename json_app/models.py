# models.py
from django.db import models

from django.utils.text import slugify



class Theme(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

    def delete(self, *args, **kwargs):
        # Supprimer toutes les figures associées
        self.charts.all().delete()
        super().delete(*args, **kwargs)

    
class HighchartData(models.Model):
    CHART_TYPES = [
        ('line', 'Série'),
        ('column', 'Histogramme'), 
        ('pie', 'Camembert'),
        ('spline', ' Courbe lissée'),
        ('area', 'Aire'),
        ('bar', 'Barre'),
        ('scatter', 'Nuage de points')
    ]

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='charts')
    title = models.CharField(max_length=255)
    labels = models.TextField(default="labels")
    values = models.TextField(default="25")
    
    chart_type = models.CharField(max_length=10, choices=CHART_TYPES, default='line')

    x_axis_title = models.CharField(max_length=50, blank=True, null=True)
    y_axis_title = models.CharField(max_length=50, blank=True, null=True)
    show_legend = models.BooleanField(default=False)
    legend_position = models.CharField(max_length=10, choices=[('top', 'Haut'), ('bottom', 'Bas')], default='top')

    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)
    width = models.IntegerField(default=6)
    height = models.IntegerField(default=4)
    

    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title