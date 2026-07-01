export default function Header() {
  return (
    <header className="border-b border-gray-200 bg-white shadow-sm">
      <div className="max-w-4xl mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-gray-900">AI Live Assistant</h1>
            <p className="text-sm text-gray-600 mt-1">
              Powered by OpenAI GPT-4
            </p>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse" />
            <span className="text-sm text-gray-600">Online</span>
          </div>
        </div>
      </div>
    </header>
  )
}
