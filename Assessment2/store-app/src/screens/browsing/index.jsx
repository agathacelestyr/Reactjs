import React, { useState } from "react";
import { Card, NavBar } from "../../components";
import "./style.css";

import { Route } from "react-router-dom";
import MobileScreen from "./mobileScreen";
import Detail from "./details";
import ClothScreen from "./clothesScreen";
import { Routes } from "react-router-dom";
import Cart from "./cart";
import { useSelector } from "react-redux";

export default function Browsing(props) {
  const [det, setdet] = useState();
  const detailing = (product) => {
    setdet(product);
  };

  const count = useSelector((store) => store.counter);

  return (
    <div className="Browsing-Window">
      <NavBar className="over" />
      <div className="loading-container">
        <Routes>
          <Route
            path="/"
            element={
              <div className="Product-Window">
                {(count.search.length === 0
                  ? count.listOfAllObject
                  : count.listOfAllObject.filter((item) =>
                      item.item2.includes(count.search)
                    )
                ).map((item) => {
                  return (
                    <Card
                      thatitem={item}
                      detailing={detailing}
                      ident={item.id}
                    />
                  );
                })}
              </div>
            }
          />
          <Route
            path="/mobilescreen"
            element={<MobileScreen detailing={detailing} />}
          />
          <Route
            path="/clothscreen"
            element={<ClothScreen detailing={detailing} />}
          />
          <Route
            path="/detail"
            element={<Detail title={det} detailing={detailing} />}
          />
          <Route path="/cart" element={<Cart detailing={detailing} />} />
        </Routes>
      </div>
    </div>
  );
}
