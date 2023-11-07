from django.urls import path

from mainsite import views


urlpatterns = [
    path('api/v1/objects/', views.ObjectList.as_view()),
    path('api/v1/objects/<int:pk>/', views.ObjectDetail.as_view()),
    path('api/v1/contracts/', views.ContractList.as_view()),
    path('api/v1/contracts/<int:pk>/', views.ContractDetail.as_view()),
    path('api/v1/nodes/', views.NodeList.as_view()),
    path('api/v1/nodes/<int:pk>/', views.NodeDetail.as_view()),
]
