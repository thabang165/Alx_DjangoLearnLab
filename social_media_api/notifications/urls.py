from django.urls import path
from .views import NotificationListView, MarkNotificationReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
    path('read/', MarkNotificationReadView.as_view(), name='mark-notification-read'),
]
