import React, { useState, useEffect } from "react";

interface SelectInputProps {
  className?: string;
  label?: string;
  value?: string | number;
  children: React.ReactNode;
  disabled?: boolean;
  onChange?: (value: string | number) => void;
}

const SelectInput: React.FC<SelectInputProps> = ({
  className,
  label,
  value = "",
  children,
  disabled,
  onChange,
}) => {
  const [inputValue, setInputValue] = useState(value);

  useEffect(() => {
    setInputValue(value);
  }, [value]);

  const handleInputChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedValue = event.target.value;
    setInputValue(selectedValue);
    if (onChange) {
      onChange(selectedValue); 
    }
  };

  return (
    <div className={className}>
      {label && <label htmlFor="default-select-input" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">{label}</label>}
      <div className="relative">
        <select
          disabled={disabled}
          className="appearance-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 pr-10 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"
          id="default-select-input"
          value={inputValue}
          onChange={handleInputChange}
        >
          {children}
        </select>
        <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
          <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" /></svg>
        </div>
      </div>
    </div>
  );
};

export default SelectInput;
