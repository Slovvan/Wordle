from django.urls import include, path
from .views import home, WordViewSet, daily_word, create_word, update_word, delete_word
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'words', WordViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/daily/', daily_word ),
    path('api/create/', create_word),
    path('api/words/<int:pk>/', update_word ),
    path('api/words/<int:pk>/delete/', delete_word),
    path('', home),
]