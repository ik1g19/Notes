```dataviewjs
const pages = dv.pages('#daily-note');

// Extract and filter focus times and game times
const focusTimes = pages.map(p => p.focus_time).filter(t => typeof t === 'number' && t > 0).values;
const gameTimes = pages.map(p => p.game_time).filter(t => typeof t === 'number' && t > 0).values;
const creativeTimes = pages.map(p => p.creative_time).filter(t => typeof t === 'number' && t > 0).values;

// If no valid times are found for either, handle gracefully
if (focusTimes.length === 0 && gameTimes.length === 0 && creativeTimes.length == 0) {
    dv.paragraph("No valid focus or game times found.");
} else {
    // Set a common bin size
    const binSize = 60;
    
    // Determine the maximum time to set up the bins range
    const maxTime = Math.max(...focusTimes, ...gameTimes, ...creativeTimes);

    // Calculate the number of bins required
    const numberOfBins = Math.max(1, Math.ceil((maxTime + 1) / binSize));

    // Initialize bins for both focus times and game times
    const focusBins = new Array(numberOfBins).fill(0);
    const gameBins = new Array(numberOfBins).fill(0);
    const creativeBins = new Array(numberOfBins).fill(0);

    // Populate bins for focus times
    focusTimes.forEach(time => {
        const binIndex = Math.floor(time / binSize);
        focusBins[binIndex] += 1;
    });

    // Populate bins for game times
    gameTimes.forEach(time => {
        const binIndex = Math.floor(time / binSize);
        gameBins[binIndex] += 1;
    });
    
	// Populate bins for creative times
    creativeTimes.forEach(time => {
        const binIndex = Math.floor(time / binSize);
        creativeBins[binIndex] += 1;
    });

    // Create labels for the bins (e.g., "0-59", "60-119", etc.)
    const binLabels = focusBins.map((_, i) => `${i * binSize}-${(i + 1) * binSize - 1}`);

    // Set up the chart data with both datasets
    const chartData = {
        type: 'bar',
        data: {
            labels: binLabels,
            datasets: [
                {
                    label: 'Focus Time - Number of Days',
                    data: focusBins,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                },
                {
                    label: 'Game Time - Number of Days',
                    data: gameBins,
                    backgroundColor: 'rgba(78, 177, 188, 0.2)',
                    borderColor: 'rgba(56, 128, 137, 1)',
                    borderWidth: 1,
                },
                {
                    label: 'Creative Time - Number of Days',
                    data: creativeBins,
                    backgroundColor: 'rgba(0, 159, 80, 0.2)',
                    borderColor: 'rgba(0, 159, 80, 1)',
                    borderWidth: 1,
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Days'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Time Range (minutes)'
                    }
                }
            }
        }
    };

    // Render the combined chart
    window.renderChart(chartData, this.container);
}

```

