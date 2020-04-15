# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from map_neigh.models import Buildings, CustomUserModel, Announcement
from django.shortcuts import render_to_response, render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import json, ast
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import NewUserForm, NewAnnouncementForm

# Create your views here.
def index(request):
    buildings_objects = Buildings.objects.all()
    return render(request=request,
                    template_name='map_neigh/map.html',
                    context={"buildings":buildings_objects})

# returns shapefile converted into geojson
def get_geojson(request):
    buildings = Buildings.objects.all()
    buildings_geojson = serialize('geojson', buildings)

    return HttpResponse(buildings_geojson)

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Zarejestrowano uzytkownika: ' + str(username))
            login(request, user)
            return redirect("map_neigh:index")

        else:
            for msg in form.error_messages:
                messages.error(request, str(msg) + ": " + str(form.error_messages[msg]))

            return render(request = request,
                          template_name = "map_neigh/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "map_neigh/register.html",
                  context={"form":form})
def logout_request(request):
    logout(request)
    messages.info(request, "Pomyślnie wylogowano")
    return redirect("map_neigh:index")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Zalogowano użytkownika " + str(username))
                return redirect('/')
            else:
                messages.error(request, "Nieprawidłowa nazwa użytkownika lub hasło.")
        else:
            messages.error(request, "Nieprawidłowa nazwa użytkownika lub hasło.")

    form = AuthenticationForm()
    return render(request=request,
                    template_name="map_neigh/login.html",
                    context={"form":form})

def add_announcement(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            username = str(request.user.get_username())
            user_name = CustomUserModel.objects.get(username=username)
            user_address = CustomUserModel.objects.values_list('address', flat=True).get(username=username)
            user_object = Buildings.objects.get(id=user_address)
            form = NewAnnouncementForm(request.POST)
            if form.is_valid():
                announcement = form.save(commit=False)
                announcement.user_name = user_name
                announcement.building_id = user_object
                announcement = form.save(commit=True)
                messages.success(request, 'Dodano ogłoszenie')
                return redirect("map_neigh:index")
            else:
                for field in form.errors:
                    for item in form.errors:
                        messages.error(request, '{}: {}'.format(field,item))

                return render(request = request,
                              template_name = "map_neigh/add.html",
                              context={"form":form})

        form = NewAnnouncementForm
        return render(request = request,
                      template_name = "map_neigh/add.html",
                      context={"form":form})

def get_json(request):
    announcements = Announcement.objects.all()
    ann_json = serialize('json', announcements)

    return HttpResponse(ann_json)

def profile(request):
    if not request.user.is_authenticated:
        return redirect("map_neigh:login")
    person = CustomUserModel.objects.get(username=request.user)
    return render(request, 'map_neigh/profile.html', {'person':person})
