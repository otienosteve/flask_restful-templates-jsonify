import React, {useState} from 'react'
import {  useFormik } from 'formik'
import * as yup from "yup";

// Yup 
function AddStudent({addStudent}) {
    const studentSchema= yup.object().shape({
lastname: yup.string().required('You must enter a Value for this field').min(3,'Length Must be at least 3 characters'),
firstname: yup.string().required('You must enter a Value for this field'),
email: yup.string().email().required('Enter a Valid Email'),
feebalance: yup.number().required("Add Balance"),
gender:yup.string().oneOf(['Male', 'Female'])
    }) 




    const {errors,values, handleChange, handleSubmit} = useFormik(

        { initialValues: { firstname:"",
        lastname:"",
        feebalance:0,
        gender:"",
        email:""
        }, 
        onSubmit: function(values){
            console.log(values);
            addStudent(values)
        }, 
        validationSchema:studentSchema

        }
    )

// const handleSubmit= (e)=>{
// e.preventDefault()

// // addStudent(student)

// }
// const handleChange=(e)=>{
//     // console.log(e);
//     let key = e.target.id
//     let value = e.target.value
// setStudent(prevsetudent=> { return {...prevsetudent,[key]:value}})

// }

  return (
    <div> 
        {/* <form  onSubmit={handleSubmit}>
    <h3> Add Student</h3>
<input type='text' value={student.firstname}  onChange={handleChange} id='firstname' placeholder='firstname' /><br /><br />
<input type='text' value={student.lastname}  onChange={handleChange} id='lastname' placeholder='lastname' /><br /><br />
<input type='text' value={student.gender}  onChange={handleChange} id='gender' placeholder='gender' /><br /><br />
<input type='text' value={student.email}  onChange={handleChange} id='email' placeholder='email' /><br /><br />
<input type='text' value={student.feebalance}  onChange={handleChange} id='feebalance' placeholder='feebalance' /><br /><br />
<input type='submit' value="Add Student" /><br /><br />
</form>            */}
 <form onSubmit={handleSubmit}>
    <input type="text" name="firstname" id="" value={values.firstname} onChange={handleChange}/><br />
    {errors.firstname}
    <br />
    <input type="text" name="lastname" id="" value={values.lastname} onChange={handleChange}/><br />
    {errors.lastname}<br />
    <input type="text" name="email" id="" value={values.email}onChange={handleChange}/><br />
    {errors.email}<br />
    <input type="text" name="gender" id="" value={values.gender} onChange={handleChange}/><br />
    {errors.gender}<br />
    <input type="text" name="feebalance" id="" value={values.feebalance} onChange={handleChange}/><br />
    {errors.feebalance}<br />
    <input type="submit" value="Add Student" />
 </form>

        </div>
  )
}

export default AddStudent