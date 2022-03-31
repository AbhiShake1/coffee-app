module.exports = {
	plugins: {
		tailwindcss: {},
		autoprefixer: {},
		cssnano: ctx => (ctx.env === 'production' ? {} : false),
	},
}
