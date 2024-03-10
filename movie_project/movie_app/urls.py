from django.urls import path
from . import views

app_name = 'movie_app'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/<int:id>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
    path('add_product/', views.add_product, name='add_product'),
    path('/edit_product/<int:id>/', views.edit_product, name='edit_product'),
    path('/delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('/product/<int:product_id>/add_comment/', views.add_comment, name='add_comment'),
    path('/product/<int:product_id>/add_rating/', views.add_rating, name='add_rating'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    
  
]