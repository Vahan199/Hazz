from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *


class IndexListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        indexbg = IndexBg.objects.all()
        indexabout = IndexAbout.objects.all()
        indexbest = IndexBest.objects.all()
        indexdream = IndexDream.objects.all()
        indexlot = IndexLot.objects.all()
        indexlot2 = IndexLot2.objects.all()
        indexlot3 = IndexLot3.objects.all()
        indexslayd = IndexSlayd.objects.all()
        indexdesigner = IndexDesigner.objects.all()
        indexblog = IndexBlog.objects.all()
        indextrend = IndexTrend.objects.all()
        logo = Logo.objects.all()
        instagram = Instagram.objects.all()


        return render(request, self.template_name, {'indexbg':indexbg, 'indexbest': indexbest, 'indexabout':indexabout,
        'indexdream':indexdream, 'indexlot': indexlot, 'indexlot2': indexlot2, 'indexlot3': indexlot3, 'indexslayd':indexslayd,
        'indexdesigner': indexdesigner, 'indexblog': indexblog, 'logo':logo,'indextrend':indextrend, 'instagram':instagram})



class AboutListView(ListView):
    template_name = 'about-us.html'



    def get(self, request):
        aboutbg = AboutBg.objects.all()
        aboutdesigner = AboutDesigner.objects.all()
        indextrend= IndexTrend.objects.all()
        logo = Logo.objects.all()
        instagram = Instagram.objects.all()
        return render(request, self.template_name, {'aboutbg': aboutbg, 'aboutdesigner' : aboutdesigner,
        'indextrend ': indextrend, 'logo':logo, 'instagram':instagram })


class BlogListView(ListView):
    template_name = 'blog.html'



    def get(self, request):
        blog1 = Blog1.objects.all()
        blog2 = Blog2.objects.all()
        logo = Logo.objects.all()
        instagram = Instagram.objects.all()


        return render(request, self.template_name, {'blog1':blog1, 'blog2':blog2, 'logo':logo, 'instagram':instagram})


class GalleryListView(ListView):
    template_name = 'gallery.html'



    def get(self, request):
        logo = Logo.objects.all()
        instagram = Instagram.objects.all()

        return render(request, self.template_name, {'logo':logo, 'instagram':instagram})



class ContactListView(ListView):
    template_name = 'contact.html'


    def get(self, request):
        logo = Logo.objects.all()
        instagram = Instagram.objects.all()
        return render(request, self.template_name, {'logo':logo, 'instagram':instagram})




