from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='home'),
    path('about-us/', views.AboutListView.as_view(), name='about'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('contact/', views.ContactListView.as_view(), name='contact'),
]



