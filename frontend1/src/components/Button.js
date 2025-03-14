import React, { Component } from 'react'

export class Button extends Component {
  render() {
    return (
      <div className={this.props.className} onClick={() => this.props.choose()}>
        <div className='icon'><this.props.value/></div>
      </div>
    )
  }
}

export default Button