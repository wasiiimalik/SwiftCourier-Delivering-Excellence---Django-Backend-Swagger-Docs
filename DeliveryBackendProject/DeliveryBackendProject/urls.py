"""
URL configuration for DeliveryBackendProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import OrderViewSet, CustomerViewSet, DriverViewSet, DeliveryStatusViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions



router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'delivery-statuses', DeliveryStatusViewSet)

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Delivery Company API",
#         default_version='v1',
#     ),
#     public=True,
# )

schema_view = get_schema_view(
    openapi.Info(
        title='Delivery App',
        default_version='v1',
        description='Api Testing Though Swagger ',
        terms_of_service='https://www.abcdelivery.com/terms/',
        contact=openapi.Contact(email='wasimmajidmalik@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    #permission_classes=(permissions.IsAuthenticated,),
    #permission_classes=(permissions.AllowAny,)  # Apply IsAuthenticated permission

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),


]
