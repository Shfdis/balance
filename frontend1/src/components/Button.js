import React, { Component } from 'react'

export class Button extends Component {
  render() {
    return (
      <div className={this.props.className} onClick={() => this.props.choose()}>
        <this.props.value/>
      </div>
      
    )
  }
}

export default Button