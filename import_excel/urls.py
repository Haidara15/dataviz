from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/import-excel/', views.importer_graphique, name='importer_graphique_excel'),
    path('api/preview-graph/', views.preview_graph_api, name='preview_graph_api'),
]
