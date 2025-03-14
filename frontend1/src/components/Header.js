import React from 'react'
import { GiScales } from "react-icons/gi";
export default function Header() {
    return (
      <header>
        <div className='logo2'>
            <span className='logo'>Balance</span>
            <GiScales className='libra-icon' />
            </div>
            <div className='presentation'></div>
      </header>
    )
}
