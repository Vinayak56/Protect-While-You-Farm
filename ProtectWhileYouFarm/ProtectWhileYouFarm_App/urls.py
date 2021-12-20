from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('home/',views.home, name='home'),
    path('addImage/',views.addImage, name='addImage'),
    path('home/addImage',views.addImage, name='home'),
    path('addImage/predictDisease', views.predictDisease,name="predictDisease"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)