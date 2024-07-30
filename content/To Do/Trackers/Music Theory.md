# <mark style="background: #126453;">Music Theory</mark>

Looks for **Theory**

```dataviewjs
dv.span("")
const calendarData = {
    year: 2024,  // (optional) defaults to current year
    entries: [],
    intensityScaleStart: 0,
    intensityScaleEnd: 60
}

//DataviewJS loop
for (let page of dv.pages('"Daily Notes"').where(p => p.Theory)) {
    //dv.span("<br>" + page.file.name) // uncomment for troubleshooting
    calendarData.entries.push({
        date: page.file.name,     // (required) Format YYYY-MM-DD
        intensity: page.Theory, // (required) the data you want to track, will map color intensities automatically
        content: await dv.span(`[[${page.file.name}|]]`),           // (optional) Add text to the date cell
        color: "tealGradient"
    })
}

renderHeatmapCalendar(this.container, calendarData)
```