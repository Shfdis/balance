import React, { Component } from 'react'

export class Taste extends Component {
    constructor(props){
        super(props)
        this.state = {json: props.json}
        this.state.onDelete = props.onDelete
        this.state.onSomethingChanged = props.onSomethingChanged
        this.changeName = this.changeName.bind(this)
    }
    changeName(event){
        var prevState = this.state
        prevState.json.name = event.target.value
        this.setState(prevState)
        this.state.onSomethingChanged(this.state.json)
    }
    render() {
        return (
        <div className='form'>
            <textarea value={this.state.json.name} onChange={this.changeName} className='text-area'></textarea>
            <button onClick={this.state.onDelete} className='delete'>Удалить вкус</button>
        </div>
        )
    }
}

export default Taste