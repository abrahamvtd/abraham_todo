from django.urls import path
from .import views

urlpatterns = [
    path('',views.taskview,name='taskview'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('covtask/',views.tasklistview.as_view(),name='covtask'),
    path('covdetail/<int:pk>/',views.covdetail.as_view(),name='covdetail'),
    path('covupdate/<int:pk>/',views.taskupdateview.as_view(),name='covupdate'),
path('covdelete/<int:pk>/',views.taskdeleteview.as_view(),name='covdelete'),
]
