"use client";
import { motion } from "framer-motion";

export default function GetStartedPage() {
  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-white font-sans px-4" style={{ fontFamily: 'Inter, Geist, Segoe UI, Arial, sans-serif' }}>
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.7 }}
        className="text-4xl md:text-5xl font-extrabold text-black text-center"
      >
        Coming Soon
      </motion.div>
    </div>
  );
} 