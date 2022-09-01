import React from "react";
import "./style.css";
import { useSelector, useDispatch } from "react-redux";
import {
  decrementCart,
  handledecrese1,
  handleincrese1,
  handleproduct2,
  incrementCart,
} from "../../../redux/todoSlice";
export default function ProductSpecific(props) {
  const count = useSelector((store) => store.counter);
  const dispatch = useDispatch();
  const { thatitem, ident } = props;
  return (
    <div className="product-specific">
      <img src={thatitem.item1} alt="" className="separate-img1" />
      <img src={thatitem.item1} alt="" className="separate-img2" />
      <img src={thatitem.item1} alt="" className="separate-img3" />
      <img src={thatitem.item1} alt="" className="separate-full-img" />
      <p className="product-name"> {thatitem.item2}</p>
      <p className="product-detail">{thatitem.item3}</p>
      <p className="product-price">{thatitem.price}</p>

      <span className="item-cart">
        <p
          className="item-remove-button"
          onClick={() => {
            if (count.sizeOfCart > 0) {
              dispatch(decrementCart());
              dispatch(handledecrese1(ident));
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
