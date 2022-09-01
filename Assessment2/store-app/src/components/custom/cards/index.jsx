import React from "react";
import "./style.css";
import { useNavigate } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import {
  decrementCart,
  incrementCart,
  handleincrese1,
  handledecrese1,
  handleproduct2,
  handleremove2,
} from "../../../redux/todoSlice";
export default function Card(props) {
  let navigate = useNavigate();
  const count = useSelector((store) => store.counter);
  const { thatitem, detailing, ident } = props;
  const dispatch = useDispatch();

  return (
    <div className="shop-item-container">
      <img
        src={count.listOfAllObject.find((item) => item.id === ident).item1}
        alt=""
        className="item-img"
      />
      <p
        className="item-name"
        onClick={() => {
          navigate("/browsing/detail");
          detailing(thatitem);
        }}
      >
        {count.listOfAllObject.find((item) => item.id === ident).item2}
      </p>
      <p className="item-description">
        {count.listOfAllObject.find((item) => item.id === ident).item3}
      </p>

      <span className="item-in-cart">
        <p
          className="item-remove-button"
          onClick={() => {
            if (
              count.listOfAllObject.find((item) => item.id === ident).quantity >
              0
            ) {
              dispatch(decrementCart());
              dispatch(handledecrese1(ident));
              dispatch(handleremove2(thatitem));
            }
          }}
        >
          -
        </p>
        <p className="item-quantity">
          {count.listOfAllObject.find((item) => item.id === ident).quantity}
        </p>
        <p
          className="item-add-button"
          onClick={() => {
            dispatch(incrementCart());
            dispatch(handleincrese1(ident));
            dispatch(handleproduct2(thatitem));
          }}
        >
          +
        </p>
      </span>
    </div>
  );
}
