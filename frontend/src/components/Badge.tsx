import React, { ReactNode } from 'react';

// Define the possible variants
type BadgeVariant = 'primary' | 'secondary' | 'success' | 'danger' | 'warning';

// Define the props interface, including the type for `variant` and `children`
interface BadgeProps {
  variant?: BadgeVariant;
  className?: string;
  children: ReactNode;
}

// Map variants to corresponding classes
const badgeColors: Record<BadgeVariant, string> = {
  primary: 'bg-primary text-text-light',
  secondary: 'bg-secondary text-text-light',
  success: 'bg-success text-text-light',
  danger: 'bg-danger text-text-light',
  warning: 'bg-warning text-text-light',
};

const badgeHoverColors: Record<BadgeVariant, string> = {
  primary: 'hover:bg-primary-dark',
  secondary: 'hover:bg-secondary-dark',
  success: 'hover:bg-success-dark',
  danger: 'hover:bg-danger-dark',
  warning: 'hover:bg-warning-dark',
};

const Badge: React.FC<BadgeProps> = ({ children, variant = 'primary', className = '' }) => {
  const baseStyles = `inline-block px-3 py-1 text-sm font-semibold rounded-full transition-colors duration-200 ${className}`;
  const colorStyles = badgeColors[variant];
  const hoverStyles = badgeHoverColors[variant];

  return (
    <span className={`${baseStyles} ${colorStyles} ${hoverStyles}`}>
      {children}
    </span>
  );
};

export default Badge;
