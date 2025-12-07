from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from .analytics import load_cost_data, load_metric_data
import pandas as pd

def summary_view(request):
    cost_df = load_cost_data()
    metric_df = load_metric_data()

    total_cost = cost_df['cost_usd'].sum()
    instance_count = cost_df['instance_id'].nunique()

    context = {
        'total_cost': float(total_cost),
        'instance_count': int(instance_count)
    }
    return render(request, 'dashboard/summary.html', context)

def instances_view(request):
    cost_df = load_cost_data()
    metric_df = load_metric_data()

    # Get unique instances with latest data
    instances = cost_df.groupby('instance_id').agg({
        'instance_id': 'first',
        'service': 'first',
        'environment': 'first',
        'team': 'first',
        'region': 'first',
        'cost_usd': 'sum'
    }).reset_index(drop=True)

    # Add state (mock as running for simplicity)
    instances['state'] = 'running'

    # Add latest metrics
    latest_metrics = metric_df.groupby('instance_id').last().reset_index()
    instances = instances.merge(latest_metrics[['instance_id', 'cpu_util', 'memory_util']], on='instance_id', how='left')

    # Pagination
    paginator = Paginator(instances.to_dict('records'), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'instances': page_obj
    }
    return render(request, 'dashboard/instances.html', context)

def cost_breakdown_view(request):
    cost_df = load_cost_data()

    # Group by service
    cost_by_service = cost_df.groupby('service')['cost_usd'].sum().reset_index()

    context = {
        'cost_by_service': cost_by_service.to_dict('records')
    }
    return render(request, 'dashboard/cost_breakdown.html', context)

def performance_view(request):
    metric_df = load_metric_data()

    # Aggregate metrics over time
    performance_data = metric_df.groupby('timestamp').agg({
        'cpu_util': 'mean',
        'memory_util': 'mean'
    }).reset_index()

    context = {
        'performance_data': performance_data.to_dict('records')
    }
    return render(request, 'dashboard/performance.html', context)

def cost_trends_view(request):
    cost_df = load_cost_data()

    # Group by date
    cost_trends = cost_df.groupby('date')['cost_usd'].sum().reset_index()

    context = {
        'cost_trends': cost_trends.to_dict('records')
    }
    return render(request, 'dashboard/cost_trends.html', context)

# API Views for JSON data
def summary_api(request):
    cost_df = load_cost_data()
    total_cost = cost_df['cost_usd'].sum()
    instance_count = cost_df['instance_id'].nunique()
    return JsonResponse({
        'total_cost': float(total_cost),
        'instance_count': int(instance_count)
    })

def instances_api(request):
    cost_df = load_cost_data()
    metric_df = load_metric_data()

    instances = cost_df.groupby('instance_id').agg({
        'instance_id': 'first',
        'service': 'first',
        'environment': 'first',
        'team': 'first',
        'region': 'first',
        'cost_usd': 'sum'
    }).reset_index(drop=True)

    instances['state'] = 'running'

    latest_metrics = metric_df.groupby('instance_id').last().reset_index()
    instances = instances.merge(latest_metrics[['instance_id', 'cpu_util', 'memory_util']], on='instance_id', how='left')

    return JsonResponse({'instances': instances.to_dict('records')})

def cost_breakdown_api(request):
    cost_df = load_cost_data()
    cost_by_service = cost_df.groupby('service')['cost_usd'].sum().reset_index()
    return JsonResponse({'cost_by_service': cost_by_service.to_dict('records')})

def performance_api(request):
    metric_df = load_metric_data()
    performance_data = metric_df.groupby('timestamp').agg({
        'cpu_util': 'mean',
        'memory_util': 'mean'
    }).reset_index()
    return JsonResponse({'performance_data': performance_data.to_dict('records')})

def cost_trends_api(request):
    cost_df = load_cost_data()
    cost_trends = cost_df.groupby('date')['cost_usd'].sum().reset_index()
    return JsonResponse({'cost_trends': cost_trends.to_dict('records')})
