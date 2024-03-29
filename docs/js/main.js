document.addEventListener('DOMContentLoaded', function() {
    fetch('data.json')
        .then(response => response.json())
        .then(data => {
            console.log("Raw data:", data); // Step 1: Log the raw data

            const ctx = document.getElementById('leetcodeChart').getContext('2d');
            const chartData = prepareChartData(data.date_count);
            
            console.log("Prepared chart data:", chartData); // Step 2: Log the prepared data

            new Chart(ctx, {
                type: 'bar',
                data: chartData,
                options: {
                    scales: {
                        x: {
                            type: 'time',
                            time: {
                                unit: 'day',
                                tooltipFormat: 'MMM d, yyyy',
                                parser: 'yyyyMMdd',
                                displayFormats: {
                                    day: 'MMM d'
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
        const formattedDate = date; // No need for conversion, Chart.js and the adapter handle it
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
