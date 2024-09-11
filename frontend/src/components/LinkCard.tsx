import React from "react";
import { useRouter } from "next/router";

interface LinkCardProps {
  title: string;
  className?: string;
  href: string;
  state?: { communityName?: string | null; teamName?: string | null };
  children?: React.ReactNode;
}

const LinkCard: React.FC<LinkCardProps> = ({ title, className, href, state, children }) => {
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
      <div className="flex flex-row items-center w-full">
        {/* Title on the left */}
        <h2 className="flex items-center">{title}</h2>

        {children ? (
          <div className="ml-4 flex-1">
            {children}
          </div>
        ) : (
          <div className="flex-1"></div> 
        )}

        <svg
          className="w-3 h-3 transition-transform ml-2"
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
    </div>
  );
};

export default LinkCard;
