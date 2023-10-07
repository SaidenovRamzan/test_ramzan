from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order import views

router = DefaultRouter()
router.register(r'order', views.OrderViewSets)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/test',views.Test.as_view()),
]
