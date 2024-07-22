import React, { useState, useEffect } from "react";

interface TextInputProps {
  className?: string;
  label?: string;
  value?: string;
  onChange?: (value: string) => void;
  onBlur?: (value: string) => void;
}

const TextInput: React.FC<TextInputProps> = ({
  className,
  label,
  value = "",
  onChange,
  onBlur,
}) => {
  const [inputValue, setInputValue] = useState(value);

  // Update local state when value prop changes
  useEffect(() => {
    setInputValue(value);
  }, [value]);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
    if (onChange) {
      onChange(event.target.value); 
    }
  };

  const handleBlur = () => {
    if (onBlur) {
      onBlur(inputValue);
    }
  };

  return (
    <div className={className}>
      <label
        htmlFor="default-input"
        className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
      >
        {label}
      </label>
      <input
        type="text"
        id="default-input"
        value={inputValue}
        onChange={handleInputChange}
        onBlur={handleBlur}
        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      />
    </div>
  );
};

export default TextInput;
