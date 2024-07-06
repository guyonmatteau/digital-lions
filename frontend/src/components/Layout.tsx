import React, { ReactNode } from "react";
import Head from "next/head";
import { metadata } from "@/metadata/metadata";
import "@/styles/globals.css";
import Navigation from "./Navigation";
import Footer from "./Footer";

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <>
      <Head>
        <title>{metadata.title}</title>
        <meta name="description" content={metadata.description} />
      </Head>
      <div className="flex flex-col min-h-screen">
        <Navigation />
        <main className="flex-1">{children}</main>
        <Footer />
      </div>
    </>
  );
};

export default Layout;
