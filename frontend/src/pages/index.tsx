import React, { useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import App from '@/App';

const HomePage: React.FC = () => {
  useEffect(() => {
    const root = createRoot(document.getElementById('root') as HTMLElement);
    root.render(
      <React.StrictMode>
        <App />
      </React.StrictMode>
    );

    return () => {
      root.unmount();
    };
  }, []);

  return <div id="root"></div>; // Placeholder div for the client-side render
};

export default HomePage;
