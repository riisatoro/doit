import '../styles/app.css';
import {
  Routes,
  Route,
} from "react-router-dom";
import Main from './Main';
import Login from './Login';
import Register from './Register';
import Header from './Header';

function App() {
  return (
    <div>
      <Header />
      <Routes>
        <Route path="/" element={<Main />} /> 
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </div>
  );
}

export default App;
