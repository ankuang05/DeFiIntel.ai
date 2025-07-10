"use client";
import { useState } from "react";

export default function DemoPage() {
  const [email, setEmail] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div className="min-h-[80vh] flex flex-col items-center justify-center bg-white px-4 py-24">
      <div className="w-full max-w-md flex flex-col items-center">
        <h1 className="text-4xl md:text-5xl font-extrabold text-black text-center leading-tight mb-2">request a</h1>
        <h2 className="text-5xl md:text-6xl font-extrabold text-black text-center mb-2">demo</h2>
        <p className="text-lg text-black text-center mb-8">be the first to experience the future of technical assessments</p>
        {submitted ? (
          <div className="w-full bg-white border border-black rounded-2xl p-6 text-center text-black font-semibold text-lg shadow-sm">Thank you for requesting a demo!</div>
        ) : (
          <form onSubmit={handleSubmit} className="w-full flex flex-col gap-4">
            <label htmlFor="email" className="text-base font-medium text-black mb-1">email address <span className="text-black">*</span></label>
            <input
              id="email"
              type="email"
              required
              placeholder="you@company.com"
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="w-full px-4 py-3 border border-black rounded-lg text-base text-black bg-white focus:outline-none focus:ring-2 focus:ring-black shadow-sm"
            />
            <button
              type="submit"
              className="w-full mt-2 px-4 py-3 rounded-lg bg-black text-white font-semibold text-lg hover:bg-neutral-900 transition shadow-sm"
            >
              Request Demo
            </button>
          </form>
        )}
      </div>
    </div>
  );
} 