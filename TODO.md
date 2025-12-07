# TODO List for Cloud Cost Dashboard Project

## Backend (Django)
- [x] Update `dashboard/views.py` to add views for instances, cost_breakdown, performance, cost_trends
- [x] Add API views in `dashboard/views.py` for JSON data (summary_api, instances_api, etc.)
- [x] Update `dashboard/urls.py` to include all page URLs and API endpoints
- [x] Ensure pagination for instances list in views

## Frontend (HTML/CSS/JS)
- [x] Create base template `dashboard/templates/dashboard/base.html` with header, sidebar navigation, and main content area
- [x] Update `dashboard/templates/dashboard/summary.html` with metric cards, professional styling
- [x] Create `dashboard/templates/dashboard/instances.html` with table, search/filter functionality
- [x] Create `dashboard/templates/dashboard/cost_breakdown.html` with pie/bar charts using Chart.js
- [x] Create `dashboard/templates/dashboard/performance.html` with line charts for CPU/memory trends
- [x] Create `dashboard/templates/dashboard/cost_trends.html` with line chart for cost trends
- [x] Add static files: `dashboard/static/dashboard/css/style.css` (Bootstrap + custom), `dashboard/static/dashboard/js/scripts.js` (Chart.js integration)
- [x] Ensure responsive design, dark theme, icons, color-coded metrics

## Data and Testing
- [x] Verify mock data in CSVs is sufficient; expand if needed
- [x] Update `dashboard/tests.py` with tests for new views
- [x] Run `python manage.py runserver` and verify all pages work
- [x] Run `python manage.py test` to verify tests pass
- [x] Test responsiveness on mobile/desktop
