'use client'

import { Message } from 'ai'
import MessageBubble from './MessageBubble'

export default function MessageList({ messages }: { messages: Message[] }) {
  if (messages.length === 0) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center">
          <div className="text-6xl mb-4">💬</div>
          <h2 className="text-2xl font-bold text-gray-900 mb-2">
            Welcome to AI Live Assistant
          </h2>
          <p className="text-gray-600 max-w-md">
            Start a conversation by typing your message below. I&apos;m here to help with any questions!
          </p>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-6">
      {messages.map((message, index) => (
        <MessageBubble
          key={index}
          message={message}
          isUser={message.role === 'user'}
        />
      ))}
    </div>
  )
}
