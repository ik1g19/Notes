# <mark style="background: #FFF3A3A6;">Cleaning</mark>

Looks for **Cleaning**

```dataviewjs
dv.span("")
const calendarData = {
    year: 2024,  // (optional) defaults to current year
    entries: [],
    intensityScaleStart: 0,
    intensityScaleEnd: 90
}

//DataviewJS loop
for (let page of dv.pages('"Daily Notes"').where(p => p.Cleaning)) {
    //dv.span("<br>" + page.file.name) // uncomment for troubleshooting
    calendarData.entries.push({
        date: page.file.name,     // (required) Format YYYY-MM-DD
        intensity: page.Cleaning, // (required) the data you want to track, will map color intensities automatically
        content: await dv.span(`[[${page.file.name}|]]`),           // (optional) Add text to the date cell
        color: "orangetored"
    })
}

renderHeatmapCalendar(this.container, calendarData)
```

