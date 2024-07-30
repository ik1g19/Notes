# <mark style="background: #008fad;">Guitar</mark>

Looks for **Guitar**

```dataviewjs
dv.span("")
const calendarData = {
    year: 2024,  // (optional) defaults to current year
    entries: [],
    intensityScaleStart: 0,
    intensityScaleEnd: 240
}

//DataviewJS loop
for (let page of dv.pages('"Daily Notes"').where(p => p.Guitar)) {
    //dv.span("<br>" + page.file.name) // uncomment for troubleshooting
    calendarData.entries.push({
        date: page.file.name,     // (required) Format YYYY-MM-DD
        intensity: page.Guitar, // (required) the data you want to track, will map color intensities automatically
        content: await dv.span(`[[${page.file.name}|]]`),           // (optional) Add text to the date cell
        color: "cyanGradient"
    })
}

renderHeatmapCalendar(this.container, calendarData)
```

