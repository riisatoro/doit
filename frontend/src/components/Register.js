import React, { useContext, useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import '../styles/registration.css';
import AvatarEditor from 'react-avatar-editor'
import { useFormik } from 'formik';
import axios from "axios";
import { GRAVATAR_URL, REGISTRATION_URL } from '../constants/urls';
import InputWidget from "./InputWidget";
import { registerValidation } from "../formik/validationSchema";
import { registrationInitial } from "../formik/initialValues";
import { registrationGenerator } from '../formik/formGenerators';
import { AuthContext } from "../context/AuthContext";

function Register() {
  const [image, setImage] = useState();
  const [registrationInfo, setRegistrationInfo] = useState();

  const formik = useFormik({
    initialValues: registrationInitial,
    validationSchema: registerValidation,
    onSubmit: (values, {setFieldError}) => {
      const formData = new FormData()
      
      Object.keys(values).forEach((key) => formData.append(key, values[key]))
      formData.append('avatar', image);

      axios.post(REGISTRATION_URL(), formData)
      .then(({data: {detail}}) => setRegistrationInfo(detail))
      .catch(({response: {data: {detail}}}) => {
        Object.keys(detail).forEach((key) => {
          setFieldError(key, detail[key][0][0]);
        });
        console.log(detail)
      })
    },
  })

  const handleImageChange = (e) => setImage(e.target.files[0]);

  return (
    <div className='container'>
      <h2>Registration</h2>
      <form className='row registration-block d-flex align-items-center' onSubmit={formik.handleSubmit}>
        <h3>{registrationInfo}</h3>
        <div className='col-8'>
          {registrationGenerator.map(
            (field) => <InputWidget key={field.name} {...{...field, handleChange: formik.handleChange, value: formik.values[field.name], error: formik.errors[field.name]}} />
          )}
          <div className='form-group'>
            <small>
              <Link to="/login">Already have an account? Login</Link>
            </small>
          </div>
          <button type='submit' className="btn btn-primary">Register</button>
        </div>
        <div className='col-4'>
          <AvatarEditor
            image={image || GRAVATAR_URL('awdawd')}
            width={256}
            height={256}
            border={50}
            color={[255, 255, 255, 0.6]}
            borderRadius={256}
            scale={1}
            rotate={0}
          />
          <div className="form-group">
            <input 
              type="file" 
              accept=".jpg,.jpeg,.png"
              className="form-control-file" 
              name='avatar' 
              onChange={handleImageChange}
            />
          </div>
        </div>
      </form>
    </div>
  )
};

export default Register;