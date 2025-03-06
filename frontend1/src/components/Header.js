import React, { useState } from 'react'
import { GiScales } from "react-icons/gi";
export default function Header() {
    return (
      <header>
        <div>
            <span className='logo'>Balance</span>
            <GiScales className='shop-cart-button' />
            </div>
            <div className='presentation'></div>
      </header>
    )
}
