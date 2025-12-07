from django.test import TestCase, Client
from django.urls import reverse
import pandas as pd
from .analytics import load_cost_data, load_metric_data

class DashboardViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_summary_view(self):
        response = self.client.get(reverse('summary'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Total Cost')
        self.assertContains(response, 'Instance Count')

    def test_instances_view(self):
        response = self.client.get(reverse('instances'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Instance List')

    def test_cost_breakdown_view(self):
        response = self.client.get(reverse('cost_breakdown'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cost Breakdown')

    def test_performance_view(self):
        response = self.client.get(reverse('performance'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Performance Metrics')

    def test_cost_trends_view(self):
        response = self.client.get(reverse('cost_trends'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cost Trends')

    def test_summary_api(self):
        response = self.client.get(reverse('summary_api'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('total_cost', data)
        self.assertIn('instance_count', data)

    def test_instances_api(self):
        response = self.client.get(reverse('instances_api'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('instances', data)

    def test_cost_breakdown_api(self):
        response = self.client.get(reverse('cost_breakdown_api'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('cost_by_service', data)

    def test_performance_api(self):
        response = self.client.get(reverse('performance_api'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('performance_data', data)

    def test_cost_trends_api(self):
        response = self.client.get(reverse('cost_trends_api'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('cost_trends', data)

class AnalyticsTestCase(TestCase):
    def test_load_cost_data(self):
        df = load_cost_data()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)

    def test_load_metric_data(self):
        df = load_metric_data()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
