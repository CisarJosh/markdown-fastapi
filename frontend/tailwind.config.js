module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
  ],
  // purge: [
  //   "./components/**/*.{vue,js,ts}",
  //   "./layouts/**/*.vue",
  //   "./pages/**/*.vue",
  //   "./plugins/**/*.{js,ts}",
  //   "./nuxt.config.{js,ts}",
  // ],
  // darkMode: false, // or 'media' or 'class'
  // https://devdojo.com/tnylea/custom-animations-in-tailwindcss
  theme: {
    extend: {
      backgroundImage: {
        "hero-pattern": "url('@/assets/poudre.canyon.svg')",
      },
      keyframes: {
        "fade-in": {
          "0%": {
            opacity: "0",
          },
          "100%": {
            opacity: "1",
          },
        },
        "fade-out": {
          from: {
            opacity: "1",
          },
          to: {
            opacity: "0",
          },
        },
      },
      animation: {
        "fade-in": "fade-in 0.5s ease-out",
        "fade-out": "fade-out 0.5s ease-out",
      },
    },
  },
  variants: {
    extend: {},
  },
  // plugins: [require("@tailwindcss/typography"), require("@tailwindcss/forms")],
}
