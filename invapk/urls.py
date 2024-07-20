from django.urls import path
from . import views

urlpatterns = [
    path('', views.showalldata, name='showalldata'),
    path('catrgory', views.catrgoryview, name='category'),
    path('brand', views.brandview, name='brand'),
    path('Order', views.Ordered, name='Order'),
    path('product', views.products, name='product'),
    path('purchese', views.purchesed, name='purchese'),
    path('supplier', views.suppliers, name='supplier'),
    path('delc/<int:pk>/',views.deletecustomer,name='delc'),
    path('c_entry/', views.c_entry, name='c_entry'),
    path('delv/<int:pk>/',views.deletecategory,name='delv'),
    path('delb/<int:pk>/',views.deletebrand,name='delb'),
    path('dels/<int:pk>/',views.deletesupplier,name='dels'),
    path('edit/', views.edit_i_customer, name='edit'),
    path('update/<int:id>/', views.update_i_customer, name='update'),
    path('editc/', views.edit_i_category, name='editc'),
    path('updatec/<int:id>/', views.update_i_category, name='updatec'),
    path('editb/', views.edit_i_brand, name='editb'),
    path('updateb/<int:id>/', views.update_i_brand, name='updateb'),
    path('edits/', views.edit_i_sup, name='edits'),
    path('updates/<int:id>/', views.update_i_sup, name='updates'),
    path('deleteproduct/<int:pk>/', views.deleteproduct, name='delp'),
    path('updatep/<int:id>/', views.update_i_sup, name='updatep'),
    path('editp/', views.edit_i_sup, name='editp'),
    path('delpu/<int:pk>/', views.deletepurchese, name='delpu'),
    path('updatepp/<int:id>/', views.update_i_pur, name='updatepp'),
    path('editpp/', views.edit_i_pur, name='editpp'),
    path('delo/<int:pk>/', views.deleteorder, name='delo'),
    path('updateo/<int:id>/', views.update_i_ore, name='updateo'),
    path('edito/', views.edit_i_ore, name='edito'),




]
