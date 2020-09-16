from django import forms
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Music


def home(request):
    if request.user.is_anonymous:
        return render(request, 'library/home.html')
    context = {
        'songs': Music.objects.filter(userId=request.user).order_by('-dateCreated'),
        'username': request.user
    }
    return render(request, 'library/home.html', context)

def titleCount(request):
    context = {
        'titles': Music.objects.values('songTitle','Artist').annotate(userCount=Count('userId')).order_by('songTitle'),
        'artists': Music.objects.values('Artist').annotate(userCount=Count('userId')).order_by('Artist')
    }
    return render(request, 'library/admin.html', context)


class MusicListView(ListView):
    model = Music
    template_name = 'library/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'songs'
    ordering = ['-dateCreated']


class MusicDetailView(LoginRequiredMixin, DetailView):
    model = Music
    #fields = ['orderSource','houseAccount', 'name', 'address', 'mobile', 'deliverydriver', 'deliverytime', 'specialInstruction', 'cateringAmount', 'deliveryFee', 'tips', 'salesTax', 'customerFeedBack', 'onTime', 'deliveryStatus', 'customerPaymentStatus', 'employeePaymentStatus', 'cateringDate', 'commissionAmount', 'commissionStatus', 'estimatedDelivery']


class MusicCreateView(LoginRequiredMixin, CreateView):
    model = Music
    fields = ['songTitle','Artist','dateCreated']

    def form_valid(self, form):
        form.instance.userId = self.request.user
        return super().form_valid(form)


class MusicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Music
    fields = ['songTitle','Artist','dateCreated']
    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        
        return True


class MusicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Music
    success_url = '/'

    def test_func(self):
        return True


def about(request):
    return render(request, 'library/about.html', {'title': 'About'})
