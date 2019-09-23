from django.urls import path
from House_rent_prediction import views

app_name = 'House_rent_prediction'
urlpatterns = [
    path('House_rent_prediction/',views.index, name = 'index'),
    path('house_style/',views.house_style, name = 'house_style'),
    path('Neighbor_hood/',views.Neighbor_hood, name = 'Neighbor_hood'),
    path('foundation/',views.foundation_data, name = 'foundation'),
    path('garage_type/',views.GarageType_data, name = 'garage_type'),
    path('pridiction/',views.pridiction, name = 'pridiction'),
]
