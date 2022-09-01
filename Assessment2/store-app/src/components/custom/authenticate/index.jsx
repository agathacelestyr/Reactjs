import React from "react";
import "./style.css";
import { getData } from "../../../api/authenicationdata/data";
import { useNavigate } from "react-router-dom";

export default function FormPage(props) {
  let navigate = useNavigate();
  return (
    <div className="form-container">
      <form className="form-fields" id="data-form">
        <span className="from-field">
          <label htmlfor="id-name" className="label">
            Username
          </label>
          <input
            id="id-username"
            name="user-name"
            type="text"
            placeholder=""
            className="input-box-text"
            required
          />
        </span>
        <span className="from-field">
          <label htmfor="id-name" className="label">
            Password
          </label>
          <input
            id="id-password"
            name="user-name"
            type="password"
            placeholder=""
            className="input-box-text"
            required
          />
        </span>
        <input
          type="submit"
          className="input-box-text1"
          value="Submit"
          onClick={() => {
            getInputValue() ? navigate("/browsing/") : prompt("error");
          }}
        />
      </form>
    </div>
  );
}

function getInputValue() {
  let user = document.getElementById("id-username").value;
  let pass = document.getElementById("id-password").value;
  let d = getData();
  if (d[0].username === user && d[0].password === pass) {
    return true;
  } else return false;
}
