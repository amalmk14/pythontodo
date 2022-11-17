
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbhome/',views.TasklistView.as_view(),name='TasklistView'),
    path('cbdetail/<int:pk>/',views.TaskdetailView.as_view(),name='TaskdetailView'),
    path('cbupdate/<int:pk>/',views.TaskupdateView.as_view(),name='TaskupdateView'),
    path('cbdelete/<int:pk>/',views.TaskdeleteView.as_view(),name='TaskdeleteView'),

]