from django.urls import path,include
from django.views.generic import TemplateView
from .views import cadastros_compra, delete_view_c_m, delete_view_v_m,delete_view_c,delete_view_v,edit_view_c,edit_view_v,edit_view_c_m,edit_view_v_m

urlpatterns = [
  path('accounts/', include('django.contrib.auth.urls')),
  path('' , TemplateView.as_view(template_name ='home.html'), name='home'),
  path("book/",(cadastros_compra), name="book"),
  path('<int:id>/deletev/', delete_view_v_m, name="deletev"),
  path('<int:id>/deletec/', delete_view_c_m, name="deletec"),
  path('<int:id>/delete_v/', delete_view_v, name="delete_v"),
  path('<int:id>/delete_c/', delete_view_c, name="delete_c"),
  path('<int:id>/edit_c/', edit_view_c, name="edit_c"),
  path('<int:id>/edit_v/', edit_view_v, name="edit_v"),
  path('<int:id>/edit_c_m/', edit_view_c_m, name="edit_c_m"),
  path('<int:id>/edit_v_m/', edit_view_v_m, name="edit_v_m") 
 
]

