import React, { useState } from 'react';
import styles from './Dropdown.module.css';

const Dropdown = ({ options, onSelect,label }) => {
  const [selectedOption, setSelectedOption] = useState(null);

  const handleSelect = (option) => {
    setSelectedOption(option);
    onSelect(option);
  };

  return (
    <div className={styles.dropdown}>
        <span>{label}</span>
      <select value={selectedOption} onChange={(e) => handleSelect(e.target.value)} className={styles.select}>
        <option value="" disabled>Select an option</option>
        {options.map((option) => (
          <option key={option} value={option}>{option}</option>
        ))}
      </select>
    </div>
  );
};

export default Dropdown;
