import React, { useEffect, useState } from "react";
import axios from "axios";
import { LOGIN_URL, REFRESH_ACCESS_TOKEN_URL } from "../constants/urls";

export const AuthContext = React.createContext();

const TOKEN_NAME = 'refresh-auth-token';

export const AuthProvider = ({ children }) => {
  const [accessToken, setAccessToken] = useState();
  const [refreshToken, setRefreshToken] = useState(
      window.localStorage.getItem(TOKEN_NAME)
  )
  const [isAuthenticated, setIsAuthenticated] = useState(Boolean(accessToken));

  const apiBase = axios.create({
    baseURL: 'http://localhost:3000',
    proxy: 'http://localhost:8000',
    headers: {Authorization: accessToken},
  })

  const saveRefresh = (token) => window.localStorage.setItem(TOKEN_NAME, token);

  const updateTokens = ({data: {access, refresh}}) => {
    setAccessToken(accessToken);
    setRefreshToken(refresh);
    saveRefresh(refresh);
  }

  const login = (data) => axios.post(LOGIN_URL(), data).then(updateTokens);

  const logout = () => {
    window.localStorage.setItem(TOKEN_NAME, null);
    setAccessToken(null);
    setRefreshToken(null);
    setIsAuthenticated(false);
  }

  const getNewAccessToken = () => {
    axios.post(REFRESH_ACCESS_TOKEN_URL(), {refresh: refreshToken})
    .then(({data: {access}}) => {
        setAccessToken(access);
        setIsAuthenticated(true);
    })
  }

  useEffect(() => {
    if (accessToken) return;
    if (!accessToken && refreshToken) getNewAccessToken();
    if (!refreshToken && !refreshToken) setIsAuthenticated(false);
  }, [accessToken, refreshToken, isAuthenticated])
  
  const values = {
      accessToken,
      refreshToken,
      updateTokens,
      apiBase,
      saveRefresh,
      isAuthenticated,
      login,
      logout,
  }

  return (
    <AuthContext.Provider value={values}>{children}</AuthContext.Provider>
  );
};
