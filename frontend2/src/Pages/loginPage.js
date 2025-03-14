import React, { Component } from 'react'
function fetchAPI(event, param, callback) {
    event.preventDefault();
    // param is a highlighted word from the user before it clicked the button
    fetch(param)
        .then(response => {
            callback(response.status === 200)
        })
        .catch(function (error) {
            console.log(error);
        })
}
export class LoginPage extends Component {
    constructor(props){
        super(props)
        this.state = {password: ""}
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.state.URL = props.APIUrl
    }
    handleChange(event){
        this.setState({password: event.target.value})
    }
    handleSubmit(password){
        if (password){
            window.open("home?password=" + this.state.password, "_self")
        }
        else{
            alert("Неверный пароль")
        }
    }

    render() {
        return (
            <form onSubmit={(event) => fetchAPI(event, this.state.URL + "/recipes?password=" + this.state.password, this.handleSubmit)}>
                <label>
                    <h2>Введите пароль </h2>
                    <textarea value={this.state.value} onChange={this.handleChange} className='text-area'/>
                </label>
                <input type='submit' value="Отправить" className='submit' />
            </form>
        )
    }
}

export default LoginPage