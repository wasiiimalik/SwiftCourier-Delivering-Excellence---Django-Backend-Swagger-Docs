from django.urls import include, path
from .authentication import urlpatterns as authentication_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
  
    path('api/', include(authentication_urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

   
]
