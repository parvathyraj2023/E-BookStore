from django.urls import path
from newapp import views
urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addcategorypage/',views.addcategorypage,name="addcategorypage"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('addbookpage/',views.addbookpage,name="addbookpage"),
    path('savebook/',views.savebook,name="savebook"),
    path('displaybook/',views.displaybook,name="displaybook"),
    path('editbook/<int:reader_id>/',views.editbook,name="editbook"),
    path('deletebook/<int:dataid>/',views.deletebook,name="deletebook"),
    path('updatebook/<int:reader_id>/',views.updatebook,name="updatebook"),
    path('adminloginpage/',views.adminloginpage,name="adminloginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('displaycontactdetails/',views.displaycontactdetails,name="displaycontactdetails"),
    path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact"),
    path('editcontact/<int:dataid>/', views.editcontact, name="editcontact"),
    path('updatecontact/<int:dataid>/', views.updatecontact, name="updatecontact")
]