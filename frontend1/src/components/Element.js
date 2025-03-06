import React, { Component, useState } from 'react'
import { RiArrowDownDoubleLine } from "react-icons/ri";
import { RiArrowDownSLine } from "react-icons/ri";
import { IoMdCheckmark } from "react-icons/io";
import { RiArrowUpSLine } from "react-icons/ri";
import { RiArrowUpDoubleLine } from "react-icons/ri";
import Button from './Button';
export class Element extends Component {
    constructor(props) {
        super(props)
        this.state ={active: 0}
        this.choose.bind(this)
    }
    choose(val) {
        this.props.choose(val)
        this.setState((prevState) => ({active: val}))
    }
    render() {        
        return (
            <div className='element'>
                <p>{this.props.element}</p>
                <Button value={RiArrowDownDoubleLine} className={`button${this.state.active===-2 && '-active'}`} choose={() => this.choose(-2)}/>
                <Button value={RiArrowDownSLine} className={`button${this.state.active===-1 && '-active'}`} choose={() => this.choose(-1)}/>
                <Button value={IoMdCheckmark} className={`button${this.state.active===0 && '-active'}`} choose={() => this.choose(0)}/>
                <Button value={RiArrowUpSLine} className={`button${this.state.active===1 && '-active'}`} choose={() => this.choose(1)}/>
                <Button value={RiArrowUpDoubleLine} className={`button${this.state.active===2 && '-active'}`} choose={() => this.choose(2)}/>
            </div>
        )
        
    }
    
}

export default Element