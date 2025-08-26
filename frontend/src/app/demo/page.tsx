"use client";
import React from "react";

export default function DemoPage() {
  // List your demo images here. Add more as needed.
  const images = [
    { src: "/demo/dashboard-1.png", alt: "Dashboard Overview" },
    { src: "/demo/wallet-analysis.png", alt: "Wallet Analysis" },
    { src: "/demo/ml-prediction.png", alt: "ML Prediction" },
    // Add more images as needed
  ];

  return (
    <div className="max-w-4xl mx-auto py-12 px-4">
      <h1 className="text-3xl font-bold mb-4">DeFiIntel.ai Demo Gallery</h1>
      <p className="text-gray-600 mb-8 text-lg">
        Explore screenshots of the DeFiIntel.ai dashboard and features in action.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {images.map((img) => (
          <div key={img.src} className="rounded-xl overflow-hidden shadow-lg border border-gray-200 bg-white flex items-center justify-center">
            <img src={img.src} alt={img.alt} className="w-full h-auto object-contain" />
          </div>
        ))}
      </div>
    </div>
  );
} 