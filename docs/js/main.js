document.addEventListener('DOMContentLoaded', function() {
    fetch('data.json')
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('leetcodeChart').getContext('2d');
            const chartData = prepareChartData(data.date_count);
            const chart = new Chart(ctx, {
                type: 'bar',
                data: chartData,
                options: {
                    scales: {
                        x: {
                            type: 'time',
                            time: {
                                unit: 'day',
                                tooltipFormat: 'MMM D, YYYY',
                                displayFormats: {
                                    day: 'MMM D'
                                }
                            }
                        },
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });
});

function prepareChartData(dateCount) {
    const labels = [];
    const easy = [];
    const medium = [];
    const hard = [];

    for (const [date, counts] of Object.entries(dateCount)) {
        const formattedDate = new Date(date.substring(0,4), date.substring(4,6) - 1, date.substring(6,8));
        labels.push(formattedDate);
        easy.push(counts.easy);
        medium.push(counts.medium);
        hard.push(counts.hard);
    }

    return {
        labels: labels,
        datasets: [
            {
                label: 'Easy',
                backgroundColor: 'rgb(75, 192, 192)',
                data: easy,
            },
            {
                label: 'Medium',
                backgroundColor: 'rgb(255, 205, 86)',
                data: medium,
            },
            {
                label: 'Hard',
                backgroundColor: 'rgb(255, 99, 132)',
                data: hard,
            }
        ]
    };
}
