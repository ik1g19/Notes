---
habit_leetcode: Leetcode Exercise
habit_music_theory: The Jazz Theory Book - Read Chapter
habit_music_song_analysis: Work Through the Progression of a Song and Understand the Changes
habit_job_application: Job Applications
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
habit_coffee: Only 1 coffee/No Coffee
habit_dotnet_guide: Complete Guide to building an App with .NET Core and React - One Section
habit_moisturize: Moisturize Face
habit_song_writing: Spend Time Learning/Reading about Song Writing or Create/Produce Something
habit_game_dev: Practise some Game Development by Following a Tutorial/Work on a Project
---

## <mark style="background: #ABF7F7A6;">Study Plan Progress</mark>

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

for(let page of dv.pages('"Daily Notes"').file.tasks.where(p=>p.checked).where(p=>String(p.section).includes("Habits")).where(p=>p.text.includes("habit_study_plan"))){
    calendarData.entries.push({
        date: page.path.split("/").pop().replace(".md", ""),
		color: page.status,
		intensity: 5
    })
}

renderHeatmapCalendar(this.container, calendarData)
```


## <mark style="background: #ABF7F7A6;">Focus</mark>

| <div style="height: 20px; width: 20px; background-color: #a9415e; border-radius: 5px; "></div> | `$= dv.page("Habits").habit_dotnet_guide`    |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------- |
| <div style="height: 20px; width: 20px; background-color: #4eb1bc; border-radius: 5px; "></div> | `$= dv.page("Habits").habit_job_application` |
| <div style="height: 20px; width: 20px; background-color: #009f50; border-radius: 5px; "></div> | `$= dv.page("Habits").habit_study_plan`      |

```dataviewjs
const calendarData = {
    year: moment().year(),
    colors: {
        red: ["#a9415e"],
        blue: ["#4eb1bc"],
        green: ["#009f50"]
    },
    entries: []
}

for(let page of dv.pages('"Daily Notes"').where(p=>p.focus)){

	let color = ""
	if (page.focus=="habit_dotnet_guide"){color="red"}
	if (page.focus=="habit_job_application"){color="blue"}
	if (page.focus=="habit_study_plan"){color="blue"}

	if (color != "") {
	    calendarData.entries.push({
	        date: page.file.name,
	        color: color,
	        intensity: 1
	    })
	}
       
}

renderHeatmapCalendar(this.container, calendarData);
```


