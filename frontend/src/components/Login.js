import React from "react";
import axios from "axios";
import { useFormik } from "formik";
import InputWidget from "./InputWidget";
import { Link } from "react-router-dom";
import { LOGIN_URL } from "../utils/urls";
import { useNavigate } from 'react-router-dom';

function Login() {

    const formFields =[
        {
            name: 'username',
            type: 'text',
        },
        {
            name: 'password',
            type: 'password',
        }
    ]

    const formik = useFormik({
        initialValues: {username: '', password: ''},
        onSubmit: (data) => {
            axios.post(LOGIN_URL(), data)
            .then((response) => {console.log(response)})
            .catch(({response: {data: {detail}}}) => {
                Object.keys(detail).forEach((key) => {
                  formik.setFieldError(key, detail[key]);
                })
              })
        }
    })

    return (
        <div className='container'>
            <h2>Login</h2>
            <form className='row registration-block d-flex align-items-center' onSubmit={formik.handleSubmit}>
            <div className='col-8'>
            {formFields.map(
                (field) => <InputWidget key={field.name} {...{...field, handleChange: formik.handleChange, value: formik.values[field.name], error: formik.errors[field.name]}} />
            )}
            <div className='form-group'>
                <small>
                <Link to="/register">Whant to create new accout? Register</Link>
                </small>
            </div>
            <button type='submit' className="btn btn-primary">Login</button>
            </div>
        </form>
    </div>
    )
};

export default Login;