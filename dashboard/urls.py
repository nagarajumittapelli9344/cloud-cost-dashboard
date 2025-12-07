from django.urls import path
from . import views

urlpatterns = [
    path('summary/', views.summary_view, name='summary'),
    path('instances/', views.instances_view, name='instances'),
    path('cost-breakdown/', views.cost_breakdown_view, name='cost_breakdown'),
    path('performance/', views.performance_view, name='performance'),
    path('cost-trends/', views.cost_trends_view, name='cost_trends'),
    # API endpoints
    path('api/summary/', views.summary_api, name='summary_api'),
    path('api/instances/', views.instances_api, name='instances_api'),
    path('api/cost-breakdown/', views.cost_breakdown_api, name='cost_breakdown_api'),
    path('api/performance/', views.performance_api, name='performance_api'),
    path('api/cost-trends/', views.cost_trends_api, name='cost_trends_api'),
]
