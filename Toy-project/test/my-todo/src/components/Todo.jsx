import React from "react";

export const Todo = ({
  content,
  handleDownButton,
  handleRemoveButton,
  handleDoneButton,
}) => {
  return (
    <div>
      <input type="text"></input>
      <button onClick={() => handleDownButton(content)}>down</button>
      <button onClick={() => handleRemoveButton(content.id)}>remove</button>
      <button onClick={() => handleDoneButton(content.id)}>
        {content.done ? "undone" : "done"}
      </button>
    </div>
  );
};
