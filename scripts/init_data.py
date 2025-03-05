from app import create_app
from app.extensions import mongo
from werkzeug.security import generate_password_hash
from datetime import datetime
import os
from dotenv import load_dotenv

def init_database():
    # Load environment variables first
    load_dotenv()
    
    app = create_app()
    
    # Set MongoDB URI explicitly
    app.config['MONGO_URI'] = 'mongodb+srv://root:root@catalogcarros.8eqf6.mongodb.net/vehicles_db'
    
    # Initialize MongoDB with the app
    mongo.init_app(app)
    
    with app.app_context():
        try:
            # Test connection with a simpler command
            print("Attempting to connect to MongoDB...")
            mongo.cx.server_info()  # Test connection
            print("MongoDB connection successful!")
            
            # Create admin user
            if not mongo.db.users.find_one({'username': 'admin'}):
                admin_user = {
                    'username': 'admin',
                    'password': generate_password_hash('admin123'),
                    'role': 'admin',
                    'created_at': datetime.now()
                }
                mongo.db.users.insert_one(admin_user)
                print("Admin user created")

            # Create sample vehicles
            sample_vehicles = [
                {
                    'nome': 'Civic',
                    'marca': 'Honda',
                    'modelo': 'EXL',
                    'foto': 'https://example.com/civic.jpg',
                    'valor': 150000.00,
                    'created_at': datetime.now()
                },
                {
                    'nome': 'Corolla',
                    'marca': 'Toyota',
                    'modelo': 'XEI',
                    'foto': 'https://example.com/corolla.jpg',
                    'valor': 160000.00,
                    'created_at': datetime.now()
                },
                {
                    'nome': 'Golf',
                    'marca': 'Volkswagen',
                    'modelo': 'GTI',
                    'foto': 'https://example.com/golf.jpg',
                    'valor': 180000.00,
                    'created_at': datetime.now()
                }
            ]

            for vehicle in sample_vehicles:
                if not mongo.db.vehicles.find_one({'nome': vehicle['nome'], 'modelo': vehicle['modelo']}):
                    mongo.db.vehicles.insert_one(vehicle)
                    print(f"Vehicle {vehicle['nome']} {vehicle['modelo']} created")
                    
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    init_database()