# <mark style="background: #FF5582A6;">Reading</mark>

Looks for **Reading**

```dataviewjs
dv.span("")
const calendarData = {
    year: 2024,  // (optional) defaults to current year
    entries: [],
    intensityScaleStart: 0,
    intensityScaleEnd: 60
}

//DataviewJS loop
for (let page of dv.pages('"Daily Notes"').where(p => p.Reading)) {
    //dv.span("<br>" + page.file.name) // uncomment for troubleshooting
    calendarData.entries.push({
        date: page.file.name,     // (required) Format YYYY-MM-DD
        intensity: page.Reading, // (required) the data you want to track, will map color intensities automatically
        content: await dv.span(`[[${page.file.name}|]]`),           // (optional) Add text to the date cell
        color: "red"
    })
}

renderHeatmapCalendar(this.container, calendarData)
```