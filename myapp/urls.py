from django.urls import path
from . import views
urlpatterns = [
    path("",views.hello),
    # path('goodbye/', views.goodbye),
    # path('maktab/', views.maktab)
]