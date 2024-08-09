import React from "react";
import { useNavigate } from "react-router-dom";

interface LinkCardProps {
  title: string;
  className?: string;
  to: string; 
  state?: any; 
}

const LinkCard: React.FC<LinkCardProps> = ({
  title,
  className,
  to,
  state, 
}) => {
  const navigate = useNavigate();

  const handleClick = () => {
    if (state) {
      localStorage.setItem('linkCardState', JSON.stringify(state));
    }
    navigate(to, { state }); 
  };

  return (
    <div
      onClick={handleClick}
      className={`${className} rounded-lg bg-card flex items-center justify-between w-full p-5 font-medium text-white hover:bg-card-dark dark:hover:bg-gray-800 transition-colors cursor-pointer`}
    >
      <div className="flex-1">
        <h2 className="flex items-center">{title}</h2>
      </div>
      <svg
        className="w-3 h-3 transition-transform"
        aria-hidden="true"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 6 10"
      >
        <path
          stroke="currentColor"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M1 1l4 4-4 4"
        />
      </svg>
    </div>
  );
};

export default LinkCard;
