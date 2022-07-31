import logo from './logo.svg';
import React, { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios'

function App() {
  const [goal, setGoal] = useState("");
  const [goals, setGoals] = useState([])

  useEffect(()=> {
    console.log("Constructor")
    loadGoals()
  }, [])

  const loadGoals = () => {
    console.log("Fetching goals")
    axios.get("http://localhost:2000/goals")
      .then(res => {
        console.log(res.data)
        setGoals(res.data.goals)
    }).catch(e => {
      console.log(e)
    })
  }

  const handleGoalChange = (e) => {
    console.log("e");
    setGoal(e.target.value);
  }
  const handleKeyDown = (e) => {
    if (goal.trim() === "") {
      return;
    }
    if (e.code === "Enter" || e.code === "NumpadEnter") {
      axios.post("http://localhost:2000/goals", {text: goal}).then(e=> {
        console.log("Added goal");
        setGoal("");

        loadGoals()
      }).catch(e => {
        console.log("Error adding goal");
      })
    }
  }
  const handleClick = (id) => {
    console.log("Deleting goal")
    axios.delete(`http://localhost:2000/goals/${id}`).then(res=> {
      console.log("Deleting goal finished")
      loadGoals()
    }).catch(err => {
      console.log("Error deleting goal")
    })
  }


  return (
    <div className="App">
      <h1>Love Update</h1>
      <div>
        <p>Add goal</p>
        <input placeholder='Type goal and press enter' value={goal} onKeyDown={handleKeyDown} onChange={handleGoalChange}></input>
      </div>
      <ul>
        {goals.map(goal => <li key={goal.id} onClick={()=>handleClick(goal.id)}> {goal.text} </li>)} 
      </ul>
    </div>
  );
}

export default App;
