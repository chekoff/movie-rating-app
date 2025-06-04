
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    host: true, // Accept external connections
    strictPort: true,
    allowedHosts: 'all' // Allow Gitpod or any hostname
  }
});
