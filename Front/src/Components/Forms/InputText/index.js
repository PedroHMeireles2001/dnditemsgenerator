import React from 'react'
import styles from './InputText.module.css'

export default function InputText({onChange,placeholder}) {
  return (
    <input placeholder={placeholder} onChange={(e)=>{onChange(e.target.value)}} type='text' className={styles.text} />
  )
}
