import '../styles/app.css';
import {
  Routes,
  Route,
} from "react-router-dom";
import Main from './Main';
import Login from './Login';
import Register from './Register';


function App() {
  return (
    <Routes>
      <Route path="/" element={<Main />} /> 
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

export default App;
