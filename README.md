# AI Live Assistant

A modern, real-time AI chat application built with Next.js 16, React 19, and OpenAI's GPT-4.

## Features

- Real-time streaming chat responses
- Clean, modern UI with Tailwind CSS
- Built with Next.js 16 App Router
- Powered by AI SDK and OpenAI GPT-4
- Production-ready deployment configuration
- TypeScript support
- Responsive design

## Tech Stack

- **Framework**: Next.js 16 with App Router
- **UI**: React 19 with TypeScript
- **Styling**: Tailwind CSS v4 with Radix UI components
- **AI**: Vercel AI SDK with OpenAI integration
- **Icons**: Lucide React
- **Package Manager**: npm

## Prerequisites

- Node.js 18.17+ or later
- npm or yarn
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))

## Environment Setup

1. Copy `.env.example` to `.env.local`:
   ```bash
   cp .env.example .env.local
   ```

2. Add your OpenAI API key to `.env.local`:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

## Installation

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

The application will be available at `http://localhost:3000`

## Deployment

### Vercel Deployment (Recommended)

The easiest way to deploy is using [Vercel](https://vercel.com):

1. Push your code to GitHub
2. Import the repository in Vercel
3. Add environment variables in Vercel project settings:
   - `OPENAI_API_KEY`: Your OpenAI API key
4. Deploy

### Environment Variables for Deployment

Required environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key

Optional:
- `AI_GATEWAY_API_KEY`: If using Vercel AI Gateway

### Docker Deployment

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY .next ./.next
COPY public ./public

EXPOSE 3000

CMD ["npm", "start"]
```

Build and run:
```bash
docker build -t ai-assistant .
docker run -p 3000:3000 -e OPENAI_API_KEY=your_key ai-assistant
```

## Project Structure

```
├── app/
│   ├── api/
│   │   └── chat/
│   │       └── route.ts           # Chat API endpoint
│   ├── layout.tsx                 # Root layout
│   ├── globals.css                # Global styles
│   └── page.tsx                   # Home page
├── components/
│   ├── ChatInterface.tsx           # Main chat component
│   ├── Header.tsx                 # App header
│   ├── MessageList.tsx            # Message display
│   ├── MessageBubble.tsx          # Individual message
│   └── MessageInput.tsx           # Input form
├── public/                        # Static assets
├── package.json
├── next.config.mjs               # Next.js configuration
├── tsconfig.json                 # TypeScript configuration
└── tailwind.config.js            # Tailwind configuration
```

## Development

### Scripts

- `npm run dev` - Start development server with hot reload
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint

### Adding Features

The app uses:
- **AI SDK** for streaming responses: `ai/react` and `ai`
- **Tailwind CSS** for styling
- **Radix UI** components (pre-installed)
- **TypeScript** for type safety

## Performance Optimizations

- Cache components enabled in Next.js 16
- Image optimization
- Streaming responses for real-time UI updates
- Component-level code splitting

## Troubleshooting

### API Key Issues
- Verify your OpenAI API key is valid and active
- Check that you have API credits available
- Ensure the key is set in environment variables

### Build Issues
- Clear `.next` folder: `rm -rf .next`
- Reinstall dependencies: `rm -rf node_modules && npm install`
- Check Node.js version: `node --version` (should be 18.17+)

### Runtime Issues
- Check server logs for error details
- Verify all environment variables are set
- Ensure network connectivity to OpenAI API

## API Reference

### POST `/api/chat`

Sends a message and returns a streaming response.

**Request:**
```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello, how are you?"
    }
  ]
}
```

**Response:** Server-sent events stream with AI response

## Security Best Practices

- Never commit `.env.local` file
- Keep API keys secure and rotate regularly
- Use rate limiting in production
- Validate and sanitize all user inputs
- Monitor API usage for unusual patterns

## License

MIT

## Support

For issues and questions:
1. Check the [Next.js documentation](https://nextjs.org/docs)
2. Review [AI SDK documentation](https://sdk.vercel.ai)
3. Visit [OpenAI documentation](https://platform.openai.com/docs)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Built with ❤️ using Next.js and OpenAI
