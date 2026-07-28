import os
import asyncio
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram.ext import ApplicationBuilder

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")
    def log_message(self, format, *args):
        pass

def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()

async def main():
    print("Bot is starting...")
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN not set!")

    thread = threading.Thread(target=run_health_server, daemon=True)
    thread.start()
    print("Health server running...")

    app = ApplicationBuilder().token(token).build()
    async with app:
        print("Bot is running!")
        await app.start()
        await app.updater.start_polling()
        await asyncio.sleep(float("inf"))

if __name__ == "__main__":
    asyncio.run(main())