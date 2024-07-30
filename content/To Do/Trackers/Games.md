# <mark style="background: #D2B3FFA6;">Games</mark>

Looks for **Games**

```dataviewjs
dv.span("")
const calendarData = {
    year: 2024,  // (optional) defaults to current year
    entries: [],
    intensityScaleStart: 60,
    intensityScaleEnd: 0
}

//DataviewJS loop
for (let page of dv.pages('"Daily Notes"').where(p => p.Games)) {
    //dv.span("<br>" + page.file.name + " " + page.Games) // uncomment for troubleshooting
    if (page.Games <= 60) {
	    calendarData.entries.push({
	        date: page.file.name,     // (required) Format YYYY-MM-DD
	        intensity: page.Games, // (required) the data you want to track, will map color intensities automatically
	        content: await dv.span(`[[${page.file.name}|]]`),           // (optional) Add text to the date cell
	        color: "purple"
	    })
    }
}

renderHeatmapCalendar(this.container, calendarData)
```

