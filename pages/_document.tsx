import Document, { Head, Html, Main, NextScript } from 'next/document';

class MyDocument extends Document {
  render() {
    return (
      <Html lang="en">
        <Head>
          <link rel="icon" href="/favicon.ico" />
          <meta
            name="description"
            content="Get your new home ideas in seconds."
          />
          <meta property="og:site_name" content="home-ai-advisor.vercel.app" />
          <meta
            property="og:description"
            content="Get your new home ideas in seconds."
          />
          <meta property="og:title" content="AI Home Advisor" />
          <meta name="twitter:card" content="summary_large_image" />
          <meta name="twitter:title" content="AI Home Advisor" />
          <meta
            name="twitter:description"
            content="Get your new home ideas in seconds."
          />
          <meta
            property="og:image"
            content="https://home-ai-advisor.vercel.app/og-image.png"
          />
          <meta
            name="twitter:image"
            content="https://home-ai-advisor.vercel.app/og-image.png"
          />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;
