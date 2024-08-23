// next.config.mjs
export default {
  async redirects() {
    return [
      {
        source: "/",
        destination: "/communities",
        permanent: true, // Permanent redirect (HTTP 301)
      },
    ];
  },
};
