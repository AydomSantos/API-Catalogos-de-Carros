const API_URL = 'http://localhost:5000';
let token = localStorage.getItem('token');

// Navigation functions
function showLoginForm() {
    document.getElementById('publicCatalog').style.display = 'none';
    document.getElementById('loginForm').style.display = 'block';
    document.getElementById('adminDashboard').style.display = 'none';
}

function showPublicCatalog() {
    document.getElementById('publicCatalog').style.display = 'block';
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('adminDashboard').style.display = 'none';
    loadPublicVehicles();
}

function showAdminDashboard() {
    document.getElementById('publicCatalog').style.display = 'none';
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('adminDashboard').style.display = 'block';
    loadAdminVehicles();
}

// Login handling
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch(`${API_URL}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();
        if (data.access_token) {
            token = data.access_token;
            localStorage.setItem('token', token);
            showAdminDashboard();
        } else {
            alert('Login falhou!');
        }
    } catch (error) {
        alert('Erro ao fazer login!');
    }
});

function logout() {
    localStorage.removeItem('token');
    token = null;
    showPublicCatalog();
}

// Load vehicles for public view
async function loadPublicVehicles() {
    try {
        const response = await fetch(`${API_URL}/vehicles`);
        const vehicles = await response.json();
        displayPublicVehicles(vehicles);
    } catch (error) {
        alert('Erro ao carregar veículos!');
    }
}

// Load vehicles for admin view
async function loadAdminVehicles() {
    try {
        const response = await fetch(`${API_URL}/vehicles`);
        const vehicles = await response.json();
        displayAdminVehicles(vehicles);
    } catch (error) {
        alert('Erro ao carregar veículos!');
    }
}

// Display vehicles for public view
function displayPublicVehicles(vehicles) {
    const vehiclesList = document.getElementById('publicVehiclesList');
    vehiclesList.innerHTML = '';

    vehicles.forEach(vehicle => {
        const card = document.createElement('div');
        card.className = 'col-md-4';
        card.innerHTML = `
            <div class="card card-vehicle">
                <img src="${vehicle.foto || 'https://via.placeholder.com/300'}" class="card-img-top vehicle-image" alt="${vehicle.nome}">
                <div class="card-body">
                    <h5 class="card-title">${vehicle.nome}</h5>
                    <p class="card-text">
                        Marca: ${vehicle.marca}<br>
                        Modelo: ${vehicle.modelo}<br>
                        Valor: R$ ${vehicle.valor}
                    </p>
                </div>
            </div>
        `;
        vehiclesList.appendChild(card);
    });
}

// Display vehicles for admin view
function displayAdminVehicles(vehicles) {
    const vehiclesList = document.getElementById('adminVehiclesList');
    vehiclesList.innerHTML = '';

    vehicles.forEach(vehicle => {
        const card = document.createElement('div');
        card.className = 'col-md-4';
        card.innerHTML = `
            <div class="card card-vehicle">
                <img src="${vehicle.foto || 'https://via.placeholder.com/300'}" class="card-img-top vehicle-image" alt="${vehicle.nome}">
                <div class="card-body">
                    <h5 class="card-title">${vehicle.nome}</h5>
                    <p class="card-text">
                        Marca: ${vehicle.marca}<br>
                        Modelo: ${vehicle.modelo}<br>
                        Valor: R$ ${vehicle.valor}
                    </p>
                    <div class="btn-group w-100">
                        <button class="btn btn-primary" onclick="editVehicle('${vehicle._id}')">Editar</button>
                        <button class="btn btn-danger" onclick="deleteVehicle('${vehicle._id}')">Excluir</button>
                    </div>
                </div>
            </div>
        `;
        vehiclesList.appendChild(card);
    });
}
// Save vehicle
document.getElementById('saveVehicle').addEventListener('click', async () => {
    const vehicleId = document.getElementById('vehicleId').value;
    const vehicle = {
        nome: document.getElementById('nome').value,
        marca: document.getElementById('marca').value,
        modelo: document.getElementById('modelo').value,
        foto: document.getElementById('foto').value || 'https://placehold.co/300x200',
        valor: Number(document.getElementById('valor').value)
    };

    try {
        const url = vehicleId 
            ? `${API_URL}/admin/vehicles/${vehicleId}`
            : `${API_URL}/admin/vehicles`;
        
        const method = vehicleId ? 'PUT' : 'POST';

        const response = await fetch(url, {
            method,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(vehicle)
        });

        if (!response.ok) {
            throw new Error('Failed to save vehicle');
        }

        bootstrap.Modal.getInstance(document.getElementById('vehicleModal')).hide();
        loadAdminVehicles();
    } catch (error) {
        alert('Erro ao salvar veículo: ' + error.message);
    }
});
// Edit vehicle
async function editVehicle(id) {
    try {
        // Remove any quotes from the id string
        const cleanId = id.replace(/['"]+/g, '');
        const response = await fetch(`${API_URL}/vehicles/${cleanId}`);
        
        if (!response.ok) {
            throw new Error('Vehicle not found');
        }
        
        const vehicle = await response.json();
        document.getElementById('vehicleId').value = cleanId;
        document.getElementById('nome').value = vehicle.nome;
        document.getElementById('marca').value = vehicle.marca;
        document.getElementById('modelo').value = vehicle.modelo;
        document.getElementById('foto').value = vehicle.foto;
        document.getElementById('valor').value = vehicle.valor;

        new bootstrap.Modal(document.getElementById('vehicleModal')).show();
    } catch (error) {
        alert('Erro ao carregar veículo!');
    }
}

// Delete vehicle
async function deleteVehicle(id) {
    if (confirm('Tem certeza que deseja excluir este veículo?')) {
        try {
            // Remove any quotes from the id string
            const cleanId = id.replace(/['"]+/g, '');
            const response = await fetch(`${API_URL}/admin/vehicles/${cleanId}`, {
                method: 'DELETE',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });

            if (response.ok) {
                loadAdminVehicles();
            } else {
                const error = await response.json();
                throw new Error(error.message || 'Erro ao excluir veículo');
            }
        } catch (error) {
            alert(error.message || 'Erro ao excluir veículo');
        }
    }
}

// Initial load
if (token) {
    showAdminDashboard();
} else {
    showPublicCatalog();
}