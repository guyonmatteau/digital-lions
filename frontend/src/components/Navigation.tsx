// components/Navigation.tsx
import React, { useState } from 'react';
import NavLink from './NavLink';

const Navigation: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(prevState => !prevState);
  };

  return (
    <nav className="bg-gray-800 p-4">
      <div className="max-w-7xl mx-auto">
        <div className="flex items-center justify-between">
          {/* Logo and Title */}
          <div className="flex-shrink-0">
            <NavLink href="/" className="text-white font-bold text-xl">
              Digital Lions
            </NavLink>
          </div>

          {/* Desktop Navigation Links */}
          <div className="hidden md:flex space-x-4">
            <NavLink href="/communities">Community</NavLink>
            {/* <NavLink href="/teams" includeSourceMenu={true}>Teams info</NavLink> */}
            <NavLink href="/attendance">Attendance</NavLink>
          </div>

          {/* Mobile Hamburger Menu Button */}
          <div className="md:hidden">
            <button
              className="text-white hover:text-gray-300 focus:outline-none"
              onClick={toggleMenu}
            >
              <svg
                className="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                {isOpen ? (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M6 18L18 6M6 6l12 12"
                  />
                ) : (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                )}
              </svg>
            </button>
          </div>
        </div>

        {/* Mobile Menu Links */}
        {isOpen && (
          <div className="md:hidden mt-4 space-y-2">
            <NavLink href="/communities" onClick={toggleMenu}>
              Community
            </NavLink>
            {/* <NavLink href="/teams" includeSourceMenu={true} onClick={toggleMenu}>
              Teams info
            </NavLink> */}
            <NavLink href="/attendance" onClick={toggleMenu}>Attendance</NavLink>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navigation;
