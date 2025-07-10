"use client";
import { useState } from "react";
import { motion } from "framer-motion";
import LetterGlitchBG from "../../components/LetterGlitchBG";

export default function DemoPage() {
  const [submitted, setSubmitted] = useState(false);
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
      setError("Please enter a valid email address.");
      return;
    }
    setError("");
    setSubmitted(true);
  };

  return (
    <div className="min-h-screen w-full flex items-center justify-center font-sans px-4 relative" style={{ fontFamily: 'Inter, Geist, Segoe UI, Arial, sans-serif' }}>
      <LetterGlitchBG
        glitchColors={["#111", "#fff", "#888"]}
        glitchSpeed={50}
        centerVignette={true}
        outerVignette={false}
        smooth={true}
      />
      <div className="relative z-10 w-full max-w-xl mx-auto flex flex-col items-center justify-center">
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
          className="bg-white rounded-2xl shadow-xl px-8 py-12 w-full flex flex-col items-center"
        >
          {!submitted ? (
            <form onSubmit={handleSubmit} className="w-full flex flex-col items-center">
              <h1 className="text-5xl md:text-6xl font-extrabold text-black text-center mb-2 leading-tight">Join the Waitlist</h1>
              <p className="text-xl text-gray-500 font-light text-center mb-12 max-w-lg">Be the first to experience the future of DeFi fraud detection and analytics</p>
              <div className="w-full text-left mb-2">
                <label htmlFor="email" className="text-gray-700 font-light text-base mb-1 block">Email address *</label>
              </div>
              <input
                id="email"
                type="email"
                autoComplete="email"
                required
                value={email}
                onChange={e => setEmail(e.target.value)}
                className="w-full bg-transparent border border-gray-300 rounded-lg px-6 py-4 text-lg text-gray-900 placeholder-gray-400 focus:outline-none focus:border-black transition mb-6"
                placeholder="you@company.com"
              />
              {error && <div className="text-red-500 text-sm mb-4">{error}</div>}
              <button
                type="submit"
                className="w-full bg-black text-white font-medium tracking-widest text-lg rounded-lg py-5 mt-2 hover:bg-neutral-900 transition"
              >
                Join waitlist
              </button>
            </form>
          ) : (
            <div className="w-full flex flex-col items-center justify-center py-24">
              <h2 className="text-4xl font-extrabold text-black mb-4 text-center">Thank you!</h2>
              <p className="text-lg text-gray-600 font-light text-center max-w-md">You've been added to the waitlist. We'll notify you when DeFiIntel.ai is ready for you to try.</p>
            </div>
          )}
        </motion.div>
      </div>
    </div>
  );
} 