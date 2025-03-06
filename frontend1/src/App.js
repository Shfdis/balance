import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import { Elements } from "./components/Elements";
var container = []

class App extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      elements: [
        "горький", "сладкий", "кислый"
      ]
    }
    for (var i = 0; i < this.state.elements.length; i++) {
      container[i] = 0
    }
  }
  render(){
    return (
      <div className="wrapper">
          <Header />
          <Elements elements={this.state.elements} choose={this.choose}/>
          <Footer />
        </div>
    );
  }
  choose(value, name){
    container[name] = value
  }
}
export default App;
