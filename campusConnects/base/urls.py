from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import DetailView
from . import views

app_name = 'base'
urlpatterns = [

    path('registration/',views.registration,name="registration"),
    path('userRegistration/',views.UserRegistration,name="userRegistration"),
    path('login/',views.loginPage,name="login"),
    path('seemore/<int:pk>/',DetailView.as_view(), name='seemore'),
    # path('seemore/<int:pk>/increment_views/',views.incrementViews(),name='incrementViews'),
    path('profile/', views.profile, name='profile'),

]

# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
