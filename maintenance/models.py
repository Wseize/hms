from django.db import models

class Category(models.Model):    
    name = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self):
        return self.name



class Service(models.Model):
    category = models.ForeignKey(Category, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    


class Order(models.Model):
    RECEIVED = 'received'
    IN_PROGRESS = 'in_progress'
    IN_TRANSIT = 'in_transit'
    COMPLETE = 'complete'

    STATUS_CHOICES = [
        (RECEIVED, 'Received'),
        (IN_PROGRESS, 'In Progress'),
        (IN_TRANSIT, 'In Transit'),
        (COMPLETE, 'Complete'),
    ]

    FEEDBACK_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=RECEIVED)
    feedback_rating = models.IntegerField(choices=FEEDBACK_CHOICES, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Order for {self.service.name} by {self.name}"
