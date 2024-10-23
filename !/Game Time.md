```dataviewjs
const pages = dv.pages('#daily-note')
const testMarks = pages.map(p => p.game_time).filter(t => typeof t === 'number' && t > 0).values; // Ensure valid numeric focus times

// If no valid focus times, handle gracefully
if (testMarks.length === 0) {
    dv.paragraph("No valid focus times found.");
} else {
    // Create bins of focus times in increments of 60 minutes
    const binSize = 30;
    const maxFocusTime = Math.max(...testMarks);

    // Prevent invalid array lengths by ensuring at least 1 bin
    const numberOfBins = Math.max(1, Math.ceil((maxFocusTime+1) / binSize));

    // Initialize bins
    const bins = new Array(numberOfBins).fill(0);

    // Count the number of days that fall into each bin
    testMarks.forEach(time => {
        const binIndex = Math.floor(time / binSize);
        bins[binIndex] += 1;
    });

    // Create labels for the bins (e.g., "0-59", "60-119", etc.)
    const binLabels = bins.map((_, i) => `${i * binSize}-${(i + 1) * binSize - 1}`);

    // Set up the chart data
    const chartData = {
        type: 'bar',
        data: {
            labels: binLabels,
            datasets: [{
                label: 'Number of Days',
                data: bins,
                backgroundColor: 'rgba(78, 177, 188)',
                borderColor: 'rgba(56, 128, 137)',
                borderWidth: 1,
            }]
        }
    }

    window.renderChart(chartData, this.container);
}

```

