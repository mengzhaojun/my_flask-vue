module.exports = {
    // 基本路径
    // baseUrl: './',
    // publicPath: '/',
    publicPath: process.env.NODE_ENV === "production" ? '/my-vue-admin/' : "/",
    outputDir: './../flask-dist',
    // 生产环境是否生成 sourceMap 文件
    productionSourceMap: false,
    // 服务器端口号
    devServer: {
        port: 7001,
    },
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:5000', //后端运行端口
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                  '^/api': ''
                }
            }
        }
    }
}