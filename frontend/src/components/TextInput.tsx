import React, { useState, useEffect } from "react";

interface TextInputProps {
  className?: string;
  label?: string;
  value?: string;
  onChange?: (value: string) => void;
  onBlur?: (value: string) => void;
  required?: boolean;
  errorMessage?: string;
  placeholder?: string; // Added placeholder prop
}

const TextInput: React.FC<TextInputProps> = ({
  className,
  label,
  value = "",
  onChange,
  onBlur,
  required = false,
  errorMessage = "", 
  placeholder = "", // Added placeholder default value
}) => {
  const [inputValue, setInputValue] = useState(value);
  const [isTouched, setIsTouched] = useState(false); 

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
    setIsTouched(true); // Mark input as touched when it loses focus
    if (onBlur) {
      onBlur(inputValue);
    }
  };

  const showError = required && isTouched && !inputValue;

  return (
    <div className={className}>
      {label && (
        <label
          htmlFor="default-input"
          className="mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >
          {label}
        </label>
      )}
      <input
        type="text"
        id="default-input"
        value={inputValue}
        onChange={handleInputChange}
        onBlur={handleBlur}
        placeholder={placeholder} // Added placeholder attribute
        className={`bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 ${
          showError ? "border-red-500" : ""
        }`}
        required={required}
      />
      {showError && (
        <p className="text-red-500 text-sm mt-1">
          {errorMessage || "This field is required"}
        </p>
      )}
    </div>
  );
};

export default TextInput;
