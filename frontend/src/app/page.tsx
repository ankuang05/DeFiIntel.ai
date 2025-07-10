"use client";
import Link from "next/link";
import { motion } from "framer-motion";
import RotatingText from "../components/RotatingText";
import { useRef, useEffect } from "react";

// --- LetterGlitch Animated Background ---
function LetterGlitchBG() {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const animationRef = useRef<number | null>(null);
  const letters = useRef<any[]>([]);
  const grid = useRef<{ columns: number; rows: number }>({ columns: 0, rows: 0 });
  const context = useRef<CanvasRenderingContext2D | null>(null);
  const lastGlitchTime = useRef<number>(Date.now());

  const fontSize = 16;
  const charWidth = 10;
  const charHeight = 20;
  const glitchColors = ['#000', '#fff', '#222'];
  const glitchSpeed = 50;
  const smooth = true;
  const outerVignette = true;
  const centerVignette = false;

  const lettersAndSymbols = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '!', '@', '#', '$', '&', '*', '(', ')', '-', '_', '+', '=', '/',
    '[', ']', '{', '}', ';', ':', '<', '>', ',', '0', '1', '2', '3',
    '4', '5', '6', '7', '8', '9'
  ];

  const getRandomChar = (): string => {
    return lettersAndSymbols[Math.floor(Math.random() * lettersAndSymbols.length)];
  };

  const getRandomColor = (): string => {
    return glitchColors[Math.floor(Math.random() * glitchColors.length)];
  };

  const hexToRgb = (hex: string): { r: number; g: number; b: number } | null => {
    const shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    hex = hex.replace(shorthandRegex, (m: string, r: string, g: string, b: string) => {
      return r + r + g + g + b + b;
    });
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
      r: parseInt(result[1], 16),
      g: parseInt(result[2], 16),
      b: parseInt(result[3], 16)
    } : null;
  };

  const interpolateColor = (start: { r: number; g: number; b: number }, end: { r: number; g: number; b: number }, factor: number): string => {
    const result = {
      r: Math.round(start.r + (end.r - start.r) * factor),
      g: Math.round(start.g + (end.g - start.g) * factor),
      b: Math.round(start.b + (end.b - start.b) * factor),
    };
    return `rgb(${result.r}, ${result.g}, ${result.b})`;
  };

  const calculateGrid = (width: number, height: number): { columns: number; rows: number } => {
    const columns = Math.ceil(width / charWidth);
    const rows = Math.ceil(height / charHeight);
    return { columns, rows };
  };

  const initializeLetters = (columns: number, rows: number) => {
    grid.current = { columns, rows };
    const totalLetters = columns * rows;
    letters.current = Array.from({ length: totalLetters }, () => ({
      char: getRandomChar(),
      color: getRandomColor(),
      targetColor: getRandomColor(),
      colorProgress: 1,
    }));
  };

  const resizeCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const parent = canvas.parentElement;
    if (!parent) return;
    const dpr = window.devicePixelRatio || 1;
    const rect = parent.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    canvas.style.width = `${rect.width}px`;
    canvas.style.height = `${rect.height}px`;
    if (context.current) {
      context.current.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    const { columns, rows } = calculateGrid(rect.width, rect.height);
    initializeLetters(columns, rows);
    drawLetters();
  };

  const drawLetters = () => {
    if (!context.current || letters.current.length === 0 || !canvasRef.current) return;
    const ctx = context.current;
    const { width, height } = canvasRef.current.getBoundingClientRect();
    ctx.clearRect(0, 0, width, height);
    ctx.font = `${fontSize}px monospace`;
    ctx.textBaseline = 'top';
    letters.current.forEach((letter, index) => {
      const x = (index % grid.current.columns) * charWidth;
      const y = Math.floor(index / grid.current.columns) * charHeight;
      ctx.fillStyle = letter.color;
      ctx.fillText(letter.char, x, y);
    });
  };

  const updateLetters = () => {
    if (!letters.current || letters.current.length === 0) return;
    const updateCount = Math.max(1, Math.floor(letters.current.length * 0.05));
    for (let i = 0; i < updateCount; i++) {
      const index = Math.floor(Math.random() * letters.current.length);
      if (!letters.current[index]) continue;
      letters.current[index].char = getRandomChar();
      letters.current[index].targetColor = getRandomColor();
      if (!smooth) {
        letters.current[index].color = letters.current[index].targetColor;
        letters.current[index].colorProgress = 1;
      } else {
        letters.current[index].colorProgress = 0;
      }
    }
  };

  const handleSmoothTransitions = () => {
    let needsRedraw = false;
    letters.current.forEach((letter) => {
      if (letter.colorProgress < 1) {
        letter.colorProgress += 0.05;
        if (letter.colorProgress > 1) letter.colorProgress = 1;
        const startRgb = hexToRgb(letter.color);
        const endRgb = hexToRgb(letter.targetColor);
        if (startRgb && endRgb) {
          letter.color = interpolateColor(startRgb, endRgb, letter.colorProgress);
          needsRedraw = true;
        }
      }
    });
    if (needsRedraw) {
      drawLetters();
    }
  };

  const animate = () => {
    const now = Date.now();
    if (now - lastGlitchTime.current >= glitchSpeed) {
      updateLetters();
      drawLetters();
      lastGlitchTime.current = now;
    }
    if (smooth) {
      handleSmoothTransitions();
    }
    animationRef.current = requestAnimationFrame(animate);
  };

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    context.current = canvas.getContext('2d');
    resizeCanvas();
    animate();
    let resizeTimeout: ReturnType<typeof setTimeout>;
    const handleResize = () => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(() => {
        if (animationRef.current !== null) cancelAnimationFrame(animationRef.current);
        resizeCanvas();
        animate();
      }, 100);
    };
    window.addEventListener('resize', handleResize);
    return () => {
      if (animationRef.current !== null) cancelAnimationFrame(animationRef.current);
      window.removeEventListener('resize', handleResize);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [glitchSpeed, smooth]);

  return (
    <div className="fixed inset-0 w-full h-full -z-10 pointer-events-none">
      <canvas ref={canvasRef} style={{ display: 'block', width: '100%', height: '100%' }} />
      {outerVignette && <div style={{position:'absolute',top:0,left:0,width:'100%',height:'100%',pointerEvents:'none',background:'radial-gradient(circle, rgba(0,0,0,0) 60%, rgba(0,0,0,1) 100%)'}}></div>}
      {centerVignette && <div style={{position:'absolute',top:0,left:0,width:'100%',height:'100%',pointerEvents:'none',background:'radial-gradient(circle, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 60%)'}}></div>}
    </div>
  );
}

// --- Hero Section ---
function Hero() {
  return (
    <motion.section
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.7 }}
      transition={{ duration: 0.7 }}
      className="w-full flex flex-col items-center justify-center min-h-[80vh] pt-24 pb-16"
    >
      <h1 className="text-7xl font-extrabold text-black mb-4 text-center leading-[1.05]">
        Empowering Your<br />DeFi Journey
      </h1>
      <div className="mb-6 text-center">
        <RotatingText
          texts={["Fraud Detection", "Wallet Analytics", "Token Analysis", "Social Sentiment", "Open-Source Intelligence"]}
          mainClassName="px-2 md:px-3 bg-neutral-100 text-black text-4xl md:text-5xl font-extrabold justify-center rounded-lg"
          staggerFrom={"last"}
          initial={{ y: "100%", opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: "-120%", opacity: 0 }}
          staggerDuration={0.025}
          splitLevelClassName="overflow-hidden pb-1"
          transition={{ type: "spring", damping: 30, stiffness: 400 }}
          rotationInterval={2000}
        />
      </div>
      <p className="text-2xl text-gray-500 font-light mb-10 text-center max-w-2xl">
        Detect and mitigate fraud in decentralized finance with our open-source dashboard.
      </p>
      <div className="flex flex-row gap-4 mt-2">
        <Link href="#dashboard" className="px-8 py-4 rounded-xl bg-black text-white font-semibold text-lg hover:bg-neutral-900 transition">Explore the Dashboard</Link>
        <Link href="/demo" className="px-8 py-4 rounded-xl bg-white border border-black text-black font-semibold text-lg hover:bg-neutral-100 transition">Join Waitlist</Link>
      </div>
    </motion.section>
  );
}

// --- How to Use Section ---
function HowToUse() {
  const steps = [
    {
      title: "Step 1: Connect Your Wallet",
      desc: "Easily link your wallet to start analyzing transactions.",
    },
    {
      title: "Step 2: Choose Your Assets",
      desc: "Select the tokens you want to monitor for potential fraud.",
    },
    {
      title: "Step 3: Review Insights",
      desc: "Gain actionable intelligence through detailed analytics.",
    },
  ];
  return (
    <motion.section
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.7 }}
      transition={{ duration: 0.7 }}
      className="w-full max-w-6xl mx-auto py-20"
    >
      <h2 className="text-5xl font-extrabold text-black mb-2 text-center">How to Use DeFiIntel.ai</h2>
      <p className="text-gray-500 font-light text-center mb-10 text-lg">Your step-by-step guide to secure and insightful DeFi analysis.</p>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {steps.map((step, i) => (
          <motion.div
            key={step.title}
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.5 }}
            transition={{ delay: 0.1 * i, duration: 0.7 }}
            className="bg-white rounded-2xl border border-gray-200 p-8 flex flex-col items-start shadow-sm relative min-h-[300px]"
          >
            <div className="absolute top-4 left-4 w-8 h-8 flex items-center justify-center rounded-lg bg-gray-50 text-lg font-bold text-gray-500 border border-gray-200">{i + 1}</div>
            <div className="w-full flex-1 flex items-center justify-center mb-6">
              <div className="w-16 h-16 bg-gray-100 rounded-lg flex items-center justify-center">
                <svg width="32" height="32" fill="none" viewBox="0 0 24 24"><rect width="24" height="24" rx="4" fill="#E5E7EB"/><path d="M8 17h8M8 13h8M8 9h8" stroke="#9CA3AF" strokeWidth="2" strokeLinecap="round"/></svg>
              </div>
            </div>
            <h3 className="text-lg font-semibold text-black mb-1">{step.title}</h3>
            <p className="text-gray-500 font-light text-sm">{step.desc}</p>
          </motion.div>
        ))}
      </div>
    </motion.section>
  );
}

// --- Core Features Section ---
function CoreFeatures() {
  const features = [
    {
      title: "Wallet Analysis",
      desc: "Thorough examination of wallet activities for suspicious patterns.",
    },
    {
      title: "Token Analysis",
      desc: "In-depth scrutiny of token behavior and reliability.",
    },
    {
      title: "Social Sentiment",
      desc: "Real-time monitoring of community sentiment and discussions.",
    },
  ];
  return (
    <motion.section
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.7 }}
      transition={{ duration: 0.7 }}
      className="w-full max-w-6xl mx-auto py-20"
    >
      <h2 className="text-5xl font-extrabold text-black mb-2 text-center">Core Features</h2>
      <p className="text-gray-500 font-light text-center mb-10 text-lg">Discover powerful tools to protect your investments.</p>
      <div className="flex flex-col gap-8">
        {features.map((f, i) => (
          <motion.div
            key={f.title}
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.5 }}
            transition={{ delay: 0.1 * i, duration: 0.7 }}
            className="flex flex-col md:flex-row bg-gray-50 rounded-2xl p-8 items-center md:items-stretch shadow-sm"
          >
            <div className="w-full md:w-1/2 flex items-center justify-center mb-6 md:mb-0">
              <div className="w-full h-32 bg-gray-100 rounded-lg flex items-center justify-center">
                <svg width="48" height="48" fill="none" viewBox="0 0 24 24"><rect width="24" height="24" rx="4" fill="#E5E7EB"/><path d="M8 17h8M8 13h8M8 9h8" stroke="#9CA3AF" strokeWidth="2" strokeLinecap="round"/></svg>
              </div>
            </div>
            <div className="w-full md:w-1/2 flex flex-col justify-center md:pl-8">
              <h3 className="text-lg font-semibold text-black mb-1">{f.title}</h3>
              <p className="text-gray-500 font-light text-sm">{f.desc}</p>
            </div>
          </motion.div>
        ))}
      </div>
    </motion.section>
  );
}

// --- Explore Our Features Section ---
function ExploreFeatures() {
  const features = [
    {
      title: "Multi-Chain Support",
      desc: "Analyze multiple blockchains seamlessly in one place.",
    },
    {
      title: "Real-Time Analytics",
      desc: "Immediate insights into transactions and activities.",
    },
    {
      title: "Risk Scoring",
      desc: "Smart scoring system based on transaction behavior.",
    },
    {
      title: "Modular Design",
      desc: "Customize your dashboard with modular tools to fit your needs.",
    },
  ];
  return (
    <motion.section
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.7 }}
      transition={{ duration: 0.7 }}
      className="w-full max-w-6xl mx-auto py-20"
    >
      <h2 className="text-5xl font-extrabold text-black mb-2 text-center">Explore Our Features</h2>
      <p className="text-gray-500 font-light text-center mb-10 text-lg">Advanced tools for comprehensive fraud detection.</p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {features.map((f, i) => (
          <motion.div
            key={f.title}
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.5 }}
            transition={{ delay: 0.1 * i, duration: 0.7 }}
            className="bg-gray-50 rounded-2xl p-8 min-h-[180px] flex flex-col justify-end shadow-sm"
          >
            <h3 className="text-lg font-semibold text-black mb-1">{f.title}</h3>
            <p className="text-gray-500 font-light text-sm">{f.desc}</p>
          </motion.div>
        ))}
      </div>
    </motion.section>
  );
}

// --- Impactful Insights Section ---
function ImpactfulInsights() {
  return (
    <motion.section
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.7 }}
      transition={{ duration: 0.7 }}
      className="w-full max-w-4xl mx-auto py-20"
    >
      <h2 className="text-5xl font-extrabold text-black mb-2 text-center">Impactful Insights</h2>
      <p className="text-gray-500 font-light text-center mb-10 text-lg">Key metrics that matter in ensuring DeFi safety.</p>
      <div className="flex flex-col md:flex-row gap-8 justify-center items-center mt-12">
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ delay: 0.1, duration: 0.7 }}
          className="bg-white rounded-2xl p-10 min-w-[260px] text-center shadow-sm border border-gray-100 rotate-[-6deg]"
        >
          <div className="text-4xl font-extrabold text-black mb-2">100+</div>
          <div className="text-gray-500 font-light text-base">Fraudulent attempts detected annually.</div>
        </motion.div>
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.5 }}
          transition={{ delay: 0.2, duration: 0.7 }}
          className="bg-white rounded-2xl p-10 min-w-[260px] text-center shadow-sm border border-gray-100 rotate-[6deg]"
        >
          <div className="text-4xl font-extrabold text-black mb-2">75%</div>
          <div className="text-gray-500 font-light text-base">Users reporting improved decision-making.</div>
        </motion.div>
      </div>
    </motion.section>
  );
}

// --- FAQ Section ---
function FAQ() {
  const faqs = [
    { q: "What does DeFiIntel.ai do?", a: "DeFiIntel.ai provides real-time fraud detection and analytics for DeFi users across multiple blockchains." },
    { q: "Is DeFiIntel.ai open-source?", a: "Yes, DeFiIntel.ai is fully open-source and welcomes community contributions." },
    { q: "How do I get started?", a: "Simply connect your wallet and start exploring the dashboard for insights and analytics." },
    { q: "What if I encounter issues?", a: "You can reach out via our community forum or support channels for help." },
  ];
  return (
    <motion.section
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.7 }}
      transition={{ duration: 0.7 }}
      className="w-full max-w-3xl mx-auto py-20"
    >
      <h2 className="text-5xl font-extrabold text-black mb-2 text-center">Frequently Asked Questions</h2>
      <p className="text-gray-500 font-light text-center mb-10 text-lg">Got questions? We have answers.</p>
      <div className="flex flex-col gap-3">
        {faqs.map((faq, i) => (
          <motion.details
            key={faq.q}
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.5 }}
            transition={{ delay: 0.1 * i, duration: 0.7 }}
            className="bg-white border border-gray-200 rounded-lg px-4 py-3"
          >
            <summary className="font-medium text-black cursor-pointer select-none">{faq.q}</summary>
            <div className="text-gray-500 font-light mt-2 text-sm">{faq.a}</div>
          </motion.details>
        ))}
      </div>
    </motion.section>
  );
}

// --- Final CTA Section ---
function FinalCTA() {
  return (
    <motion.section
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.7 }}
      transition={{ duration: 0.7 }}
      className="w-full flex flex-col items-center justify-center py-20"
    >
      <div className="w-full max-w-3xl mx-auto text-center mb-10">
        <h2 className="text-5xl font-extrabold text-black mb-2">Ready to Secure Your<br />DeFi Investments?</h2>
        <p className="text-gray-500 font-light mb-6">Join the platform that protects millions.</p>
        <Link href="/get-started" className="inline-block px-6 py-3 rounded-lg bg-black text-white font-semibold text-base hover:bg-gray-800 transition">Get Started Now</Link>
      </div>
      <div className="w-full flex justify-center">
        {/* Placeholder for product illustration */}
        <div className="border-4 border-black rounded-2xl w-[420px] h-[180px] md:w-[520px] md:h-[220px] flex items-end justify-center relative bg-white">
          <div className="absolute left-8 bottom-8 w-2/3 h-24 border-4 border-black rounded-xl"></div>
          <div className="absolute right-8 bottom-4 w-1/4 h-32 border-4 border-black rounded-2xl"></div>
        </div>
      </div>
    </motion.section>
  );
}

// --- Footer ---
function Footer() {
  return (
    <footer className="w-full border-t border-gray-200 bg-white py-12 mt-8">
      <div className="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center md:items-start gap-8 px-4">
        <div className="flex flex-col items-center md:items-start">
          <div className="flex items-center gap-2 mb-1">
            {/* Blocky/stacked logo icon */}
            <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="2" y="2" width="8" height="8" rx="2" fill="#111"/>
              <rect x="2" y="12" width="8" height="8" rx="2" fill="#111"/>
              <rect x="12" y="12" width="8" height="8" rx="2" fill="#111"/>
            </svg>
            <span className="font-extrabold text-xl text-black select-none">DeFiIntel.ai</span>
          </div>
          <span className="text-gray-500 font-light text-sm mb-2">Your go-to platform for DeFi fraud detection.</span>
        </div>
        <div className="flex flex-wrap gap-12 justify-center md:justify-end">
          <div>
            <div className="font-semibold text-black mb-2">Resources</div>
            <ul className="text-gray-500 font-light text-sm space-y-1">
              <li><Link href="/blog">Blog</Link></li>
              <li><Link href="/docs">Documentation</Link></li>
              <li><Link href="/community">Community Forum</Link></li>
            </ul>
          </div>
          <div>
            <div className="font-semibold text-black mb-2">Company</div>
            <ul className="text-gray-500 font-light text-sm space-y-1">
              <li><Link href="/about">About Us</Link></li>
              <li><Link href="/careers">Careers</Link></li>
              <li><Link href="/privacy">Privacy Policy</Link></li>
            </ul>
          </div>
          <div>
            <div className="font-semibold text-black mb-2">Connect</div>
            <ul className="text-gray-500 font-light text-sm space-y-1">
              <li><a href="#" target="_blank" rel="noopener noreferrer">Twitter</a></li>
              <li><a href="#" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
              <li><a href="#" target="_blank" rel="noopener noreferrer">Discord</a></li>
            </ul>
          </div>
        </div>
      </div>
      <div className="text-center text-gray-400 font-light text-xs mt-8">© 2025. All rights reserved</div>
    </footer>
  );
}

export default function Home() {
  return (
    <div className="w-full min-h-screen flex flex-col items-center justify-center bg-white font-sans relative" style={{ fontFamily: 'Inter, Geist, Segoe UI, Arial, sans-serif' }}>
      <LetterGlitchBG />
      <Hero />
      <HowToUse />
      <CoreFeatures />
      <ExploreFeatures />
      <ImpactfulInsights />
      <FAQ />
      <FinalCTA />
      <Footer />
    </div>
  );
}
