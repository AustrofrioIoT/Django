from django.urls import path
from app import views as app_views
from portfolio import views as portfolio_views

from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('',app_views.home,name='home'),
    path('about-me/',app_views.about,name='about'),
    path('contact/',app_views.contact,name='contact'),
    path('portfolio/',portfolio_views.portfolio,name='portfolio'),
    path('admin/',admin.site.urls),

]


##modo debug
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
