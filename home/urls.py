from django.urls import path
from home import views
urlpatterns = [
    path('', views.index,name='index'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('category_product/<int:id>/<slug:slug>',views.category_product, name='category_product'),
    path('contactus/',views.contactus, name='contactus'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('chefbio/<int:id>', views.chefbio, name='chefbio'),
]