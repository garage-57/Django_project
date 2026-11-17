from django.urls import path
from . import views
from .views import home_item

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts_answer', views.contacts_answer, name='contacts_answer'),
    path('item/<int:item_id>/', views.home_item, name='home_item')
]
