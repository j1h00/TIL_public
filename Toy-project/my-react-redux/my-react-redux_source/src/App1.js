// props version 
import React, {Component} from 'react';
import './App.css';

class AddNumber extends Component {
    state = {size:1}
    render() {
        return (
            <div>
                <h1>Add Number</h1>
                <input type="button" value="+" onClick={function() {
                    this.props.onClick(this.state.size);
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
            <AddNumber onClick={function(size) {
                this.props.onClick(size);
            }.bind(this)}></AddNumber>
        </div>
    )
  }
}

class DisplayNumber extends Component {
    render() {
        return (
            <div>
              <h1>Display Number</h1>
              <input type="text" value={this.props.number} readOnly></input>
          </div>
      )
    }
}

class DisplayNumberRoot extends Component {
    render() {
        return (
            <div>
            <h1>Display Number Root</h1>
            <DisplayNumber number={this.props.number}></DisplayNumber>
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
                <AddNumberRoot onClick={function(size) {
                    this.setState({number:this.state.number + size});
                }}></AddNumberRoot>
                <DisplayNumberRoot number={this.state.number}></DisplayNumberRoot>
            </div>
        )
    }
}

export default App;