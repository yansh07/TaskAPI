// tailwind.config.js
export default {
  content: [
    "./templates/*.html",  
    "./static/styles/*.css",
  ],
  theme: {
    extend: {},
  },
  experimental: {
    optimizeUniversalDefaults: false,
  }
}
