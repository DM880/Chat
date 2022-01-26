from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


from .views import views


urlpatterns = [
    path("sign/", views.sign, name="sign"),
    path("signin/" views.sign_in, name="sign_in"),
    path("signup/" views.sign_up, name="sign_up"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
