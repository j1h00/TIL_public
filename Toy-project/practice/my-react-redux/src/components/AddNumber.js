import React, {Component} from 'react';

export default class AddNumber extends Component {
    state = {size:1}
    render() {
      return (
            <div>
                <h1>Add Number</h1>
                <input type="button" value="+" onClick={function() {
                    console.log('hello1')
                    this.props.onClick(this.state.size);
                }.bind(this)}></input>
                <input type="text" value={this.state.size} onChange={function(event) {
                    this.setState({size: Number(event.target.value)});
                }.bind(this)}></input>
            </div>
        )
    }
}