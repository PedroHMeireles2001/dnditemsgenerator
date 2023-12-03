import React, { useState } from 'react';
import styles from "./Switch.module.css"

const Switch = ({onToggle,initialState,label}) => {
  const [isChecked, setChecked] = useState(initialState);

  const toggleSwitch = () => {
    if (onToggle){
        onToggle(!isChecked)
    }
    setChecked(!isChecked);
  };

  return (
    <div className={styles.container}>
      <label className={styles.switch}>
        <input type="checkbox" checked={isChecked} onChange={toggleSwitch} />
        <span className={styles.slider}></span>
      </label>
      <span className={styles.switchlabel}>{isChecked ? label[0] : label[1]}</span>
    </div>
  );
};
export default Switch;