from django.contrib import admin
from django.urls import include, path # includeを追加


urlpatterns = [
    path("kanban/", include("kanban.urls")),
    path('kanban/', include('django.contrib.auth.urls')), # この行を追加
    path('admin/', admin.site.urls),
]