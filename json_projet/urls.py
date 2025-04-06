
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('json_app.urls')),
    path('import/', include('import_excel.urls')),

]
