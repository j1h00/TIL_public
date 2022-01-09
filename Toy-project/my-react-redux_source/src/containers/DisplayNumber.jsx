import DisplayNumber from '../components/DisplayNumber'
import { connect } from 'react-redux';

function mapReduxStateToReactProps(state){
    return {
        number: state.number
    };
}

export default connect(mapReduxStateToReactProps)(DisplayNumber);

// import React, { Component } from 'react';
// import store from "../store";
// export default class DisplayNUmber extends Component {
//     state = {number: store.getState().number}
//     constructor(props) {
//         super(props);
//         store.subscribe(function() {
//             this.setState({number: store.getState().number});
//         }.bind(this));
//     }
    
//     render() {
//         return (
//             <div>
//                 <h1>Display Number Root</h1>
//                 <DisplayNumber number={this.state.number}></DisplayNumber>
//             </div>
//         )
//     }
// }