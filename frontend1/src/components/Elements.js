import React, { Component } from 'react'
import Element from './Element'
export class Elements extends Component {
  render() {
    return (
      <main>
        {this.createElements()}
      </main>
    )
  }
  createElements(){
    let arr = []    
    for(let i = 0; i < this.props.elements.length; i++){
        arr[i] = <Element key={this.props.elements[i]} element={this.props.elements[i]} 
        choose={(value) => this.props.choose(value, i)}/>
    }
    return arr
  }
}

export default Elements