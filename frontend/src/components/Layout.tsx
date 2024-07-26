import React, { ReactNode } from 'react';
import Navigation from './Navigation';
import Footer from './Footer';
import Breadcrumbs from './Breadcrumbs'; // Import your Breadcrumbs component

interface LayoutProps {
  children: ReactNode;
  breadcrumbs?: { label: string; path?: string }[]; // Optional breadcrumbs prop
}

const Layout: React.FC<LayoutProps> = ({ children, breadcrumbs }) => {
  return (
    <div className="flex flex-col min-h-screen bg-background text-background-text">
      <Navigation />
      {/* Render Breadcrumbs if provided */}
      {breadcrumbs && (
        <div className="w-full bg-gray-50 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
          <div className="container mx-auto px-4 md:px-8 py-3">
            <Breadcrumbs breadcrumbs={breadcrumbs} />
          </div>
        </div>
      )}
      <main className="flex-1">
        <div className="container mx-auto px-4 md:px-8 py-8">
          <div className="grid grid-cols-12 gap-4">
            <div className="col-span-12 md:col-start-1 lg:col-span-8 xl:col-span-6">
              {children}
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default Layout;
