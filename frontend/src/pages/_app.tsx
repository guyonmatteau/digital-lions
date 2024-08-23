import type { AppProps } from 'next/app';
import '@/styles/globals.css'
import 'tailwindcss/tailwind.css';
import '@radix-ui/themes/styles.css';

function MyApp({ Component, pageProps }: AppProps) {
  return (
      <Component {...pageProps} />
  );
}

export default MyApp;
