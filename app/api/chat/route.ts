import { openai } from '@ai-sdk/openai'
import { streamText } from 'ai'

export async function POST(req: Request) {
  const { messages } = await req.json()

  const result = streamText({
    model: openai('gpt-4-turbo'),
    system:
      'You are a helpful AI assistant. Provide clear, concise, and accurate responses. If you do not know something, say so rather than making something up.',
    messages,
  })

  return result.toDataStreamResponse()
}
