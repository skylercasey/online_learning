from django.urls import path 
from . import views 

urlpatterns=[
		path('mine/',views.ManagerCourseListView.as_view(),name='Manage_Course_List'),
		path('create/',views.CourseCreateView.as_view(),name='course_create'),
		path('<pk>/edit/',views.CourseUpdateView.as_view(),name='course_edit'),
		path('<pk>/edit/',views.CourseDeleteView.as_view(),name='course_delete'),
]