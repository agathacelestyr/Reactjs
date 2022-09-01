import React from "react";
import "./style.css";
import { Card } from "../../../components";
import { useSelector } from "react-redux";
export default function Cart(props) {
  const { detailing } = props;

  const count = useSelector((store) => store.counter);
  return (
    <div className="">
      {count.listOfCartOjbect.length === 0 ? (
        <p>No items in cart</p>
      ) : (
        count.listOfCartOjbect.map((item) => {
          return <Card thatitem={item} detailing={detailing} ident={item.id} />;
        })
      )}
    </div>
  );
}
