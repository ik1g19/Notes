# Concepts

#react #udemy-course
# Creating the React Project

Rather than using HTML or CSS to build our web pages, we will build them using React components

We will be using `Vite` as opposed to `NextJS` etc... as the framework to create the React project

Using `npm` you can create a Vite project using

```
npm create vite@latest
```

First you will be prompted to enter a Vite project name

Then you will be prompted to select a framework for this project, which in this case will be React

![[notes/Courses/Udemy Courses/Complete guide to building an app with DotNet Core and React/Images/Pasted image 20240421234846.png|400]]

You will then be prompted to choose a variant, which in this case will be using TypeScript and **S**peedy **W**eb **C**ompiler

![[notes/Courses/Udemy Courses/Complete guide to building an app with DotNet Core and React/Images/Pasted image 20240421234944.png|400]]

Then `cd ./client-app` and run `npm install` to install all the dependencies needed

Start the Vite-React application using:

```
npm run dev
```

It will start on localhost:5173 by default

![[notes/Courses/Udemy Courses/Complete guide to building an app with DotNet Core and React/Images/Pasted image 20240421235132.png]]

# Reviewing the React Project Files

![[Images/Pasted image 20241103200114.png|150]]

- `node_modules` contains all of the dependencies the project is using
	- It gets the dependencies from `package.json`
- `index.html` is the boilerplate HTML
	- Default React scripts are loaded through`<script type="module" src="/src/main.tsx"></script>`
- `vite.config.ts` is the Vite configuration file
- `tsconfig.json` is for typescript configuration
- We use `public` for images etc.

You can add a script to `client-app\package.json` and then trigger it with `npm [name]`

```json
"scripts": {
    "start": "vite",
    "dev": "vite",
    "build": "tsc && vite build",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview"
  },
```

We replace the default React page with this

📁`client-app\src\App.tsx`
```tsx
import './App.css'

function App() {

  return (
    <h1>Reactivies</h1>
  )
}

export default App
```

We can remove all the default styling as well by deleting everything inside `client-app\src\App.css` and `client-app\src\index.css`

We can change the server port with

📁`client-app\vite.config.ts`
```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 3000
  },
  plugins: [react()],
})
```

# React Components

How React components work

![[Images/20241104_220006.jpg]]
## Virtual DOM

Virtual Domain Object Model

Kept in memory and synced with the real DOM via React

![[Images/camera_capture.jpg]]

Data cannot flow backwards from DOM to VDOM in React

## JSX

Sugar coating over JavaScript, that makes it look like html

## React Hooks

Hooks are functions that let us hook into Reacts state and lifecycle features

Common hooks
- `useState()` this will track state inside the component
	- A function component is a function that returns JSX
- `useEffect()` adds a side effect to our function so that something happens when our component mounts

# Typescript Components

## Typescript Features

| Pros                                 | Cons              |
| ------------------------------------ | ----------------- |
| Strong Typing                        | More Upfront Code |
| Object Oriented                      |                   |
| Access Modifiers                     |                   |
| Catches Mistakes Weak Typing Doesn't |                   |
# TypeScript Demo & Basics

[[notes/Uni Content/Advanced Programming Language Concepts/Week 3/Gradual Typing#Union Type|Union Typing]] allows multiple possible types

```ts
let data: number | string = 42

data = '42'
```

# Using TypeScript with React

Only one thing can be returned at a time in JSX

```tsx
import './App.css'

function App() {

  return (
    <h1>Reactivies</h1>
  )
}

export default App
```

When we want to use Java or TypeScript in a JSX element we use `{}`

The following example code demonstrates how TypeScript components can be used in React

`() => duck.makeSound` is wrapped in a callback method so that execution is deferred until the button is actually clicked, otherwise it would be executed as soon as the page is loaded

When iterating through elements e.g. using `map`, a unique key needs to be provided, as seen in `<div key={duck.name}>`

📁`demo.ts`
```ts
interface Duck {
  name: string;
  numLegs: number;
  makeSound: (sound: string) => void;
}

const duck1: Duck = {
  name: 'huey',
  numLegs: 2,
  makeSound: (sound: string) => console.log(sound)
}

const duck2: Duck = {
  name: 'duey',
  numLegs: 2,
  makeSound: (sound: string) => console.log(sound)
}

duck1.makeSound('quack');
duck2.makeSound('sound');
```

📁`App.tsx`
```tsx
import './App.css'
import { ducks } from './demo'

function App() {
  return (
    <div>
      <h1>Reactivities</h1>
      {ducks.map(duck => (
        <div key={duck.name}>
          <span>{duck.name}</span>
          <button onClick={() => duck.makeSound(duck.name + ' quack')}>Make sound</button>
        </div>
      ))}
    </div>
  )
}

export default App
```

This next example shows how to use a React component

The component accepts a Prop as a parameter

📁`App.tsx`
```tsx
import './App.css'
import { ducks } from './demo'

function App() {
  return (
    <div>
      <h1>Reactivities</h1>
      {ducks.map(duck => (
        <div key={duck.name}>
          <DuckItem key={duck.name} duck={duck} />
        </div>
      ))}
    </div>
  )
}

export default App
```

📁`DuckItem.tsx`
```tsx
import { Duck } from './demo'

interface Props {
  duck: Duck
}

export default function DuckItem({ duck }: Props) {
  return (
    <div key={duck.name}>
      <span>{duck.name}</span>
      <button onClick={() => duck.makeSound(duck.name + ' quack')}>Make sound</button>
    </div>
  )
}
```

# Web Extensions for Debugging

[React DevTools](https://addons.mozilla.org/en-GB/firefox/addon/react-devtools/)

# Fetching Data from the API

We will use Axios

>[!INFO]
>Axios is a _[promise-based](https://javascript.info/promise-basics)_ HTTP Client for `node.js` and the browser

