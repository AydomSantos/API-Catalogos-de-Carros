"""
This is the main file that will run the application.
"""

from dotenv import load_dotenv
load_dotenv()  # Load environment variables before importing app

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)




