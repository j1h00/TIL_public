import React from "react";

export default function Options({ name }) {
  return (
    <form>
      <input type="checkbox" id={`${name} option`} />{" "}
      <label htmlFor={`${name} option`}>{name}</label>
    </form>
  );
}
