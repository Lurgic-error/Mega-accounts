from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View, DeleteView, DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail


class Home(View):

    def get(self, request, *args, **kwargs):

        template = 'pages/home.html'
        context = {}

        return render(request, template, context)