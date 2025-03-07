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
        this.state = {json: []}

        this.somethingChanged = this.somethingChanged.bind(this)
        this.sendData = this.sendData.bind(this)
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
                console.log(JSON.stringify(json))
                this.setState({json: json})
            })
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
    sendData(e) {
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