```dataviewjs
const pages = dv.pages('#daily-note');

// Extract focus, game, and creative times along with their dates
const focusTimes = pages.map(p => ({ date: p.file.day, time: p.focus_time })).filter(d => typeof d.time === 'number' && d.time > 0);
const gameTimes = pages.map(p => ({ date: p.file.day, time: p.game_time })).filter(d => typeof d.time === 'number' && d.time > 0);
const creativeTimes = pages.map(p => ({ date: p.file.day, time: p.creative_time })).filter(d => typeof d.time === 'number' && d.time > 0);

// If no valid times are found for either, handle gracefully
if (focusTimes.length === 0 && gameTimes.length === 0 && creativeTimes.length === 0) {
    dv.paragraph("No valid focus, game, or creative times found.");
} else {
    // Extract unique dates and sort them
    const dates = [...new Set([...focusTimes, ...gameTimes, ...creativeTimes].map(d => d.date))]
        .sort((a, b) => new Date(a) - new Date(b));

    // Initialize arrays to hold daily times (fill with 0 initially)
    const dailyFocusTimes = dates.map(date => {
    const entry = focusTimes.find(d => d.date === date);
	    return entry && entry.time > 0 ? entry.time : null; // Replace 0 with null
	});
	
	const dailyGameTimes = dates.map(date => {
	    const entry = gameTimes.find(d => d.date === date);
	    return entry && entry.time > 0 ? entry.time : null; // Replace 0 with null
	});
	
	const dailyCreativeTimes = dates.map(date => {
	    const entry = creativeTimes.find(d => d.date === date);
	    return entry && entry.time > 0 ? entry.time : null; // Replace 0 with null
	});

    // Set up the chart data with daily times
    const chartData = {
        type: 'line',
        data: {
            labels: dates.map(date => date.toString()),  // Convert dates to strings for labels
            datasets: [
                {
                    label: 'Focus Time (minutes)',
                    data: dailyFocusTimes,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                    fill: false,
                },
                {
                    label: 'Game Time (minutes)',
                    data: dailyGameTimes,
                    backgroundColor: 'rgba(78, 177, 188, 0.2)',
                    borderColor: 'rgba(56, 128, 137, 1)',
                    borderWidth: 1,
                    fill: false,
                },
                {
                    label: 'Creative Time (minutes)',
                    data: dailyCreativeTimes,
                    backgroundColor: 'rgba(0, 159, 80, 0.2)',
                    borderColor: 'rgba(0, 159, 80, 1)',
                    borderWidth: 1,
                    fill: false,
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Time (minutes)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Date'
                    },
                    type: 'time',
                    time: {
                        unit: 'day'
                    }
                }
            },
            plugins: {
                annotation: {
                    annotations: {
                        gameGoal: {
                            type: 'line',
                            yMin: 120,
                            yMax: 120,
                            borderColor: 'rgba(93, 213, 226, 0.4)',
                            borderWidth: 2,
                            borderDash: [5, 5],
                            label: {
                                enabled: true,
                                content: '120 Minutes',
                                position: 'end',
                                backgroundColor: 'rgba(0, 0, 0, 0.7)',
                                color: 'white',
                                font: {
                                    size: 10
                                }
                            }
                        },
                        focusGoal: {
                            type: 'line',
                            yMin: 180,
                            yMax: 180,
                            borderColor: 'rgba(241, 68, 105, 0.4)',
                            borderWidth: 2,
                            borderDash: [5, 5],
                            label: {
                                enabled: true,
                                content: '90 Minutes',
                                position: 'end',
                                backgroundColor: 'rgba(0, 0, 0, 0.7)',
                                color: 'white',
                                font: {
                                    size: 10
                                }
                            }
                        }
                    }
                }
            }
        }
    };

    // Render the line chart
    window.renderChart(chartData, this.container);
}

```

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

![[Organisation/Habits#<mark style="background ABF7F7A6;">Main Focus</mark>]]