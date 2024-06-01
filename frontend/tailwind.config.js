/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
          'custom-gradient': 'linear-gradient(to right top, #27272b, #2c2e4f, #2c3674, #273c9a, #1d42c2, #1d42c2, #1d42c2, #1d42c2, #273c9a, #2c3674, #2c2e4f, #27272b)',
          "box-gradient": "linear-gradient(to right bottom, #222324, #003354, #004289, #004bbd, #124ceb)",
          'innerbox-gradient':'linear-gradient(to left top, #222324, #0f2c45, #003368, #00378a, #0b35a7)'
      },
      blur: {
        '4xl': '80px',
        '5xl': '100px',
      },
    },
  },
  plugins: [],
};
