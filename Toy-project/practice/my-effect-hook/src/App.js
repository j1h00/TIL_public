import { useEffect, useState } from "react";

function App() {
  const [counter, setValue] = useState(0);
  const [keyword, setKeyword] = useState("");

  const onClick = () => setValue((prev) => prev + 1);
  const onChange = (event) => setKeyword(event.target.value);
  console.log("run all the time");

  useEffect(() => {
    console.log("run only once");
  }, []);

  useEffect(() => {
    if (keyword !== "" && keyword.length > 2) {
      console.log("KEYWORD CHANGES: ", keyword);
    }
  }, [keyword]);

  useEffect(() => {
    console.log("COUNTER CHANGES");
  }, [counter]);

  useEffect(() => {
    console.log("KEYWORD & COUNTER CHANGES");
  }, [keyword, counter]);

  return (
    <div>
      <input onChange={onChange} type="text" placeholder="Search here..." />
      <h1>{counter}</h1>
      <button onClick={onClick}>click me</button>
    </div>
  );
}

function Hello() {
  useEffect(() => {
    console.log("Im here!");
  }, []);
  return <h1>Hello</h1>;
}

function App2() {
  const [showing, setShowing] = useState(false);
  const onClick = () => setShowing((prev) => !prev);
  return (
    <div>
      {showing ? <Hello /> : null}
      <button onClick={onClick}>{showing ? "Hide" : "Show"}</button>
    </div>
  );
}

export default App;
