import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    host: process.env.VITE_APP_HOST || 'localhost',  // Use the environment variable or fallback to localhost
  },
});
