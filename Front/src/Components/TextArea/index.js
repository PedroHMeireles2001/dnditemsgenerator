import React from 'react'
import styles from './TextArea.module.css'
export default function TextArea({text,title}) {
  return (
    <>
        <h3>{title}</h3>
        <textarea className={styles.textarea} readOnly >{text}</textarea>
    </>
  )
}
