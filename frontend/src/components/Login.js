import React, { useContext, useState } from "react";
import { useFormik } from "formik";
import InputWidget from "./InputWidget";
import { Link, Navigate } from "react-router-dom";
import { loginInitial } from "../formik/initialValues";
import { loginValidation } from "../formik/validationSchema";
import { loginGenerator } from '../formik/formGenerators';
import { AuthContext } from '../context/AuthContext';
import { LOGIN_URL } from "../constants/urls";
import axios from "axios";

function Login() {
    const { updateTokens, isAuthenticated } = useContext(AuthContext);
    const [loginDetail, setLoginDetail] = useState();

    const formik = useFormik({
        initialValues: loginInitial,
        validationSchema: loginValidation,
        onSubmit: (values) => {
            axios.post(LOGIN_URL(), values)
            .then(updateTokens)
            .catch(({ response: { data: { detail } }}) => {
                setLoginDetail(detail);
            });
        },
    })

    if (isAuthenticated) return <Navigate to='/' />

    return (
        <div className='mt-5'>
            <h2>Login</h2>
            <form className='row registration-block d-flex align-items-center' onSubmit={formik.handleSubmit}>
            <div className='col-8'>
            {loginGenerator.map(
                (field) => <InputWidget key={field.name} {...{...field, handleChange: formik.handleChange, value: formik.values[field.name], error: formik.errors[field.name]}} />
            )}
            <div className='form-group'>
                <small>
                <Link to="/register">Whant to create new accout? Register</Link>
                </small>
            </div>
            {loginDetail && <p>{loginDetail}</p>}
            <button type='submit' className="btn btn-primary">Login</button>
            </div>
        </form>
    </div>
    )
};

export default Login;