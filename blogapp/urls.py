from django.urls import path

from blogapp.views import BlogView, blogcreate, blogdelete ,blogupdate
app_name = 'blogapp'
urlpatterns = [
    path('liste',BlogView.as_view(), name="listhtml"),
    path('create',blogcreate.as_view(), name="createhtml"),
    path('delete/<int:pk>/',blogdelete.as_view(), name="deletehtml"),
    path('update/<int:pk>/',blogupdate.as_view(), name="updatehtml"),



]