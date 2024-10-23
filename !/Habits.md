---
habit_leetcode: Leetcode Exercise
habit_music_theory: The Jazz Theory Book - Read Chapter
habit_music_song_analysis: Work Through the Progression of a Song and Understand the Changes
habit_job_application: Job Application
habit_dev_django: Django - One Section
habit_dev_node: NodeJS - The Complete Guide - One Section
habit_read_it: Read 2 Chapters of IT
habit_exercise: Exercise
habit_food: Note down new recipe to try
habit_java_w3: Read through 5 Sections on W3's Page on Learning Java [🔗Link](https://www.w3schools.com/java/java_modifiers.asp)
habit_dev_spring: Learning Spring with Spring Boot - One Section
habit_tldr: Read TLDR Article
habit_medium: Read Medium Article
habit_study_plan: Tick off Study Plan Item
habit_games: Less than 1hr Games
---

## <mark style="background: #ABF7F7A6;">Leetcode</mark>


```dataviewjs
const calendarData = {
	year: moment().year(),
	colors: {
		"x": ["#228B22", "#228B22", "#228B22", "#228B22", "#79a8a8"],
		"-": ["#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000"],
		">": ["#696969", "#696969", "#696969", "#696969", "#696969"]
	},
	intensityScaleStart: 1,
	intensityScaleEnd: 5,
	entries: []
}

for(let page of dv.pages('"Daily Notes"').file.tasks.where(p=>p.checked).where(p=>String(p.section).includes("Habits")).where(p=>p.text.includes("habit_leetcode"))){
    calendarData.entries.push({
        date: page.path.split("/").pop().replace(".md", ""),
		color: page.status,
		intensity: 5
    })
}

renderHeatmapCalendar(this.container, calendarData)
```

## <mark style="background: #ABF7F7A6;">Music Theory</mark>


```dataviewjs
const calendarData = {
	year: moment().year(),
	colors: {
		"x": ["#228B22", "#228B22", "#228B22", "#228B22", "#79a8a8"],
		"-": ["#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000"],
		">": ["#696969", "#696969", "#696969", "#696969", "#696969"]
	},
	intensityScaleStart: 1,
	intensityScaleEnd: 5,
	entries: []
}

for(let page of dv.pages('"Daily Notes"').file.tasks.where(p=>p.checked).where(p=>String(p.section).includes("Habits")).where(p=>p.text.includes("habit_music_theory"))){
    calendarData.entries.push({
        date: page.path.split("/").pop().replace(".md", ""),
		color: page.status,
		intensity: 5
    })
}

renderHeatmapCalendar(this.container, calendarData)
```

## <mark style="background: #ABF7F7A6;">Studying new Development Language</mark>

```dataviewjs
const calendarData = {
	year: moment().year(),
	colors: {
		"x": ["#228B22", "#228B22", "#228B22", "#228B22", "#79a8a8"],
		"-": ["#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000"],
		">": ["#696969", "#696969", "#696969", "#696969", "#696969"]
	},
	intensityScaleStart: 1,
	intensityScaleEnd: 5,
	entries: []
}

for(let page of dv.pages('"Daily Notes"').file.tasks.where(p=>p.checked).where(p=>String(p.section).includes("Habits")).where(p=>p.text.includes("habit_dev"))){
    calendarData.entries.push({
        date: page.path.split("/").pop().replace(".md", ""),
		color: page.status,
		intensity: 5
    })
}

renderHeatmapCalendar(this.container, calendarData)
```

## <mark style="background: #ABF7F7A6;">Reading</mark>

```dataviewjs
const calendarData = {
	year: moment().year(),
	colors: {
		"x": ["#228B22", "#228B22", "#228B22", "#228B22", "#79a8a8"],
		"-": ["#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000"],
		">": ["#696969", "#696969", "#696969", "#696969", "#696969"]
	},
	intensityScaleStart: 1,
	intensityScaleEnd: 5,
	entries: []
}

for(let page of dv.pages('"Daily Notes"').file.tasks.where(p=>p.checked).where(p=>String(p.section).includes("Habits")).where(p=>p.text.includes("habit_read"))){
    calendarData.entries.push({
        date: page.path.split("/").pop().replace(".md", ""),
		color: page.status,
		intensity: 5
    })
}

renderHeatmapCalendar(this.container, calendarData)
```

## <mark style="background: #ABF7F7A6;">Workout</mark>

```dataviewjs
const calendarData = {
	year: moment().year(),
	colors: {
		"x": ["#228B22", "#228B22", "#228B22", "#228B22", "#79a8a8"],
		"-": ["#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000"],
		">": ["#696969", "#696969", "#696969", "#696969", "#696969"]
	},
	intensityScaleStart: 1,
	intensityScaleEnd: 5,
	entries: []
}

for(let page of dv.pages('"Daily Notes"').file.tasks.where(p=>p.checked).where(p=>String(p.section).includes("Habits")).where(p=>p.text.includes("habit_exercise"))){
    calendarData.entries.push({
        date: page.path.split("/").pop().replace(".md", ""),
		color: page.status,
		intensity: 5
    })
}

renderHeatmapCalendar(this.container, calendarData)
```




