import React, { Component } from 'react'
import RecipeCoefs from '../Components/RecipeCoefs'
function showRecipesCoefs(props, onSomethingChanged) {
    return (<div>
        {props.json.map(el => (
            <RecipeCoefs json={el} key={el.id} tastes={el.tastes} onSomethingChanged={onSomethingChanged}/>
        ))}
    </div>)
}
export class Coef extends Component {
    constructor(props){
        super(props)
        this.state = {json: null}
        this.state.json = [{
            id: 0,
            name: "espresso", 
            tastes: [{id: 0, name: "bitter"}, {id: 1, name: "sour"}, {id: 2, name: "strong"}],
            default_measures: [{id: 0, name: "ground_coffee", value: 18}, {id: 1, name: "water", value: 36}],
            change_coeficients: [{id: 0, name: "ground_coffee", tastes: [{id: 0,name: "bitter", value: 1}]}]
        }]
        this.somethingChanged = this.somethingChanged.bind(this)
        this.sendData = this.sendData.bind(this)
    }    
    somethingChanged(json) {
        let prev = this.state
        for (let i = 0; i < prev.json.length; i++) {
            if (prev.json[i].id === json.id) {
                prev.json[i] = json
                break
            }
        }
        this.setState(prev)
        console.log(JSON.stringify(this.state.json))
    }
    sendData() {
        // rest request
        console.log(JSON.stringify(this.state.json))
    }
    render() {
        return (
            <div>
                {showRecipesCoefs(this.state, this.somethingChanged)}
                <form onSubmit={this.sendData}>
                    <input type="submit" className='submit' />
                </form>
            </div>
        
        )
    }
}

export default Coef