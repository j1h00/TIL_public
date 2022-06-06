import React from "react";
import { connect } from "react-redux";

function Home({ toDos }) {
  const [text, setText] = useState("");
  function onChange(e) {
    setText(e.terget.value);
  }
  function onSubmit(e) {
    e.preventDefault();
    setText("");
  }
  return (
    <>
      <h1>To Do</h1>
      <form onSubmit={}>
        <input type="text" value={text} />
        <button>Add</button>
      </form>
      <ul></ul>
    </>
  );
}

//mapStateToProps
function getCurrentState(state) {
  return { toDos: state }
}

export default connect(getCurrentState)(Home);
