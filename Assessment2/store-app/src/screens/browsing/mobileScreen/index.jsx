import React from "react";
import { Card } from "../../../components";

import "./style.css";
import { useSelector } from "react-redux";
export default function MobileScreen(props) {
  const count = useSelector((store) => store.counter);
  const { detailing, handleproduct } = props;

  return (
    <div className="mobile-section-container">
      <div className="section-m-con1">
        <h3>Realme</h3>
        <div className="horizonal-scrolling">
          {(count.search.length === 0
            ? count.listOfRealmeObject
            : count.listOfRealmeObject.filter((item) =>
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
        <h3>oppo</h3>
        <div className="horizonal-scrolling">
          {(count.search.length === 0
            ? count.listOfRealmeObject
            : count.listOfRealmeObject.filter((item) =>
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
