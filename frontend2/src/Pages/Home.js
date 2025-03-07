import React, { Component } from 'react'
import Recipe from '../Components/Recipe'
function showRecipes (props, onDelete, somethingChanged) {
    return (<div>
        {props.json.map(el => (
            <Recipe json={el} key={el.id} onDelete={() => onDelete(el.id)} onSomethingChanged={(val) => somethingChanged(val)}/>
        ))}
    </div>)
}

export class Home extends Component {
    constructor(props){
        super(props)
        this.state = {json: []}
        this.state.json = []     
        this.recipeAccess = []
        this.addRecipe = this.addRecipe.bind(this)
        this.deleteRecipe = this.deleteRecipe.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.somethingChanged = this.somethingChanged.bind(this)
        this.loadData = this.loadData.bind(this)
    }
    componentDidMount() {
        this.loadData()
    }

    loadData(){
        let params = new URL(document.location.toString()).searchParams;
        let password = params.get("password").toString();
        fetch(this.props.APIUrl + "/recipes?password=" + password)
            .then(response => response.json())
            .then(json => {
                console.log(json)
                this.setState({json: json})
            })
    }
    handleSubmit(e) {
        e.preventDefault()
        let params = new URL(document.location.toString()).searchParams;
        let password = params.get("password").toString();
        fetch(this.props.APIUrl + "/recipes?password=" + password, {
            method: "POST",
            body: JSON.stringify(this.state.json),
            headers: {
                "Content-Type": "application/json"
            }
          });
        
        console.log(JSON.stringify(this.state.json))
        window.open("/coef" + "?password=" + password, "_self")
    }

    somethingChanged(json) {
        let prev = this.state
        for (let i = 0; i < prev.json.length; i++) {
            if (prev.json[i].id === json.id) {
                prev.json[i] = json
            }
        }
        this.setState(this.state)
        console.log(JSON.stringify(this.state.json))
    }
    deleteRecipe(key){  
        let prev = this.state
        prev.json = prev.json.filter(el => el.id !== key)
        this.setState(prev) 
    }
    addRecipe(){
        let prev = this.state
        let len = prev.json.length
        if (len === 0) {
            prev.json[len] = {
                id: 0,
                name: "", 
                tastes: [],
                default_ingredients: [],
                change_coeficients: []}
        } else {
            prev.json[len] = {
                id: prev.json[len - 1].id + 1,
                name: "", 
                tastes: [],
                default_ingredients: [],
                change_coeficients: []}
        }
        this.setState(prev)
    }
    render() {
        return (
        <div>
        {showRecipes(this.state, this.deleteRecipe, this.somethingChanged)}
        <button onClick={this.addRecipe} className='add'>Добавить рецепт</button>
        <form onSubmit={this.handleSubmit}>
            
            <input type='submit' className='submit'></input>
        </form>
        </div>
        )
    }
}

export default Home