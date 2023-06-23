import React, {useState} from 'react'

function AddStudent({addStudent}) {

    const [student, setStudent]=useState({})

const handleSubmit= (e)=>{
e.preventDefault()
// console.log(student);
addStudent(student)
// console.log("Form submitted");
}
const handleChange=(e)=>{
    // console.log(e);
    let key = e.target.id
    let value = e.target.value
setStudent(prevsetudent=> { return {...prevsetudent,[key]:value}})

}

  return (
    <div> 
        <form  onSubmit={handleSubmit}>
    <h3> Add Student</h3>
<input type='text' value={student.firstname}  onChange={handleChange} id='firstname' placeholder='firstname' /><br /><br />
<input type='text' value={student.lastname}  onChange={handleChange} id='lastname' placeholder='lastname' /><br /><br />
<input type='text' value={student.gender}  onChange={handleChange} id='gender' placeholder='gender' /><br /><br />
<input type='text' value={student.email}  onChange={handleChange} id='email' placeholder='email' /><br /><br />
<input type='text' value={student.feebalance}  onChange={handleChange} id='feebalance' placeholder='feebalance' /><br /><br />
<input type='submit' value="Add Student" /><br /><br />
</form>           
        </div>
  )
}

export default AddStudent