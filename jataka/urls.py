from django.urls import path
from jataka import views

app_name = 'jataka'

urlpatterns = [
    path('jataka_home/',views.jataka_home,name='jataka_home'),
]
