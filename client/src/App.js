import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import AddStudent from './AddStudent';


function App() {
  const [student, setStudent] = useState([])

  useEffect(()=>{
fetch('http://127.0.0.1:5000/api').then(res=>res.json()).then( data=>{
    console.log(data)
    setStudent(data)
  })}, [])

  const addStudent = (student)=>{
    console.log(student)
    fetch('http://127.0.0.1:5000/api', {
method:"POST",
headers:{
  "accept":"application/json",
  "content-type":"application/json"
}, body:JSON.stringify(student)}).then(res=>res.json())

  }

  return (
    <div className="App">
      <h4>FLASK +REACT</h4>
    <AddStudent  addStudent={addStudent} />


    </div>
  );
}

export default App;
