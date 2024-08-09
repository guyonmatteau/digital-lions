import React from 'react';
import { Link } from 'react-router-dom';

interface Breadcrumb {
  label: string;
  path?: string;
}

interface BreadcrumbsProps {
  breadcrumbs: Breadcrumb[];
}

const Breadcrumbs: React.FC<BreadcrumbsProps> = ({ breadcrumbs }) => {
  return (
    <nav
      aria-label="Breadcrumb"
      className="flex py-3 text-gray-700 "
    >
      <ol className="inline-flex items-center">
        {breadcrumbs.map((breadcrumb, index) => (
          <li key={index} className="inline-flex items-center">
            {breadcrumb.path ? (
              <Link
                to={breadcrumb.path}
                className="inline-flex items-center text-sm font-medium text-gray-700 dark:text-white hover:text-blue-600 dark:hover:text-white"
              >
                {breadcrumb.label}
              </Link>
            ) : (
              <span className="text-sm font-medium text-gray-500">
                {breadcrumb.label}
              </span>
            )}
            {index < breadcrumbs.length - 1 && (
              <svg
                className="w-3 h-3 mx-1 text-gray-400 dark:text-white"
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
                  d="m1 9 4-4-4-4"
                />
              </svg>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
};

export default Breadcrumbs;
