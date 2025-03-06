import React, { Component } from 'react'
import Taste from './Taste'
import Ingredients from './Ingredients'
const showTastes = (props, onDelete, onSomethingChanged) => {
    let ans = []
    for (let i = 0; i < props.json.tastes.length; i++) {
        ans.push(<Taste json={props.json.tastes[i]} key={props.json.tastes[i].id} onDelete={() => onDelete(props.json.tastes[i].id)} onSomethingChanged={onSomethingChanged}/>)
    }
    return (<div>
        {ans}
    </div>)
}
const showMeasures = (props, onDelete, onSomethingChanged) => {
    let ans = []
    for (let i = 0; i < props.json.default_measures.length; i++) {
        let cur = props.json.default_measures[i]
        ans.push(<Ingredients json={cur} key={cur.id} onDelete={() => onDelete(cur.id)} onSomethingChanged={onSomethingChanged}/>)
    }
    return (<div>
        {ans}
    </div>)
}
export class Recipe extends Component {
    constructor(props){
        super(props)
        this.state = {json:null, onDelete:null, onSomethingChanged:null}
        this.state.json = props.json
        this.state.onDelete = props.onDelete
        this.state.onSomethingChanged = props.onSomethingChanged
        this.changeName = this.changeName.bind(this)
        this.addTaste = this.addTaste.bind(this)
        this.deleteTaste = this.deleteTaste.bind(this)
        this.addIngredient = this.addIngredient.bind(this)
        this.deleteIngredient = this.deleteIngredient.bind(this)
        this.deleteCoeficients = this.deleteCoeficients.bind(this)
        this.onTasteChanged = this.onTasteChanged.bind(this)
        this.onIngredientChanged = this.onIngredientChanged.bind(this)
    }
    onIngredientChanged(json) {
        let prev = this.state
        for (let i = 0; i < prev.json.default_measures.length; i++) {
            if (prev.json.default_measures[i].id === json.id) {
                prev.json.default_measures[i] = json
            }
        }
        this.setState(prev)
        this.state.onSomethingChanged(this.state.json)
    }
    onTasteChanged(json) {
        let prev = this.state
        for (let i = 0; i < prev.json.tastes.length; i++) {
            if (prev.json.tastes[i].id === json.id) {
                prev.json.tastes[i] = json
            }
        }
        this.setState(prev)
        this.state.onSomethingChanged(this.state.json)
    }
    changeName(event){
        var prevState = this.state
        prevState.json.name = event.target.value
        this.setState(prevState)
        this.state.onSomethingChanged(this.state.json)
    }
    deleteTaste(key){  
        let prev = this.state
        prev.json.tastes = prev.json.tastes.filter(el => el.id !== key)
        this.setState(prev) 
        this.state.onSomethingChanged(this.state.json)
    }
    addTaste(){
        let prev = this.state
        if (prev.json.tastes.length === 0) {
            prev.json.tastes.push({"id": 0, "name": ""})
        }
        else {
            let ind = prev.json.tastes[prev.json.tastes.length - 1].id + 1
            prev.json.tastes.push({"id": ind, "name": ""})
        }
        this.setState(prev)
        this.state.onSomethingChanged(this.state.json)
    }
    deleteIngredient(key){  
        let prev = this.state
        prev.json.default_measures = prev.json.default_measures.filter(el => el.id !== key)
        this.setState(prev) 
        this.state.onSomethingChanged(this.state.json)
    }
    addIngredient(){
        let prev = this.state
        if (prev.json.default_measures.length === 0) {
            prev.json.default_measures.push({"id": 0, "name": "", "value": 0})
        }
        else {
            let ind = prev.json.default_measures[prev.json.default_measures.length - 1].id + 1
            prev.json.default_measures.push({"id": ind, "name": "", "value": 0})
        }
        this.setState(prev)
        this.state.onSomethingChanged(this.state.json)
    }
    deleteCoeficients(key){
        let prev = this.state
        prev.json.change_coeficients = prev.json.change_coeficients.filter(el => el.id !== key)
        this.setState(prev)
        this.state.onSomethingChanged(this.state.json)
    }
    avaliableIngredients(){
        let prev = this.state.json.default_measures
        let ans = []
        for(let i = 0; i < prev.length; i++){
            ans.push(prev[i].name)
        }
        return ans
    }
    avaliableTastes(){
        let prev = this.state.json.tastes
        let ans = []
        for(let i = 0; i < prev.length; i++){
            ans.push(prev[i].name)
        }
        return ans
    }
    render() {
        return (
            <div className='recipe'>
            <label>
                <button onClick={this.state.onDelete} className='delete'>Удалить рецепт</button>
                <p>Имя рецепта</p>
                <textarea value={this.state.json.name} onChange={this.changeName} className='text-area'/>
            </label>
            <p>Вкусы</p>
            {showTastes(this.state, this.deleteTaste, this.onTasteChanged)}
            <button onClick={this.addTaste} className='add'>Добавить вкус</button>
            <p>Ингредиенты</p>
            {showMeasures(this.state, this.deleteIngredient, this.onIngredientChanged)}
            <button onClick={this.addIngredient} className='add'>Добавить ингредиент</button>
            </div>
        )
    }
}

export default Recipe