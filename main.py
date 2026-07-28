# main.py
from telegram.ext import ApplicationBuilder

def main():
    print("Hello from hr-bot!")
    
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()
    
    # This line blocks forever — exactly what Render needs
    app.run_polling()

if __name__ == "__main__":
    main()
