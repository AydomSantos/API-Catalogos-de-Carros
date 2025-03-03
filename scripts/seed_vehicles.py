import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.extensions import db
from app.models.vehicle import Vehicle

# Lista de veículos para teste
vehicles_data = [
    {
        "nome": "Corolla Cross",
        "marca": "Toyota",
        "modelo": "XRX Hybrid",
        "foto": "https://www.toyota.com.br/wp-content/uploads/2021/03/corolla-cross-xrx-hybrid-celestial-black.png",
        "valor": 184990.00
    },
    {
        "nome": "Civic",
        "marca": "Honda",
        "modelo": "EXL",
        "foto": "https://www.honda.com.br/automoveis/sites/hab/files/2020-12/Civic_EXL_PrataMeteoro.png",
        "valor": 149990.00
    },
    {
        "nome": "Compass",
        "marca": "Jeep",
        "modelo": "Limited",
        "foto": "https://www.jeep.com.br/content/dam/jeep/products/603/2d4/4/2024/page/hero.png",
        "valor": 198990.00
    },
    {
        "nome": "HB20",
        "marca": "Hyundai",
        "modelo": "Premium",
        "foto": "https://www.hyundai.com.br/content/dam/hyundai/brasil/pt/models/hb20-nova-geracao/versoes/hb20-premium.png",
        "valor": 94990.00
    },
    {
        "nome": "Kicks",
        "marca": "Nissan",
        "modelo": "Advance",
        "foto": "https://www.nissan.com.br/content/dam/Nissan/br/vehicles/kicks/product_code/product_version/my23/advance-cvt.png.ximg.l_full_m.smart.png",
        "valor": 116990.00
    },
    {
        "nome": "Tracker",
        "marca": "Chevrolet",
        "modelo": "Premier",
        "foto": "https://www.chevrolet.com.br/content/dam/chevrolet/mercosur/brazil/portuguese/index/crossovers-and-suvs/2024-tracker/mov/01-images/novo-tracker-2024.png",
        "valor": 129990.00
    },
    {
        "nome": "T-Cross",
        "marca": "Volkswagen",
        "modelo": "Highline",
        "foto": "https://volkswagen.com.br/content/dam/onehub_pkw/importers/br/models/2024/tcross/exterior/T-Cross-Highline.png",
        "valor": 146990.00
    },
    {
        "nome": "Pulse",
        "marca": "Fiat",
        "modelo": "Impetus",
        "foto": "https://pulse.fiat.com.br/content/dam/fiat/products/341/a11/0/2024/page/hero.png",
        "valor": 129990.00
    }
]

app = create_app()

with app.app_context():
    # Adiciona cada veículo ao banco de dados
    for vehicle_data in vehicles_data:
        vehicle = Vehicle.create(vehicle_data)
        db.session.add(vehicle)
    
    # Commit das alterações
    try:
        db.session.commit()
        print(f"✅ {len(vehicles_data)} veículos foram adicionados com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao adicionar veículos: {str(e)}")
        db.session.rollback() 