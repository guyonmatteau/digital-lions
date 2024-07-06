import React, { useState } from "react";

interface AccordionProps {
  title: string;
  description: string;
  children: React.ReactNode;
}

const Accordion: React.FC<AccordionProps> = ({
  title,
  description,
  children,
}) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleAccordion = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div id="accordion-open" data-accordion="open">
      <h2 id="accordion-open-heading-1">
        <button
          onClick={toggleAccordion}
          type="button"
          className="bg-white flex items-center justify-between w-full p-5 mt-2 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3"
          data-accordion-target="#accordion-open-body-1"
          aria-expanded={isOpen}
          aria-controls="accordion-open-body-1"
        >
          <span className="flex items-center">{title}</span>
          <svg
            data-accordion-icon
            className={`w-3 h-3 ${!isOpen ? "rotate-180" : ""} shrink-0`}
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 10 6"
          >
            <path
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M9 5 5 1 1 5"
            />
          </svg>
        </button>
      </h2>
      <div
        id="accordion-open-body-1"
        className={`${isOpen ? "" : "hidden"}`}
        aria-labelledby="accordion-open-heading-1"
      >
        <div className="p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900">
          <p className="mb-2 text-gray-500 dark:text-gray-400">{description}</p>
          {children}
        </div>
      </div>
    </div>
  );
};

export default Accordion;
