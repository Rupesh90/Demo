from django.urls import path
from pages import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('hello/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact',views.contact,name='contact')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)