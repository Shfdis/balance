import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import { Elements } from "./components/Elements";
class App extends React.Component {
  constructor(props){
    super(props)
    
    this.state = {
      elements: [],
      APIUrl: "http://localhost:5000",
      container: []
    }
    this.loadData = this.loadData.bind(this)
    this.submit = this.submit.bind(this)
    this.choose = this.choose.bind(this)
  }
  componentDidMount(){
    this.loadData()
  }
  loadData(){
    let params = new URL(document.location.toString()).searchParams;
    let id = params.get("recipe_id").toString();
    let container = []
    fetch(this.state.APIUrl + "/tastes/" + id)
    .then(response => response.json())
    .then(data => {
      for (let i = 0; i < data.length; i++) { 
        data[i] = data[i].name
        container[i] = 0
      }
      this.setState({elements: data, container: container})
    })
  }
  submit(){
    var result = {}
    for (var i = 0; i < this.state.elements.length; i++) {
      result[this.state.elements[i]] = (this.state.container[i] / 20)
    }
    let params = new URL(document.location.toString()).searchParams;
    let token = params.get("token").toString();
    fetch(this.state.APIUrl + "/submit/" + token, {
      method: "POST",
      body: JSON.stringify(result),
      headers: {
          "Content-Type": "application/json"
      }
    });
  }
  render(){
    return (
      <div className="wrapper">
          <Header />
          <Elements elements={this.state.elements} choose={this.choose}/>
          <button className="submit" onClick={this.submit}>Отправить</button>
          <Footer />
        </div>
    );
  }
  choose(value, name){
    this.state.container[name] = value
  }
}
export default App;
