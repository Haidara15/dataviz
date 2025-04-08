from django.urls import path
from . import views

urlpatterns = [
    path('', views.theme_list, name='theme_list'),
    path('nouvelle/', views.create_theme, name='create_theme'),
    path('theme/<slug:theme_slug>/save-grid-layout/', views.save_grid_layout, name='save_grid_layout'),
    
]

# Sous-route pour les actions liées aux thèmes
urlpatterns += [
    path('theme/<slug:theme_slug>/edit/', views.edit_theme, name='edit_theme'),
    path('theme/<slug:theme_slug>/delete/', views.delete_theme, name='delete_theme'),
    path('theme/<slug:theme_slug>/charts/', views.theme_charts, name='theme_charts'),
]

# Sous-route pour les actions liées aux figures
urlpatterns += [
    path('theme/<slug:theme_slug>/chart/new/', views.create_chart_data, name='create_chart_data'),
    path('theme/<slug:theme_slug>/chart/<int:pk>/edit/', views.edit_chart_data, name='edit_chart_data'),
    path('theme/<slug:theme_slug>/chart/<int:pk>/delete/', views.delete_chart_data, name='delete_chart_data'),
]	


