import React, { Component } from 'react'
export class LoginPage extends Component {
    constructor(props){
        super(props)
        this.state = {password: ""}
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.checkPassword = this.checkPassword.bind(this)
    }
    handleChange(event){
        this.setState({password: event.target.value})
    }
    handleSubmit(event){
        if (this.checkPassword()){
            event.preventDefault();
            window.open("home?password=" + this.state.password, "_self")
        }
        else{
            alert("Неверный пароль")
        }
    }
    checkPassword(){
        return this.state.password === "6321"
    }
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
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