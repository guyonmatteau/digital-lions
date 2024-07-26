import React from 'react';
import { Link, LinkProps } from 'react-router-dom';

interface NavLinkProps extends LinkProps {
  children: React.ReactNode;
  className?: string;
  includeSourceMenu?: boolean; // New prop to include source=menu in the query parameters
}

const NavLink: React.FC<NavLinkProps> = ({ to, children, className, includeSourceMenu = false, ...rest }) => {
  const urlWithQuery = includeSourceMenu ? `${to}?source=menu` : to;

  return (
    <Link
      to={urlWithQuery}
      className={`text-white hover:bg-gray-700 px-3 py-2 rounded-md text-sm font-medium ${className}`}
      {...rest}
    >
      {children}
    </Link>
  );
};

export default NavLink;
