import React, { useState } from "react";
import * as Accordion from "@radix-ui/react-accordion";
import { ChevronDownIcon, ChevronUpIcon } from "@radix-ui/react-icons";
interface AccordionProps {
  title: string;
  description?: string;
  className?: string;
  children: React.ReactNode;
}

const CustomAccordion: React.FC<AccordionProps> = ({
  title,
  description,
  children,
  className,
}) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <Accordion.Root
      type="single"
      collapsible
      className={`${className} border border-border rounded-xl overflow-hidden`}
    >
      <Accordion.Item value="item-1">
        <Accordion.Header className="bg-card">
          <Accordion.Trigger
            onClick={toggleMenu}
            className="flex items-center justify-between w-full p-5 font-medium text-card-text border-b border-border focus:ring-4 focus:ring-background gap-3 transition-all duration-300"
          >
            <span className="flex items-center">{title}</span>
            {isOpen ? (
              <ChevronUpIcon className="AccordionChevron" aria-hidden />
            ) : (
              <ChevronDownIcon className="AccordionChevron" aria-hidden />
            )}
          </Accordion.Trigger>
        </Accordion.Header>
        <Accordion.Content className="bg-card p-5">
          {children}
        </Accordion.Content>
      </Accordion.Item>
    </Accordion.Root>
  );
};

export default CustomAccordion;
