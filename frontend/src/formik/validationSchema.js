import * as Yup from 'yup';

const loginFormShape = {
    username: Yup.string()
    .min(5, 'Too Short!')
    .max(50, 'Too Long!')
    .required('Required'),
    password: Yup.string()
    .min(8, 'Too Short!')
    .required('Required'),
};

const registerFormShape = {
    ...loginFormShape,
    email: Yup.string()
      .email()
      .required('Required'),
    
    confirm_password: Yup.string()
      .min(8, 'Too Short!')
      .required('Required'),
};

export const loginValidation = Yup.object().shape(loginFormShape);
export const registerValidation = Yup.object().shape(registerFormShape);
