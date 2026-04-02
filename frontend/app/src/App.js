import { useEffect, useState } from "react";
import './App.css'
function App() {
  const [imagen, setImagen] = useState("");
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/posts/")
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setImagen(data.message);
      });
  }, []);

  return (
    <div className="App">
      <h1 className="App-header">Imagen desde API</h1>
      {imagen ? (
        <img className="App-Logo" src={imagen} alt="perro" width="300"/>
      ) : (
        <p>en seguida xd...</p>
      )}
    </div>
  );
}

export default App;