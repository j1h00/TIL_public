import { useState } from "react";
import "./App.css";
import { TodoCard } from "./components/TodoCard";

function App() {
  const initialTodos = {
    "to Check": {},
    "to Buy": {},
    "to Read": {},
  };

  const [todos, setTodos] = useState(initialTodos);

  const paintTodoCard = Object.keys(todos).map((category) => (
    <TodoCard
      key={category}
      category={category}
      todos={todos}
      setTodos={setTodos}
    ></TodoCard>
  ));

  const handleDownButton = (content) => {};

  return (
    <div className="Todo-App">
      <div className="todo-container">
        <h1>Todos Application</h1>
        {paintTodoCard}
      </div>
    </div>
  );
}

export default App;
