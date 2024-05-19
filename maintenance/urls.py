from django.urls import path
from .views import CategoryList, CategoryDetail, OrderCreate, OrderDetail, OrderFeedbackRatingUpdate, OrderStatusUpdate, ServiceList, ServiceDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('services/', ServiceList.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
    path('orders/', OrderCreate.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='service-detail'),
    path('orders/<int:pk>/status/', OrderStatusUpdate.as_view(), name='order-status-update'),
    path('orders/<int:pk>/feedback-rating/', OrderFeedbackRatingUpdate.as_view(), name='order-feedback-rating-update'),
]