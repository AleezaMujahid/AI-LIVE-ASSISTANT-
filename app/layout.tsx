import type { Metadata, Viewport } from 'next'
import { Geist, Geist_Mono } from 'next/font/google'
import './globals.css'

const geistSans = Geist({ subsets: ['latin'] })
const geistMono = Geist_Mono({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'AI Live Assistant',
  description: 'A real-time AI chat assistant powered by OpenAI',
}

export const viewport: Viewport = {
  themeColor: '#000000',
  userScalable: true,
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="bg-background">
      <body className={`${geistSans.className} antialiased`}>
        {children}
      </body>
    </html>
  )
}
