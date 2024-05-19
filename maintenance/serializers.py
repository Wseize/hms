from rest_framework import serializers
from .models import Category, Order, Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'services']



class OrderSerializer(serializers.ModelSerializer):
    service_name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'phone_number', 'name', 'location', 'comment', 'service', 'service_name', 'status', 'feedback_rating', 'created_at']

    def get_service_name(self, obj):
        if isinstance(obj.service, Service):
            return obj.service.name
        else:
            try:
                service_id = obj.service 
                service = Service.objects.get(id=service_id)
                return service.name
            except Service.DoesNotExist:
                return None
            


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']


class OrderFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['feedback_rating']