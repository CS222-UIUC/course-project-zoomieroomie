const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/login',
    createProxyMiddleware({
      target: 'http://127.0.0.1:5000',
      changeOrigin: true,
      onProxyReq: (proxyReq, req, res) => {
        console.log('Incoming request:', req.url);
        console.log('Target server:', proxyReq._headers.host);
      }
    })
  );
};
