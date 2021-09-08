from django.urls import path
import appli.views
from . import views

urlpatterns = [
    path('', appli.views.vue_index, name='index'),
    path('index', appli.views.vue_index, name='index'),
]