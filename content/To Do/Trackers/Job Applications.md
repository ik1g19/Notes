# <mark style="background: #FFB86CA6;">Job Applications</mark>

Looks for **Jobs**

```dataviewjs
dv.span("")
const calendarData = {
    year: 2024,  // (optional) defaults to current year
    entries: [],
    intensityScaleStart: 0,
    intensityScaleEnd: 120
}

//DataviewJS loop
for (let page of dv.pages('"Daily Notes"').where(p => p.Jobs)) {
    //dv.span("<br>" + page.file.name) // uncomment for troubleshooting
    calendarData.entries.push({
        date: page.file.name,     // (required) Format YYYY-MM-DD
        intensity: page.Jobs, // (required) the data you want to track, will map color intensities automatically
        content: await dv.span(`[[${page.file.name}|]]`),           // (optional) Add text to the date cell
        color: "orangetored"
    })
}

renderHeatmapCalendar(this.container, calendarData)
```