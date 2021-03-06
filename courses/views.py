from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Course 
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


# Create your views here.
class ManagerCourseListView(ListView):
	model=Course
	template_name='courses/manage/course/list.html'

	def get_queryset(self):
		qs=super(ManagerCourseListView,self).get_queryset()
		return qs.filter(owner=self.request.user)

class OwnerMixin(object):
	def get_queryset(self):
		qs=super(OwnerMixin,self).get_queryset()
		return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
	def form_valid(self,form):
		form.instance.owner=self.request.user
		return super(OwnerEditMixin,self).form_valid(form)

class OwnerCourseMixin(LoginRequiredMixin):
	model=Course
	fields=['subject','title','slug','overview']
	success_url=reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerCourseMixin,OwnerEditMixin):
	fields=['subject','title','slug','overview']
	success_url=reverse_lazy('manage_course_list')
	template_name='courses/manage/course/list.html'

class CourseCreateView(PermissionRequiredMixin,OwnerCourseEditMixin,CreateView):
	template_name = 'courses/manage/course/form.html'
	permission_required='courses.add_course'

class CourseUpdateView(PermissionRequiredMixin,OwnerCourseEditMixin,UpdateView):
	permission_required='courses.add_course'

class CourseDeleteView(PermissionRequiredMixin,OwnerCourseMixin,DeleteView):
	template_name='courses/manage/course/delete.html'
	success_url=reverse_lazy('manage_course_list')
	permission_required='courses.delete_course'