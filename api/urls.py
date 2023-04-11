
from api.views import instrutorViewSet, planosViewSet
# from django.urls import path
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('', list_instructors.as_view()),
#     path('instrutores/', list_instructors,
#          name='instrutor-list-create'),
#     path('instrutores/<slug:slug_name>/',
#          delete_and_update_instrutors.as_view(),
#          name='instrutor-retrieve-update'),
#     path('', list_planos),
#     path('planos/', list_planos.as_view(), name='plano-list-create'),
#     path('planos/<str:id>/', delete_and_update_planos.as_view(),
#          name='plano-retrieve-update')
# ]

router = DefaultRouter()
router.register('instrutores', instrutorViewSet)
router.register('planos', planosViewSet)
urlpatterns = router.urls
