import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    fontFamily: {
      sans: ['Work Sans', 'sans-serif'],
    },
    extend: {
      colors: {
        'button-primary': 'var(--color-button)',
        'button-secondary': 'var(--color-button-secondary)',
        'button-text': 'var(--color-button-text)',
        'background': 'var(--color-background)',
        'background-text': 'var(--color-background-text)',
        'footer-background': 'var(--color-footer-background)',
        'footer-text': 'var(--color-footer-text)',
        'card': 'var(--color-card)',
        'card-dark': 'var(--color-card-dark)',
        'card-secondary': 'var(--color-card-secondary)',
        'card-secondary-dark': 'var(--color-card-secondary-dark)',
        'card-text': 'var(--color-card-text)',
        'border': 'var(--color-border)',

        'primary-blue': 'var(--color-primary-blue)',
        'primary-blue-dark': 'var(--color-primary-blue-dark)',
        
        'primary': 'var(--color-primary)',
        'primary-dark': 'var(--color-primary-dark)',
        'secondary': 'var(--color-secondary)',
        'secondary-dark': 'var(--color-secondary-dark)',
        'success': 'var(--color-success)',
        'success-dark': 'var(--color-success-dark)',
        'error': 'var(--color-error)',
        'error-dark': 'var(--color-error-dark)',
        'warning': 'var(--color-warning)',
        'warning-dark': 'var(--color-warning-dark)',
        'neutral-light': 'var(--color-neutral-light)',

        'text-primary': 'var(--color-text)',
        'text-primary-light': 'var(--color-text-light)',
      },
    },
  },
  variants: {
    extend: {
      backgroundColor: ['hover'],
    },
  },
  plugins: [],
};
export default config;
