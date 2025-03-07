import React, { Component } from 'react'
import TasteCoefs from './TasteCoefs'
function createOptions(avaliable_ingredients){
    let options = []
    for(let i = 0; i < avaliable_ingredients.length; i++){
        options[i] = (<option value={avaliable_ingredients[i]} className='options' key={i}>{avaliable_ingredients[i]}</option>)
    }
    return options
}
function createTastes(tastes, avaliable_tastes, onDelete, onSomethingChanged) {
    let taste = []
    for (let i = 0; i < tastes.length; i++) {
        let cur = tastes[i]
        taste[i] = (<TasteCoefs key={cur.id} json={cur} avaliable_tastes={avaliable_tastes} onDelete={() => onDelete(cur.id)} onSomethingChanged={onSomethingChanged}/>)
    }
    return taste
}
export class Coeficients extends Component {
    constructor(props){
        super(props)
        this.state = {json:props.json, avaliable_tastes: props.avaliable_tastes, avaliable_ingredients: props.avaliable_ingredients}
        this.state.id = props.id
        this.state.onDelete = props.onDelete
        this.state.onSomethingChanged = props.onSomethingChanged
        this.changeName = this.changeName.bind(this)
        this.deleteTaste = this.deleteTaste.bind(this)
        this.addTaste = this.addTaste.bind(this)
        this.onTasteChanged = this.onTasteChanged.bind(this)
    }
    changeName(event){
        var prevState = this.state
        prevState.json.name = event.target.value
        this.setState(prevState)
        this.state.onSomethingChanged(this.state.json)
    }

    deleteTaste(id) {
        let prevState = this.state
        prevState.json.tastes = prevState.json.tastes.filter(p => p.id !== id)
        this.setState(prevState)
        this.state.onSomethingChanged(this.state.json)
    }
    addTaste() {
        let l = this.state.json.tastes.length
        let prev = this.state
        prev.json.tastes[l] = {
            id: l > 0 ? this.state.json.tastes[l - 1].id + 1 : 0,
            name: "",
            value: 0
        }
        this.setState(prev)
        this.state.onSomethingChanged(this.state.json)
    }
    onTasteChanged(json) {
        let prev = this.state
        for (let i = 0; i < this.state.json.tastes.length; i++) {
            if (prev.json.tastes[i].id === json.id) {
                prev.json.tastes[i] = json
            }
        }
        this.setState(prev)
        this.state.onSomethingChanged(this.state.json)
    }
    render() {
        return (
        <div>
            <label>Выберете ингредиент</label>
                <select value={this.state.json.name} onChange={this.changeName} className='select'>
                    {createOptions(this.state.avaliable_ingredients)}
                </select>
                <button onClick={this.state.onDelete} className='delete'>Удалить ингредиент</button>
                {createTastes(this.state.json.tastes, this.state.avaliable_tastes, this.deleteTaste, this.onTasteChanged)}
                <button onClick={this.addTaste} className='add'>Добавить вкус </button>
        </div>
        )
    }
}
export default Coeficients