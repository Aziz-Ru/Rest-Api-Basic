from django.urls import path
from api.views import *

urlpatterns = [
    path('api/', api_home,name='api/'),
    path('products/<pk>/',Product_Detail_View),
    path('create/',Product_Create_View),
    path('products/<pk>/update/',Product_Update_View),
    path("products/<pk>/delete/", Product_Destroy_View),
    path('createlist/',Product_Create_List_View),
]
