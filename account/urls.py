from django.urls import path
from .views import *
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns=[
    path('reg',RegView.as_view(),name="reg"),
    path('home',HomeView.as_view(),name="home"),
    path('lout',LogoutView.as_view(),name="lout")
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)