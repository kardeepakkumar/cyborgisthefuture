document.addEventListener('DOMContentLoaded', function() {
    fetch('data.json')
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('leetcodeChart').getContext('2d');
            const chartData = prepareChartData(data.date_count);
            new Chart(ctx, {
                type: 'bar',
                data: chartData,
                options: {
                    scales: {
                        x: {
                            type: 'time',
                            time: {
                                parser: 'YYYYMMDD',
                                unit: 'day',
                                tooltipFormat: 'MMM D, YYYY',
                                displayFormats: {
                                    day: 'MMM D'
                                }
                            },
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Problems Solved'
                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: true
                        }
                    }
                }
            });
        }).catch(error => console.error("Error loading data:", error));
});

function prepareChartData(dateCount) {
    const labels = [];
    const easy = { label: 'Easy', data: [], backgroundColor: 'rgb(75, 192, 192)' };
    const medium = { label: 'Medium', data: [], backgroundColor: 'rgb(255, 205, 86)' };
    const hard = { label: 'Hard', data: [], backgroundColor: 'rgb(255, 99, 132)' };

    for (const [date, counts] of Object.entries(dateCount)) {
        const formattedDate = moment(date, "YYYYMMDD").toDate();
        labels.push(formattedDate);
        easy.data.push(counts.easy);
        medium.data.push(counts.medium);
        hard.data.push(counts.hard);
    }

    return {
        labels: labels,
        datasets: [easy, medium, hard]
    };
}
