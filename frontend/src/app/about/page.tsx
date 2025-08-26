"use client";
import Link from "next/link";

export default function AboutPage() {
  return (
    <div className="w-full min-h-screen flex flex-col items-center justify-center bg-white font-sans">
      <div className="w-full max-w-4xl mx-auto px-4 py-12">
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-extrabold text-black mb-4">
            About DeFiIntel.ai
          </h1>
          <p className="text-xl text-gray-500 font-light">
            Open-source DeFi fraud detection and analytics platform
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
          <div>
            <h2 className="text-2xl md:text-3xl font-bold text-black mb-4 text-left">What is DeFiIntel.ai?</h2>
            <p className="text-gray-600 mb-4 text-left">
              DeFiIntel.ai is an open-source DeFi fraud detection dashboard. It empowers users to analyze wallets, tokens, and social sentiment across multiple blockchains, integrating APIs like Helius, Etherscan, GeckoTerminal, and Twitter. The platform features ML-based fraud detection, wallet/token analytics, and a modern, minimal frontend built with Next.js and Streamlit.
            </p>
            <p className="text-gray-600 mb-4 text-left">
              Our mission is to provide transparent, accessible tools for detecting suspicious activity in the DeFi ecosystem, helping users make informed decisions about their investments.
            </p>
          </div>

          <div>
            <h2 className="text-2xl md:text-3xl font-bold text-black mb-4 text-left">Key Features</h2>
            <ul className="text-gray-600 space-y-2 text-left">
              <li>• Multi-chain blockchain analysis (Solana, Ethereum)</li>
              <li>• Machine learning fraud detection models</li>
              <li>• Real-time social sentiment analysis</li>
              <li>• Interactive data visualizations</li>
              <li>• Risk scoring and behavioral analysis</li>
              <li>• Integrated on-chain and social APIs (Helius, Etherscan, GeckoTerminal, Twitter) for real-time analytics.</li>
            </ul>
          </div>
        </div>

        <div className="bg-gray-50 rounded-2xl p-8 mb-12">
          <h2 className="text-2xl md:text-3xl font-bold text-black mb-4 text-center">Technology Stack</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="text-center">
              <h3 className="font-semibold text-black mb-2">Backend</h3>
              <p className="text-gray-600">Python, Streamlit, Pandas, Scikit-learn</p>
            </div>
            <div className="text-center">
              <h3 className="font-semibold text-black mb-2">Frontend</h3>
              <p className="text-gray-600">Next.js, TypeScript, Tailwind CSS</p>
            </div>
            <div className="text-center">
              <h3 className="font-semibold text-black mb-2">Data</h3>
              <p className="text-gray-600">Blockchain APIs, Twitter API, Real-time</p>
            </div>
          </div>
        </div>

        <div className="text-center">
          <p className="text-black mb-4 text-center">Join the waitlist or check out the docs to get started with DeFiIntel.ai.</p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/waitlist" className="px-6 py-3 bg-black text-white font-semibold rounded-lg hover:bg-neutral-900 transition shadow-sm">Join Waitlist</Link>
            <Link href="/docs" className="px-6 py-3 bg-white border border-black text-black font-semibold rounded-lg hover:bg-neutral-900 transition shadow-sm">View Documentation</Link>
          </div>
        </div>
      </div>
    </div>
  );
} 