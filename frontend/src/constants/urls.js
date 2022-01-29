export const GRAVATAR_URL = (hash) => `https://www.gravatar.com/avatar/${hash}?d=identicon&s=512`;
export const REGISTRATION_URL = () => '/auth/register/';
export const LOGIN_URL = () => '/auth/token/';
export const REFRESH_ACCESS_TOKEN_URL = () => '/auth/refresh/';
export const LOGGED_USER_INFO_URL = () => '/user/';
export const USER_INFO_URL = (slug) => `/user?slug=${slug}`;