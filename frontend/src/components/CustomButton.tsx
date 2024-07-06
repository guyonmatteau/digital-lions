import React, { useState } from "react";

interface CustomButtonProps {
  label: string;
  onClick?: () => void;
  className?: string;
  isLoading?: boolean;
  isDisabled?: boolean;
  variant?:
    | "primary"
    | "secondary"
    | "success"
    | "danger"
    | "warning"
    | "outline"
    | "none"; // Added variant prop
}

const CustomButton: React.FC<CustomButtonProps> = ({
  label,
  onClick,
  className,
  isLoading,
  isDisabled,
  variant = "primary",
}) => {
  const [loading, setLoading] = useState(false);

  const handleClick = () => {
    if (onClick && !loading) {
      setLoading(true);
      onClick();
      // Example: Simulate async action with setTimeout
      setTimeout(() => {
        setLoading(false);
      }, 1000); // Replace with actual async action
    }
  };

  // Define classes based on variant prop
  let buttonClass =
    "relative text-white font-bold py-2 px-4 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500";
  let buttonColorClass = "bg-green-500 hover:bg-green-700";
  let textColorClass = "text-white";
  let borderColorClass = "border-transparent";

  switch (variant) {
    case "primary":
      buttonColorClass = "bg-blue-500 hover:bg-blue-700";
      break;
    case "secondary":
      buttonColorClass = "bg-gray-500 hover:bg-gray-700";
      break;
    case "success":
      buttonColorClass = "bg-green-500 hover:bg-green-700";
      break;
    case "danger":
      buttonColorClass = "bg-red-500 hover:bg-red-700";
      break;
    case "warning":
      buttonColorClass = "bg-yellow-500 hover:bg-yellow-700";
      break;
    case "outline":
      buttonColorClass = "hover:bg-gray-200";
      textColorClass = "text-gray-700";
      borderColorClass = "border-gray-500";
      break;
    case "none":
      buttonColorClass = "";
      break;
    default:
      break;
  }

  return (
    <button
      type="button"
      className={`${buttonClass} ${buttonColorClass} ${textColorClass} ${borderColorClass} relative flex items-center justify-center rounded-lg px-4 py-2 text-white ${className}`}
      onClick={handleClick}
      disabled={isLoading || isDisabled}
      style={{ minWidth: "8rem", minHeight: "2.5rem" }}
    >
 {isLoading ? (
                <div className="absolute inset-0 flex items-center justify-center">
           <svg className="h-5 w-5 animate-spin text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
    </svg>
                </div>
            ) : (
                label
            )}
        </button>
  );
};

export default CustomButton;
