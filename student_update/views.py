from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from . import models
from . import mforms
from django.contrib import messages 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

class home(ListView):
    model = models.St_img
    context_object_name = 'img'
    template_name = "home.html"

class studentList(ListView):
    model = models.St_img
    template_name = 'st_list.html'
    context_object_name = 'student'

class add_student(CreateView):
    form_class = mforms.st_gelary
    template_name = "st_create_update.html"
    success_url = reverse_lazy('studentList')
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        messages.success(self.request, "Student add successfully.")
        return super().form_valid(form)
    
class update_student(UpdateView):
    model = models.St_img
    form_class = mforms.st_gelary
    template_name = "st_create_update.html"
    context_object_name = 'student'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('studentList')
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        messages.success(self.request, "Student Updatede successfully.")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context
    
class delete_student(DeleteView):
    model = models.St_img
    pk_url_kwarg = 'id'
    template_name = "delete.html"
    success_url = reverse_lazy('studentList')

    def delete(self, request, *args, **kwargs):
        messages.WARNING(self.request, "Student Delete successful.")
        return super().delete(request, *args, **kwargs)
