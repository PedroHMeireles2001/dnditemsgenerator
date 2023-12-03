import React, { useState } from 'react';
import styles from './Slider.module.css';

const Slider = ({label,initial,max,min,onChange}) => {
  const [sliderValue, setSliderValue] = useState(initial);

  const handleSliderChange = (event) => {
    onChange(event.target.value)
    setSliderValue(event.target.value);
  };

  return (
    <div className={styles.sliderContainer}>
        <p>{label}</p>
      <input
        type="range"
        min={min}
        max={max}
        value={sliderValue}
        onChange={handleSliderChange}
        className={styles.sliderInput}
        step="0.01"
      />
      <input type='number' value={sliderValue} className={styles.value} onChange={handleSliderChange} step="0.01" />
    </div>
  );
};

export default Slider;
