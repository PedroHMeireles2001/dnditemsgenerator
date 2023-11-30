import React from 'react'
import styles from './Button.module.css'

export default function Button({text, onClick}) {
  return (
    <button onClick={(e)=>onClick(e)} className={styles.button}>{text}</button>
  )
}
