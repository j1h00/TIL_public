import { click } from "@testing-library/user-event/dist/click";
import React, { useState } from "react";
import { Todo } from "./Todo";

export const TodoCard = ({ category, todos, setTodos }) => {
  const [nextId, setNextId] = useState(0);

  const handleDownButton = () => {};

  const handleCreateButton = () => {
    setTodos((prev) => {
      return {
        ...prev,
        [category]: {
          ...prev[category],
          [nextId]: {
            id: nextId,
            category: category,
            done: false,
          },
        },
      };
    });
    setNextId((prev) => prev + 1);
  };

  const handleRemoveButton = (clickedId) => {
    const newTodosInCateogry = { ...todos[category] };
    delete newTodosInCateogry[clickedId];

    setTodos((prev) => {
      return {
        ...prev,
        [category]: newTodosInCateogry,
      };
    });
  };

  const handleDoneButton = (clickedId) => {
    setTodos((prev) => {
      return {
        ...prev,
        [category]: {
          ...prev[category],
          [clickedId]: {
            ...prev[category][clickedId],
            done: !prev[category][clickedId].done,
          },
        },
      };
    });
  };

  const paintTodoList = Object.keys(todos[category]).map((id) => (
    <Todo
      key={`${category}-${id}`}
      content={todos[category][id]}
      handleRemoveButton={handleRemoveButton}
      handleDoneButton={handleDoneButton}
    ></Todo>
  ));

  return (
    <div className="todo-card">
      <h2>{category}</h2>
      {paintTodoList}
      <button onClick={() => handleCreateButton()}>Create</button>
    </div>
  );
};
