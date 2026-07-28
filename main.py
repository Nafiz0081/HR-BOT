# main.py
from telegram.ext import ApplicationBuilder

def main():
    print("Hello from hr-bot!")
    
    app = ApplicationBuilder().token("8937341187:AAHjEe_yOgi0D-EJw15p9oBE7A8jiJFKB-0").build()
    
    # This line blocks forever — exactly what Render needs
    app.run_polling()

if __name__ == "__main__":
    main()
