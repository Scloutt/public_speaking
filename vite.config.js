import { defineConfig } from "vite";
import path from "path";

export default defineConfig({
  root: path.resolve(__dirname, "static/src"),
  base: "/",
  build: {
    outDir: path.resolve(__dirname, "static/dist"),
    emptyOutDir: true,
    assetsDir: ".",
    rollupOptions: {
      input: path.resolve(__dirname, "static/src/main.js"),
      output: {
        entryFileNames: "main.js",
        chunkFileNames: "[name].js",
        assetFileNames: "[name].[ext]"
      }
    }
  }
});
