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
        'card-dark': 'var(--color-card-dark)',
        'card-secondary-dark': 'var(--color-card-secondary-dark)',
        'primary-dark': 'var(--color-primary-dark)',
        'secondary-dark': 'var(--color-secondary-dark)'
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
