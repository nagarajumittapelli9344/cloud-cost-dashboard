# Cloud Cost and Performance Monitoring Dashboard

A comprehensive web-based dashboard for monitoring cloud infrastructure costs and performance metrics in real-time.

## 🌟 Features

- **Dashboard Summary**: Real-time overview of total cloud costs and instance count
- **Instance Management**: Detailed table view of all cloud instances with search functionality
- **Cost Breakdown**: Visual representation of costs by service type (EC2, RDS, Lambda, S3)
  - Pie chart for percentage distribution
  - Bar chart for absolute cost values
- **Performance Metrics**: Monitor CPU and Memory utilization trends over time
- **Cost Trends**: Track daily cost variations to identify spending patterns
- **Responsive Design**: Dark-themed professional UI that works on all devices
- **Fast Navigation**: Seamless page transitions with sidebar navigation

## 📊 Dashboard Pages

| Page | Purpose |
|------|----------|
| **Summary** | Quick metrics showing total cost ($3084) and instance count (5) |
| **Instances** | Complete instance inventory with details (ID, Service, Environment, Cost, CPU, Memory) |
| **Cost Breakdown** | Visual analysis of spending by AWS service type |
| **Performance** | CPU and Memory utilization tracking over time |
| **Cost Trends** | Daily cost analysis for budget forecasting |

## 🛠️ Tech Stack

**Backend:**
- Django (Python web framework)
- Django REST Framework
- Python 3.8+

**Frontend:**
- HTML5
- CSS3  
- JavaScript
- Chart.js (for data visualization)
- Bootstrap/Custom CSS

**Database:**
- SQLite (for development)
- PostgreSQL (recommended for production)

## 📄 Project Structure

```
cloud_dashboard/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
├── cloud_dashboard/
├── dashboard/
├── templates/
└── static/
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Steps

1. Clone the repository
2. Create virtual environment
3. Install dependencies
4. Apply migrations
5. Run development server
6. Access at `http://127.0.0.1:8000/dashboard/summary/`

## 📋 Key Features

### Real-time Metrics
- Total cloud spend: $3,084.00
- Active instances: 5
- CPU utilization tracking
- Memory usage monitoring

### Data Visualization
- Pie charts for cost distribution
- Line charts for trend analysis
- Bar charts for service comparison
- Interactive legends

## 🚀 Deployment

Deploy to Heroku, AWS Elastic Beanstalk, Railway, or Render with your preferred platform.

## 📝 License

MIT License - Free to use and modify

---

**Status**: Production Ready ✅
**Last Updated**: December 2025
**Version**: 1.0.0
