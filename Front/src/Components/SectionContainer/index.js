import React from 'react'
import styles from './SectionContainer.module.css'

export default function SectionContainer({children}) {
  return (
    <section className={styles.container}>{children}</section>
  )
}
