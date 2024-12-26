from rest_framework import routers
from llanquiPageProject.llanquiPageApp import views
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'multimediaFavorita', views.MultimediaFavoritaViewSet, 'multimedia')
router.register(r'recomendacionUsuario', views.RecomendacionUsuarioViewSet, 'recomendacion')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('index/', views.Index, name='index'),
    path('docs/', include_docs_urls(title='Llanqui Page API')),
]
