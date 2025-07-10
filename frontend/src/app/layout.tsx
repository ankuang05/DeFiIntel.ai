import Link from 'next/link';
import './globals.css';

export const metadata = {
  title: 'DeFiIntel.ai',
  description: 'Open-source DeFi fraud detection dashboard',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-white min-h-screen flex flex-col font-sans">
        {/* Navbar */}
        <nav className="sticky top-0 z-20 w-full bg-white border-b border-gray-100 flex items-center justify-between px-8 py-4">
          <Link href="/" className="flex items-center gap-2 select-none">
            {/* Tiny geometric logo */}
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="2" y="2" width="7" height="7" rx="2" fill="#111"/>
              <rect x="2" y="11" width="7" height="7" rx="2" fill="#111"/>
              <rect x="11" y="11" width="7" height="7" rx="2" fill="#111"/>
            </svg>
            <span className="text-2xl font-extrabold text-black tracking-tight">DeFiIntel.ai</span>
          </Link>
          <div className="flex items-center gap-8">
            <Link href="/" className="text-black text-base font-medium hover:text-blue-600 transition">Home</Link>
            <Link href="/about" className="text-black text-base font-medium hover:text-blue-600 transition">About</Link>
            <Link href="/get-started" className="text-black text-base font-medium hover:text-blue-600 transition">Get Started</Link>
            <Link href="/docs" className="text-black text-base font-medium hover:text-blue-600 transition">Docs</Link>
            <Link href="/blog" className="text-black text-base font-medium hover:text-blue-600 transition">Blog</Link>
            <Link href="/demo" className="ml-4 px-6 py-2 bg-black text-white rounded-lg font-semibold text-base hover:bg-neutral-900 transition">Join Waitlist</Link>
          </div>
        </nav>
        <main className="flex-1 w-full flex flex-col items-center justify-center">{children}</main>
      </body>
    </html>
  );
}
