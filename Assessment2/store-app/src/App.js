import { Browsing, Authentication } from "./screens";
import "./App.css";
import { Routes, Route } from "react-router-dom";
export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Authentication />} />
      <Route path="/browsing/*" element={<Browsing />} />
    </Routes>
  );
}
