from django.urls import path
from .views.director_views import DirectorsView, DirectorDetailView
from .views.film_views import FilmsView, FilmDetailView
from .views.user_views import SignUpView, SignInView, SignOutView, ChangePasswordView

urlpatterns = [
  	# Restful routing
    path('directors/', DirectorsView.as_view(), name='directors'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director_detail'),
    path('films/', FilmsView.as_view(), name='films'),
    path('films/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('change-pw/', ChangePasswordView.as_view(), name='change-pw')
]
