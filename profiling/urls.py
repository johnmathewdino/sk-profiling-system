from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
from .forms import UserLoginForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login_page/index.html', authentication_form = UserLoginForm, redirect_authenticated_user = True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('',views.dashboard, name="dashboard"),
    path('profiles/', views.profile, name="profiles"),
    path('profiles/<slug:slug>/', views.profile_page, name="profile_page"),
    path('profiles/<slug:slug>/edit/', views.profile_page_edit, name="profile_page_edit"),
    path('add_profile/', views.add_profile, name="add_profile"),
    path('filter_level/', views.profile_filter_level, name="profile_filter_level_page"),
    path('filter_year/', views.profile_filter_year, name="profile_filter_year_page"),
    path('generate_document/', views.generate_document, name="generate_document"),
    path('get_document/<slug:grade>/<slug:header>/', views.getPdfPage, name="get_document"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
handler404 = "profiling.views.page_not_found_view"
