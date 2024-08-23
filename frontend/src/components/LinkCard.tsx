import React from "react";
import { useRouter } from "next/router";

interface LinkCardProps {
  title: string;
  className?: string;
  href: string;
  state?: any;
}

const LinkCard: React.FC<LinkCardProps> = ({ title, className, href, state }) => {
  const router = useRouter();

  const handleClick = () => {
    if (state) {
      localStorage.setItem("linkCardState", JSON.stringify(state));
    }
    router.push(href); // Navigate to the href
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
