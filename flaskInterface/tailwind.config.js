/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      height: {
        '128': '120px',
      },
      fontFamily:{
        itali :['Montserrat Alternates'],
        oswad:['Oswald'],
        patrick:['Patrick Hand']
      }
    },
  },
  plugins: [],
}
