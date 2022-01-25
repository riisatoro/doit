import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import '../styles/registration.css';
import AvatarEditor from 'react-avatar-editor'
import { useFormik } from 'formik';
import axios from "axios";
import { GRAVATAR_URL, REGISTRATION_URL } from '../utils/urls';
import InputWidget from "./InputWidget";
import * as Yup from 'yup';

function Register() {
  const [image, setImage] = useState('');
  const formFields = [
    {
      name: 'username',
      type: 'text'
    },
    {
      name: 'email',
      type: 'email'
    },
    {
      name: 'password',
      type: 'password'
    },
    {
      name: 'confirm_password',
      type: 'password'
    },
  ]

  const formValidation = Yup.object().shape({
    username: Yup.string()
      .min(5, 'Too Short!')
      .max(50, 'Too Long!')
      .required('Required'),
    email: Yup.string()
      .email()
      .required('Required'),
    password: Yup.string()
      .min(8, 'Too Short!')
      .required('Required'),
    confirm_password: Yup.string()
      .min(8, 'Too Short!')
      .required('Required'),
  });

  const formik = useFormik({
    initialValues: {
      username:'', email: '', password: '', confirm_password: '', avatar: '',
    },
    validationSchema: formValidation,
    onSubmit: (values, {setFieldError}) => {
      axios.post(REGISTRATION_URL(), values)
      .then((response) => console.log(response))
      .catch(({response: {data: {detail}}}) => {
        Object.keys(detail).forEach((key) => {
          setFieldError(key, detail[key][0][0]);
        });
        setErrors(FormikErrors);
      })
    },
  })

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
    formik.handleChange(e);
  }

  return (
    <div className='container'>
      <h2>Registration</h2>
      <form className='row registration-block d-flex align-items-center' onSubmit={formik.handleSubmit}>
        <div className='col-8'>
          {formFields.map(
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
              value={formik.values.avatar}
            />
          </div>
        </div>
      </form>
    </div>
  )
};

export default Register;