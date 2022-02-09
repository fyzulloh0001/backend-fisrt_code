from django.urls import path
from .views import base,python,django

urlpatterns = [
    
    path('',base.as_view(),name='base'),
    path('python/',python,name='python'),
    path('django/',django,name='django')
]
