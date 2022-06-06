// redux version 
import React, {Component} from 'react';
import AddNumberRoot from './components/AddNumberRoot';
import DisplayNumberRoot from './components/DisplayNumberRoot'
import './App.css';

class App extends Component {
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