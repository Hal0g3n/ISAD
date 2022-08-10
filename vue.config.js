const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
    publicPath: process.env.NODE_ENV == "production" ? "/ISAD/" : "/",
    lintOnSave: false,
    transpileDependencies: [
      "vuetify"
    ],
    chainWebpack: (config) => {
        config.module
        .rule("ts")
        .use("ts-loader")
        .loader("ts-loader");
    },
});
