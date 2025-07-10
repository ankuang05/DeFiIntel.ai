"use client";
import { motion } from "framer-motion";

export default function About() {
  return (
    <div className="w-full min-h-[80vh] flex flex-col items-center bg-white px-4 py-24 font-sans" style={{ fontFamily: 'Inter, Geist, Segoe UI, Arial, sans-serif' }}>
      <div className="w-full max-w-4xl flex flex-col gap-16 items-center">
        <motion.h1
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.7 }}
          transition={{ duration: 0.7 }}
          className="text-5xl md:text-6xl font-extrabold text-black text-center mb-8"
        >
          About DeFiIntel.ai
        </motion.h1>
        <motion.section
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ delay: 0.1, duration: 0.7 }}
          className="w-full"
        >
          <h2 className="text-2xl md:text-3xl font-bold text-black mb-4 text-left">What is DeFiIntel.ai?</h2>
          <p className="text-lg text-black mb-8 text-left">
            DeFiIntel.ai is an open-source DeFi fraud detection dashboard. It empowers users to analyze wallets, tokens, and social sentiment across multiple blockchains, integrating APIs like Helius, Etherscan, GeckoTerminal, and Twitter. The platform features ML-based fraud detection, wallet/token analytics, and a modern, minimal frontend built with Next.js and a Streamlit backend.
          </p>
        </motion.section>
        <motion.section
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ delay: 0.2, duration: 0.7 }}
          className="w-full"
        >
          <h2 className="text-2xl md:text-3xl font-bold text-black mb-4 text-left">What We Did</h2>
          <ul className="list-disc pl-8 text-black text-lg space-y-3 text-left">
            <li>Designed a clean, minimal, black-and-white UI with modern navigation and smooth scroll animations.</li>
            <li>Integrated on-chain and social APIs (Helius, Etherscan, GeckoTerminal, Twitter) for real-time analytics.</li>
            <li>Implemented wallet and token feature extraction for fraud detection and risk scoring.</li>
            <li>Added ML-based fraud detection using behavioral, temporal, and social features.</li>
            <li>Built a modular Next.js frontend and Streamlit backend for extensibility and rapid development.</li>
            <li>Created demo, docs, and blog pages with consistent aesthetics and navigation.</li>
          </ul>
        </motion.section>
        <motion.section
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ delay: 0.3, duration: 0.7 }}
          className="w-full flex flex-col items-center mt-4"
        >
          <h3 className="text-2xl font-bold text-black mb-2 text-center">Want to learn more or try the dashboard?</h3>
          <p className="text-black mb-4 text-center">Join the waitlist or check out the docs to get started with DeFiIntel.ai.</p>
          <div className="flex gap-4">
            <a href="/demo" className="inline-block px-8 py-3 rounded-lg bg-black text-white font-semibold text-lg hover:bg-neutral-900 transition shadow-sm">Join Waitlist</a>
            <a href="/docs" className="inline-block px-8 py-3 rounded-lg border border-black text-black font-semibold text-lg hover:bg-neutral-100 transition shadow-sm">View Docs</a>
          </div>
        </motion.section>
      </div>
    </div>
  );
} 