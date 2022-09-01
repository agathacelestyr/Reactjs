import React from "react";
import "./style.css";
import { useNavigate } from "react-router-dom";
import cart from "../../../assest/images/cart.svg";
import profile from "../../../assest/images/profile.svg";
import { useSelector, useDispatch } from "react-redux";
import { onSearchChanging } from "../../../redux/todoSlice";
export default function NavBar(props) {
  let navigate = useNavigate();
  const count = useSelector((store) => store.counter);
  const dispatch = useDispatch();
  const { title = "Genral Store" } = props;

  return (
    <div className="NavBar-container">
      <p className="NavBar-title" onClick={() => navigate("/browsing/")}>
        {title}
      </p>
      <input
        type="text"
        placeholder="Search Product"
        className="NavBar-search"
        onChange={(e) => dispatch(onSearchChanging(e.target.value))}
      />
      <p
        onClick={() => navigate("/browsing/mobilescreen")}
        className="Mob-icon"
      >
        Mobile
      </p>
      <p onClick={() => navigate("/browsing/clothscreen")} className="Mob-icon">
        Clothes
      </p>
      <div className="NavBar-right">
        <span className="icon-container">
          <img
            src={cart}
            className="NavBar-icon"
            alt="cart"
            onClick={() => navigate("/browsing/cart")}
          />
          {count.sizeOfCart > 0 && (
            <p className="NavBar-icon-tooltip">{count.sizeOfCart}</p>
          )}
        </span>
        <img
          src={profile}
          alt=""
          className="NavBar-img"
          onClick={() => navigate("/")}
        />
      </div>
    </div>
  );
}
