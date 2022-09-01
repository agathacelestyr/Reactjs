import React from "react";
import { Card } from "../../../components";

import "./style.css";
import { useSelector } from "react-redux";
export default function ClothesScreen(props) {
  const count = useSelector((store) => store.counter);
  const { detailing, handleproduct } = props;

  return (
    <div className="cloth-section-container">
      <div className="section-c-con1">
        <h3>Denim</h3>
        <div className="horizonal-scrolling">
          {(count.search.length === 0
            ? count.listOfClothesObject
            : count.listOfClothesObject.filter((item) =>
                item.item2.includes(count.search)
              )
          ).map((item) => {
            return (
              <Card
                thatitem={item}
                detailing={detailing}
                handleproduct1={handleproduct}
                ident={item.id}
              />
            );
          })}
        </div>
      </div>

      <div className="section-m-con1">
        <h3>levis</h3>
        <div className="horizonal-scrolling">
          {(count.search.length === 0
            ? count.listOfClothesObject
            : count.listOfClothesObject.filter((item) =>
                item.item2.includes(count.search)
              )
          ).map((item) => {
            return (
              <Card
                thatitem={item}
                detailing={detailing}
                handleproduct1={handleproduct}
                ident={item.id}
              />
            );
          })}
        </div>
      </div>
    </div>
  );
}
