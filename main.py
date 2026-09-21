from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Açaí Mania Delivery Gratuito")

# Dados do cardápio extraídos da plataforma
PRODUCTS = [
    {
        "id": 1,
        "name": "Copo Açaí 250 ml",
        "price": 10.00,
        "description": "2 acompanhamentos inclusos",
        "max_acomp": 2,
        "category": "Copo"
    },
    {
        "id": 2,
        "name": "Copo Açaí 350ml",
        "price": 12.00,
        "description": "4 acompanhamentos inclusos",
        "max_acomp": 4,
        "category": "Copo"
    },
    {
        "id": 3,
        "name": "Copo Açaí de 400ml",
        "price": 15.00,
        "description": "5 acompanhamentos inclusos",
        "max_acomp": 5,
        "category": "Copo"
    },
    {
        "id": 4,
        "name": "Copo Açaí 770ml",
        "price": 25.00,
        "description": "7 acompanhamentos inclusos",
        "max_acomp": 7,
        "category": "Copo"
    },
    {
        "id": 5,
        "name": "Combo Supremo",
        "price": 45.00,
        "description": "4 copos de Açaí de 350 ml, com 4 acompanhamentos em cada.",
        "max_acomp": 4,
        "category": "Combo"
    },
    {
        "id": 6,
        "name": "Combo Mania",
        "price": 42.00,
        "description": "3 copos de 400 ml cada, com 5 acompanhamentos em cada.",
        "max_acomp": 5,
        "category": "Combo"
    }
]

# Acompanhamentos comuns (você pode customizar os adicionais do seu irmão aqui)
ACCOMPANIMENTS = [
    "Leite Condensado", "Leite Ninho", "Paçoca", "Granola", 
    "Flocos de Arroz", "Ovomaltine", "Chocobom", "Morango", 
    "Banana", "Creme de Cupuaçu", "Gotas de Chocolate"
]

class OrderItem(BaseModel):
    product_name: str
    price: float
    selected_acomp: List[str]
    client_name: str
    address: str
    neighborhood: str
    payment_method: str
    change_for: str = ""

@app.get("/api/menu")
def get_menu():
    return {
        "store": "Açaí Mania",
        "address": "Projetada, 31 - Kiola Sarney",
        "products": PRODUCTS,
        "accompaniments": ACCOMPANIMENTS
    }

@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTML_CONTENT

# HTML incorporado para facilitar rodar direto com uvicorn main:app --reload
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Açaí Mania - Cardápio Digital</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen">
    <!-- Header -->
    <header class="bg-purple-950 border-b border-purple-900 p-4 shadow-md sticky top-0 z-50">
        <div class="max-w-4xl mx-auto flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <div class="bg-purple-600 rounded-full h-12 w-12 flex items-center justify-center font-bold text-xl">AM</div>
                <div>
                    <h1 class="text-xl font-bold">Açaí Mania</h1>
                    <p class="text-xs text-purple-300">Projetada, 31 - Kiola Sarney</p>
                </div>
            </div>
            <div class="bg-emerald-600 text-xs px-3 py-1 rounded-full font-semibold flex items-center gap-1">
                <span class="w-2 h-2 rounded-full bg-white animate-pulse"></span> Aberto
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <main class="max-w-4xl mx-auto p-4 pb-24">
        <div class="my-6">
            <h2 class="text-2xl font-black text-purple-400 mb-1">Nosso Cardápio</h2>
            <p class="text-sm text-slate-400">Monte seu pedido do seu jeito, sem taxas extras!</p>
        </div>

        <div id="product-list" class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <!-- Os produtos entram aqui via JS -->
        </div>
    </main>

    <!-- Modal de Montagem / Carrinho -->
    <div id="modal" class="fixed inset-0 bg-black/80 backdrop-blur-xs hidden z-50 flex items-center justify-center p-4">
        <div class="bg-slate-800 border border-slate-700 w-full max-w-lg rounded-2xl p-6 max-h-[90vh] overflow-y-auto shadow-2xl">
            <div class="flex justify-between items-center mb-4">
                <h3 id="modal-title" class="text-xl font-bold text-purple-400"></h3>
                <button onclick="closeModal()" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark text-xl"></i></button>
            </div>
            <p id="modal-desc" class="text-sm text-slate-300 mb-4"></p>
            
            <div id="acomp-container" class="mb-6">
                <label class="block text-sm font-semibold mb-2 text-purple-300">Escolha os Acompanhamentos:</label>
                <div id="acomp-list" class="grid grid-cols-2 gap-2"></div>
            </div>

            <div class="border-t border-slate-700 pt-4 space-y-3">
                <h4 class="font-bold text-sm text-purple-300">Dados para Entrega</h4>
                <input type="text" id="client-name" placeholder="Seu Nome Completo" class="w-full bg-slate-900 border border-slate-700 p-2.5 rounded-lg text-sm focus:outline-purple-500">
                <input type="text" id="client-address" placeholder="Endereço (Rua, Número)" class="w-full bg-slate-900 border border-slate-700 p-2.5 rounded-lg text-sm focus:outline-purple-500">
                <input type="text" id="client-neighborhood" placeholder="Bairro" value="Kiola Sarney / Região" class="w-full bg-slate-900 border border-slate-700 p-2.5 rounded-lg text-sm focus:outline-purple-500">
                
                <select id="payment-method" class="w-full bg-slate-900 border border-slate-700 p-2.5 rounded-lg text-sm focus:outline-purple-500">
                    <option value="Pix">Pix</option>
                    <option value="Cartão">Cartão (Débito/Crédito)</option>
                    <option value="Dinheiro">Dinheiro</option>
                </select>
                <input type="text" id="change-for" placeholder="Troco para quanto? (Se precisar)" class="w-full bg-slate-900 border border-slate-700 p-2.5 rounded-lg text-sm hidden">
            </div>

            <div class="mt-6 flex gap-3">
                <button onclick="closeModal()" class="w-1/2 bg-slate-700 hover:bg-slate-600 py-3 rounded-xl font-bold text-sm">Cancelar</button>
                <button onclick="sendOrder()" class="w-1/2 bg-emerald-600 hover:bg-emerald-500 py-3 rounded-xl font-bold text-sm flex items-center justify-center gap-2">
                    <i class="fa-brands fa-whatsapp text-lg"></i> Enviar Pedido
                </button>
            </div>
        </div>
    </div>

    <script>
        let menuData = {};
        let currentProduct = null;

        fetch('/api/menu')
            .then(res => res.json())
            .then(data => {
                menuData = data;
                renderProducts();
            });

        function renderProducts() {
            const list = document.getElementById('product-list');
            list.innerHTML = '';
            menuData.products.forEach(p => {
                list.innerHTML += `
                    <div class="bg-slate-800 border border-slate-700/60 rounded-2xl p-4 flex flex-col justify-between shadow-lg">
                        <div>
                            <span class="text-xs uppercase tracking-wider bg-purple-900/50 text-purple-300 px-2 py-0.5 rounded-md font-semibold">${p.category}</span>
                            <h3 class="font-bold text-lg mt-2">${p.name}</h3>
                            <p class="text-xs text-slate-400 mt-1">${p.description}</p>
                        </div>
                        <div class="flex justify-between items-center mt-4 pt-3 border-t border-slate-700/40">
                            <span class="font-black text-emerald-400 text-lg">R$ ${p.price.toFixed(2)}</span>
                            <button onclick="openModal(${p.id})" class="bg-purple-600 hover:bg-purple-500 text-white px-4 py-2 rounded-xl text-xs font-bold transition-all">Montar</button>
                        </div>
                    </div>
                `;
            });
        }

        function openModal(id) {
            currentProduct = menuData.products.find(p => p.id === id);
            document.getElementById('modal-title').innerText = currentProduct.name;
            document.getElementById('modal-desc').innerText = currentProduct.description + ` (Escolha até ${currentProduct.max_acomp} adicionais)`;
            
            const acompList = document.getElementById('acomp-list');
            acompList.innerHTML = '';
            menuData.accompaniments.forEach(a => {
                acompList.innerHTML += `
                    <label class="flex items-center space-x-2 text-sm bg-slate-900/50 p-2 rounded-lg border border-slate-700/40 cursor-pointer hover:border-purple-500">
                        <input type="checkbox" name="acomp" value="${a}" class="rounded text-purple-600 focus:ring-purple-500 h-4 w-4">
                        <span class="text-slate-300 text-xs">${a}</span>
                    </label>
                `;
            });

            document.getElementById('modal').classList.remove('hidden');
        }

        function closeModal() {
            document.getElementById('modal').classList.add('hidden');
        }

        document.getElementById('payment-method').addEventListener('change', (e) => {
            const changeInput = document.getElementById('change-for');
            if(e.target.value === 'Dinheiro') {
                changeInput.classList.remove('hidden');
            } else {
                changeInput.classList.add('hidden');
            }
        });

        function sendOrder() {
            const name = document.getElementById('client-name').value;
            const address = document.getElementById('client-address').value;
            const neighborhood = document.getElementById('client-neighborhood').value;
            const payment = document.getElementById('payment-method').value;
            const change = document.getElementById('change-for').value;

            if(!name || !address) {
                alert('Por favor, preencha seu nome e endereço de entrega!');
                return;
            }

            const checkboxes = document.querySelectorAll('input[name="acomp"]:checked');
            const selectedAcomp = Array.from(checkboxes).map(cb => cb.value);

            if(selectedAcomp.length > currentProduct.max_acomp) {
                alert(`Você pode escolher no máximo ${currentProduct.max_acomp} acompanhamentos para este item.`);
                return;
            }

            let text = `*NOVO PEDIDO - AÇAÍ MANIA* 🍇%0A%0A`;
            text += `*Item:* ${currentProduct.name} (R$ ${currentProduct.price.toFixed(2)})%0A`;
            text += `*Acompanhamentos:* ${selectedAcomp.length > 0 ? selectedAcomp.join(', ') : 'Nenhum'}%0A%0A`;
            text += `*CLIENTE:* ${name}%0A`;
            text += `*ENDEREÇO:* ${address}, ${neighborhood}%0A`;
            text += `*PAGAMENTO:* ${payment} ${change ? '(Troco para: R$ ' + change + ')' : ''}%0A%0A`;
            text += `*TOTAL A PAGAR:* R$ ${currentProduct.price.toFixed(2)}`;

            // Substitua pelo número do WhatsApp do seu irmão (com DDI e DDD, ex: 55989XXXXXXXX)
            const whatsappNumber = "98 984098706"; 
            window.open(`https://wa.me/${whatsappNumber}?text=${text}`, '_blank');
        }
    </script>
</body>
</html>
"""