---
game_time: 0
--- 

```dataviewjs
// Define the programming languages to rotate through
const languages = ["Java", "Python", "C++"];

// Extract the date from the file name (assumed format: yyyy-mm-dd)
const fileName = dv.current().file.name;
const dateParts = fileName.split("-");
if (dateParts.length === 3) {
    const year = parseInt(dateParts[0]);
    const month = parseInt(dateParts[1]) - 1; // Months are 0-indexed in JavaScript
    const day = parseInt(dateParts[2]);

    // Calculate the day of the year
    const dayOfYear = Math.floor(
        (Date.UTC(year, month, day) - Date.UTC(year, 0, 0)) / 24 / 60 / 60 / 1000
    );

    // Determine the programming language
    const languageForToday = languages[dayOfYear % languages.length];

    // Display the language
    dv.paragraph(`**Today's Leetcode Language:** ${languageForToday}`);
} else {
    dv.paragraph("Error: File name does not match the expected yyyy-mm-dd format.");
}
```

# To Do

![[To Dos/To Do 3|To Do]]

# Habits

- [ ] `$= dv.page("Habits").habit_leetcode`
- [ ] `$= dv.page("Habits").habit_dotnet_guide`
- [ ] `$= dv.page("Habits").habit_java_spring`
- [ ] `$= dv.page("Habits").habit_wpf`

![[Organisation/Habits#<mark style="background ABF7F7A6;">Only 1 Coffee</mark>]]

![[Organisation/Habits#<mark style="background ABF7F7A6;">Leetcode</mark>|Habits]]


- [ ] `$= dv.page("Habits").habit_coffee`
- [ ] `$= dv.page("Habits").habit_moisturize`
- [ ] `$= dv.page("Habits").habit_vitamins`
- [ ] `$= dv.page("Habits").habit_song_writing`
- [ ] `$= dv.page("Habits").habit_game_dev`
- [ ] `$= dv.page("Habits").habit_song_analysis`

#daily-note

```dataviewjs
// DataviewJS snippet for task progress bar

// Get all tasks from the current file
let currentFile = dv.current();

// Filter tasks that contain the word "jobs"
let allTasks = currentFile.file.tasks.filter(t => t.text.toLowerCase().includes('habit'));

// Count completed tasks and total tasks
let completedTasks = allTasks.filter(t => t.completed).length;
let totalTasks = allTasks.length;

// Avoid division by zero
let progress = totalTasks === 0 ? 0 : Math.floor((completedTasks / totalTasks) * 100);

// Set progress bar color to #4caf50 when progress is 100%, otherwise keep the original color
let progressBarColor = progress === 100 ? '#4caf50' : '#2b8089';

// Render progress bar
let progressBar = ` <div style="text-align: center; margin-top: 10px;"> 
<div style="background-color: #ddd; border-radius: 10px; padding: 2px; width: 80%; display: inline-block;"> 
<div style="background-color:${progressBarColor}; width: ${progress}%; height: 4px; border-radius: 10px;"></div> </div> </div>`;

dv.paragraph(`${completedTasks}/${totalTasks} Habits Completed`);
dv.paragraph(progressBar);

```


[[Templates/Daily Notes Template|Daily Notes Template]]