# <mark style="background: #BBFABBA6;">Productivity</mark>

```dataviewjs
dv.span("")
const calendarData = {
    year: 2024,  // (optional) defaults to current year
    entries: [],
    intensityScaleStart: 0,
    intensityScaleEnd: 240
}

//DataviewJS loop
for (let page of dv.pages('"Daily Notes"').where(p => p.Productivity)) {
    //dv.span("<br>" + page.file.name) // uncomment for troubleshooting
    calendarData.entries.push({
        date: page.file.name,     // (required) Format YYYY-MM-DD
        intensity: page.Productivity, // (required) the data you want to track, will map color intensities automatically
        content: await dv.span(`[[${page.file.name}|]]`),           // (optional) Add text to the date cell
        color: "default"
    })
}

renderHeatmapCalendar(this.container, calendarData)
```

