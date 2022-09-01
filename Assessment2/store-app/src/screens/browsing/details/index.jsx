import React from "react";
import { Card, ProductDetail } from "../../../components";
import "./style.css";
import { useSelector } from "react-redux";
export default function Detail(props) {
  const count = useSelector((store) => store.counter);
  const { title, detailing } = props;

  return (
    <div className="product-detail">
      <ProductDetail thatitem={title} ident={title.id} />
      <p>Suggestion</p>
      <div className="Product-Window">
        {(count.search.length === 0
          ? count.listOfAllObject
          : count.listOfAllObject.filter((item) =>
              item.item2.includes(count.search)
            )
        ).map((item) => {
          return <Card detailing={detailing} ident={item.id} thatitem={item} />;
        })}
      </div>
    </div>
  );
}
