import React, { Component } from 'react'
function createOptions(avaliable_tastes){
    let options = []
    for(let i = 0; i < avaliable_tastes.length; i++){
        options[i] = (<option value={avaliable_tastes[i]} className='options' key={i}>{avaliable_tastes[i]}</option>)
    }
    return options
}
export class TasteCoefs extends Component {
    constructor(props) {
        super(props)
        this.state = {avaliable_tastes: props.avaliable_tastes, json: props.json, onDelete: props.onDelete}
        this.changeValue = this.changeValue.bind(this)
        this.changeTaste = this.changeTaste.bind(this)
        this.state.onSomethingChanged = props.onSomethingChanged
    }

    changeValue(event) {
        let prev = this.state
        prev.json.value = event.target.value
        this.setState(prev)
        this.state.onSomethingChanged(this.state.json)
    }
    changeTaste(event) {
        let prev = this.state
        prev.json.name = event.target.value
        this.setState(prev)
        this.state.onSomethingChanged(this.state.json)
    }

    render() {
        return (
        <div className='form'>
            <select value={this.state.json.name} onChange={this.changeTaste} className='select'>
                {createOptions(this.state.avaliable_tastes)}
            </select>
            <textarea value={this.state.json.value} onChange={this.changeValue} className='text-area'></textarea>
            <button onClick={this.state.onDelete} className='delete'>Удалить вкус</button>
        </div>
        )
    }
}

export default TasteCoefs