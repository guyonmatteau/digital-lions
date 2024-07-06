import React from 'react';
import { Link, LinkProps } from 'react-router-dom';

interface NavLinkProps extends LinkProps {
  children: React.ReactNode;
  className?: string; // Optional className
}

const NavLink: React.FC<NavLinkProps> = ({ to, children, className, ...rest }) => {
  return (
    <Link
      to={to}
      className={`text-white hover:bg-gray-700 px-3 py-2 rounded-md text-sm font-medium ${className}`}
      {...rest}
    >
      {children}
    </Link>
  );
};

export default NavLink;
