from django.urls import path

from . import views

app_name = 'questionnaire'

urlpatterns = [
    path('', views.Index.as_view(), name='index', ),
    path('new-game/', views.new_game, name='new-game', ),
]
