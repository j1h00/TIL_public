// redux version 
import React, {Component} from 'react';
import store from './store';
import './App.css';

class AddNumber extends Component {
    state = {size:1}
    render() {
      return (
            <div>
                <h1>Add Number</h1>
                <input type="button" value="+" onClick={function() {
                    // this.props.onClick(this.state.size);
                    store.dispatch({type: 'INCREMENT', size:this.state.size});
                }}></input>
                <input type="text" value={this.state.size} onChange={function(event) {
                    this.setState({size: Number(event.target.value)})
                }}></input>
            </div>
        )
    }
}

class AddNumberRoot extends Component {
  render() {
    return (
    	<div>
            <h1>Add Number Root</h1>
            <AddNumber></AddNumber>
        </div>
    )
  }
}

class DisplayNumber extends Component {
    state = {number: store.getState().number}
    constructor(props) {
        super(props);
        store.subscribe(function() {
            this.setState({number: store.getState().number});
        }.bind(this));
    }
    render() {
        return (
            <div>
              <h1>Display Number</h1>
              <input type="text" value={this.state.number} readOnly></input>
          </div>
      )
    }
}

class DisplayNumberRoot extends Component {
    render() {
        return (
            <div>
            <h1>Display Number Root</h1>
            <DisplayNumber></DisplayNumber>
        </div>
        )
    }
}

class App extends Component {
    state = {number: 0}
    render() {
        return (
            <div className="App">
                <h1>Root</h1>
                <AddNumberRoot></AddNumberRoot>
                <DisplayNumberRoot></DisplayNumberRoot>
            </div>
        )
    }
}

export default App;