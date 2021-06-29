from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,DeleteView,DetailView,UpdateView,CreateView



class  AlerListViewPost(TemplateView):
    template_name='home.html'
    



