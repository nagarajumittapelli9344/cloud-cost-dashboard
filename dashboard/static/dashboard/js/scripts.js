// Custom JavaScript for Cloud Cost Dashboard

// Function to format currency
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

// Function to format percentage
function formatPercentage(value) {
    return value.toFixed(2) + '%';
}

// Function to update metric cards dynamically (if needed)
function updateMetricCards() {
    // This could be used for real-time updates
    fetch('/dashboard/api/summary/')
        .then(response => response.json())
        .then(data => {
            document.querySelector('.card-title:contains("Total Cost") + .card-text').textContent = formatCurrency(data.total_cost);
            document.querySelector('.card-title:contains("Instance Count") + .card-text').textContent = data.instance_count;
        })
        .catch(error => console.error('Error updating metric cards:', error));
}

// Initialize tooltips if Bootstrap tooltips are used
document.addEventListener('DOMContentLoaded', function() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-refresh data every 5 minutes (optional)
    // setInterval(updateMetricCards, 300000);
});

// Function to handle responsive sidebar toggle (for mobile)
function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('d-none');
}

// Add event listener for sidebar toggle button if exists
document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.querySelector('.sidebar-toggle');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', toggleSidebar);
    }
});
