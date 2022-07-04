import React from "react";
import Type from "./Type";

export default function OrderPage() {
  return (
    <div>
      <h1>Travel Products</h1>
      <div>
        <Type orderType="products" />
      </div>
      <div style={{ display: "flex", marginTop: 20 }}>
        <div style={{ width: "50%" }}>
          <Type orderType="options" />
        </div>
        <div>
          <h2>Total Price: </h2>
          <br />
          <button onClick={() => {}}>주문하기</button>
        </div>
      </div>
    </div>
  );
}
