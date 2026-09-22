from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

WHATSAPP = "5598984098706"
SENHA_ADMIN = "tilico1234"

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Açaí Mania</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}
body{background:#0b0914;color:#fff}
header{background:linear-gradient(135deg,#9333ea,#7e22ce);padding:20px 15px}
.cab{max-width:1000px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:15px}
.esq{display:flex;align-items:center;gap:12px}
.logo{background:#fff;color:#9333ea;width:45px;height:45px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:bold}
.tit h1{font-size:1.2rem}
.tit p{color:#e9d5ff;font-size:.8rem}
.dir{display:flex;gap:10px;align-items:center}
.status{padding:6px 14px;border-radius:20px;font-weight:bold;font-size:.85rem}
.aberto{background:#22c55e}
.fechado{background:#ef4444}
.btn-adm{background:#f472b6;border:none;color:#fff;padding:7px 14px;border-radius:20px;font-weight:bold;cursor:pointer}
.container{max-width:1000px;margin:25px auto;padding:0 15px}
h2{font-size:1.4rem;color:#e9d5ff;margin-bottom:5px}
.sub{color:#a78bfa;margin-bottom:25px;font-size:.9rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px}
.card{background:linear-gradient(145deg,#312e81,#4c1d95);border-radius:14px;padding:18px}
.tipo{display:inline-block;background:rgba(255,255,255,.2);padding:3px 10px;border-radius:10px;font-size:.7rem;font-weight:bold;margin-bottom:10px}
.foto{width:100%;height:140px;object-fit:cover;border-radius:10px;margin-bottom:12px;background:#2d264a}
.card h3{font-size:1rem;margin-bottom:4px}
.card p{color:#d8b4fe;font-size:.8rem;margin-bottom:12px}
.foot{display:flex;justify-content:space-between;align-items:center}
.preco{font-weight:bold;color:#86efac;font-size:1.1rem}
.btn-montar{background:#f472b6;border:none;color:#fff;padding:8px 18px;border-radius:8px;font-weight:bold;cursor:pointer}
.btn-montar:disabled{background:#555;cursor:not-allowed;opacity:.6}
.painel{display:none;margin-top:35px;background:#1e1b4b;border:3px solid#a855f7;border-radius:14px;padding:25px}
.painel.mostrar{display:block}
.head-adm{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}
.head-adm h3{color:#f9a8d4}
.btn-fechar{background:#ef4444;border:none;color:#fff;padding:6px 12px;border-radius:6px;cursor:pointer;font-weight:bold}
.secao{background:#312e81;padding:15px;border-radius:10px;margin-bottom:15px}
.secao h4{color:#ddd6fe;margin-bottom:10px}
.botoes-status{display:flex;gap:10px;margin-bottom:5px}
.btn-status{padding:10px 20px;border-radius:8px;border:none;font-weight:bold;cursor:pointer}
.btn-sim{background:#22c55e;color:#fff}
.btn-nao{background:#4b5563;color:#ddd}
.btn-ativo{box-shadow:0 0 0 2px #fff}
.lista-chk{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:8px}
.lista-chk label{background:#1e1b4b;padding:8px 12px;border-radius:6px;display:flex;align-items:center;gap:8px;cursor:pointer;font-size:.9rem}
.fundo{display:none;position:fixed;inset:0;background:rgba(0,0,0,.85);justify-content:center;align-items:center;padding:20px;z-index:9999}
.fundo.aberto{display:flex}
.janela{background:#312e81;border:3px solid#a855f7;border-radius:14px;padding:25px;max-width:420px;width:100%;max-height:90vh;overflow-y:auto}
.janela h3{margin-bottom:5px}
.janela-sub{color:#c4b5fd;font-size:.9rem;margin-bottom:15px}
.aviso-limite{color:#fcd34d;font-size:.85rem;margin-bottom:12px}
label.block{display:block;margin:15px 0 5px;color:#ddd6fe;font-weight:bold}
input[type=text], select{width:100%;padding:10px;border-radius:8px;border:2px solid#6366f1;background:#1e1b4b;color:#fff;margin-bottom:10px}
.grupo{display:flex;flex-direction:column;gap:6px;margin-bottom:10px}
.grupo label{display:flex;align-items:center;gap:8px;padding:6px;cursor:pointer;border-radius:4px;transition:background .2s}
.grupo label:hover{background:#4c1d95}
.grupo label.desativado{opacity:.5;cursor:not-allowed}
.btns{display:flex;gap:10px;margin-top:15px}
.btn-canc{flex:1;padding:12px;border:none;border-radius:8px;background:#ef4444;color:#fff;font-weight:bold;cursor:pointer}
.btn-env{flex:1;padding:12px;border:none;border-radius:8px;background:#22c55e;color:#fff;font-weight:bold;cursor:pointer}
</style>
</head>
<body>
<header>
  <div class="cab">
    <div class="esq">
      <div class="logo">AM</div>
      <div class="tit">
        <h1>Açaí Mania</h1>
        <p>Projetada, 31 - Kiola Sarney</p>
      </div>
    </div>
    <div class="dir">
      <span id="sts" class="status aberto">🟢 Aberto</span>
      <button class="btn-adm" onclick="loginAdm()">🔒 Admin</button>
    </div>
  </div>
</header>
<div class="container">
  <h2>Nosso Cardápio</h2>
  <p class="sub">Monte seu pedido do seu jeito, sem taxas extras!</p>
  <div class="grid" id="cardapio"></div>
  <div class="painel" id="painel">
    <div class="head-adm">
      <h3>⚙️ Painel de Controle</h3>
      <button class="btn-fechar" onclick="fecharPainel()">✖ Fechar</button>
    </div>
    <div class="secao">
      <h4>Status da Loja</h4>
      <div class="botoes-status">
        <button id="botao-abrir" class="btn-status btn-sim btn-ativo" onclick="mudarLoja(true)">🟢 Aberto</button>
        <button id="botao-fechar" class="btn-status btn-nao" onclick="mudarLoja(false)">🔴 Fechado</button>
      </div>
    </div>
    <div class="secao">
      <h4>Produtos Disponíveis</h4>
      <div class="lista-chk" id="lista-prod"></div>
    </div>
    <div class="secao">
      <h4>Acompanhamentos Disponíveis</h4>
      <div class="lista-chk" id="lista-ing"></div>
    </div>
  </div>
</div>
<div class="fundo" id="modal">
  <div class="janela">
    <h3 id="m-titulo"></h3>
    <p class="janela-sub" id="m-sub"></p>
    <p class="aviso-limite" id="aviso-limite"></p>
    
    <label class="block">Escolha os acompanhamentos:</label>
    <div class="grupo" id="m-ingred"></div>
    
    <label class="block">Seu Nome Completo:</label>
    <input type="text" id="m-nome" placeholder="Ex: João da Silva">
    
    <label class="block">Endereço (Rua, Número, Bairro):</label>
    <input type="text" id="m-endereco" placeholder="Ex: Rua Principal, 123 - Centro">
    
    <label class="block">Região / Referência:</label>
    <input type="text" id="m-regiao" placeholder="Ex: Kiola Sarney">
    
    <label class="block">Forma de Pagamento:</label>
    <select id="m-pagamento">
      <option value="Dinheiro">Dinheiro</option>
      <option value="Pix">Pix</option>
      <option value="Cartão">Cartão</option>
    </select>
    
    <div class="btns">
      <button class="btn-canc" onclick="fecharModal()">Cancelar</button>
      <button class="btn-env" onclick="enviar()">Enviar Pedido 🚀</button>
    </div>
  </div>
</div>
<script>
const SENHA = "SENHA_AQUI";
const ZAP = "ZAP_AQUI";
let lojaAberta = true;
let prodSel = null;
let selecionados = new Set();
const produtos = [
  {id:1,nome:"Copo Açaí 250ml",tipo:"Copo",preco:10.00,limite:2,desc:"2 acompanhamentos inclusos",img:"https://images.unsplash.com/photo-1515823064-d6e0c04616f7?w=400&h=300&fit=crop",ativo:true},
  {id:2,nome:"Copo Açaí 350ml",tipo:"Copo",preco:12.00,limite:4,desc:"4 acompanhamentos inclusos",img:"https://images.unsplash.com/photo-1502741224143-90386d7f8c82?w=400&h=300&fit=crop",ativo:true},
  {id:3,nome:"Copo Açaí de 400ml",tipo:"Copo",preco:15.00,limite:5,desc:"5 acompanhamentos inclusos",img:"https://images.unsplash.com/photo-1551024601-bec78aea7465?w=400&h=300&fit=crop",ativo:true},
  {id:4,nome:"Copo Açaí 770ml",tipo:"Copo",preco:25.00,limite:7,desc:"7 acompanhamentos inclusos",img:"https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400&h=300&fit=crop",ativo:true},
  {id:5,nome:"Combo Supremo",tipo:"Combo",preco:45.00,limite:4,desc:"4 copos de 350ml, 4 acompanhamentos em cada",img:"https://images.unsplash.com/photo-1498837167922-ddd6d2a99011?w=400&h=300&fit=crop",ativo:true},
  {id:6,nome:"Combo Mania",tipo:"Combo",preco:42.00,limite:5,desc:"3 copos de 400ml, 5 acompanhamentos em cada",img:"https://images.unsplash.com/photo-1496116218417-01d66f038a40?w=400&h=300&fit=crop",ativo:true}
];
const ingredientes = [
  {nome:"Leite Condensado",ativo:true},
  {nome:"Leite em Pó",ativo:true},
  {nome:"Paçoca",ativo:true},
  {nome:"Granola",ativo:true},
  {nome:"Flocos de Arroz",ativo:true},
  {nome:"Creme de Cupuaçu",ativo:true},
  {nome:"Banana",ativo:true},
  {nome:"Morango",ativo:true},
  {nome:"Chantilly",ativo:true},
  {nome:"Leite Ninho",ativo:true},
  {nome:"Ovomaltine",ativo:true},
  {nome:"Chocobom",ativo:true},
  {nome:"Gotas de Chocolate",ativo:true}
];
function render(){
  const grid = document.getElementById("cardapio");
  grid.innerHTML = "";
  produtos.filter(p=>p.ativo).forEach(p=>{
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <span class="tipo">${p.tipo}</span>
      <img src="${p.img}" alt="${p.nome}" class="foto" loading="lazy">
      <h3>${p.nome}</h3>
      <p>${p.desc}</p>
      <div class="foot">
        <span class="preco">R$ ${p.preco.toFixed(2).replace('.',',')}</span>
        <button class="btn-montar" onclick="abreModal(${p.id})" ${!lojaAberta?'disabled':''}>
          ${lojaAberta?'Montar':'Fechado'}
        </button>
      </div>
    `;
    grid.appendChild(card);
  });
  const lp = document.getElementById("lista-prod");
  lp.innerHTML = "";
  produtos.forEach((p,i)=>{
    const lbl = document.createElement("label");
    lbl.innerHTML = `<input type="checkbox" ${p.ativo?'checked':''} onchange="toggleProd(${i})"> ${p.nome}`;
    lp.appendChild(lbl);
  });
  const li = document.getElementById("lista-ing");
  li.innerHTML = "";
  ingredientes.forEach((ig,i)=>{
    const lbl = document.createElement("label");
    lbl.innerHTML = `<input type="checkbox" ${ig.ativo?'checked':''} onchange="toggleIng(${i})"> ${ig.nome}`;
    li.appendChild(lbl);
  });
  const el = document.getElementById("sts");
  if(lojaAberta){
    el.className = "status aberto";
    el.textContent = "🟢 Aberto";
    document.getElementById("botao-abrir").classList.add("btn-ativo");
    document.getElementById("botao-fechar").classList.remove("btn-ativo");
  }else{
    el.className = "status fechado";
    el.textContent = "🔴 Fechado";
    document.getElementById("botao-abrir").classList.remove("btn-ativo");
    document.getElementById("botao-fechar").classList.add("btn-ativo");
  }
}
function loginAdm(){
  const s = prompt("Senha do Administrador:");
  if(s===SENHA){
    document.getElementById("painel").classList.add("mostrar");
  }else if(s!==null){
    alert("Senha incorreta!");
  }
}
function fecharPainel(){
  document.getElementById("painel").classList.remove("mostrar");
}
function mudarLoja(abrir){
  lojaAberta = abrir;
  render();
}
function toggleProd(i){
  produtos[i].ativo = !produtos[i].ativo;
  render();
}
function toggleIng(i){
  ingredientes[i].ativo = !ingredientes[i].ativo;
}
function abreModal(id){
  if(!lojaAberta){alert("A loja está fechada no momento!");return;}
  prodSel = produtos.find(x=>x.id===id);
  selecionados.clear();
  
  document.getElementById("m-titulo").textContent = `${prodSel.nome} - R$ ${prodSel.preco.toFixed(2).replace('.',',')}`;
  document.getElementById("m-sub").textContent = prodSel.desc;
  document.getElementById("aviso-limite").textContent = `Escolha até ${prodSel.limite} acompanhamento(s)`;
  
  const cont = document.getElementById("m-ingred");
  cont.innerHTML = "";
  ingredientes.filter(x=>x.ativo).forEach(ig=>{
    const lbl = document.createElement("label");
    lbl.dataset.nome = ig.nome;
    lbl.innerHTML = `<input type="checkbox" value="${ig.nome}" onchange="atualizarContagem(this, '${ig.nome}')"> ${ig.nome}`;
    cont.appendChild(lbl);
  });
  
  document.getElementById("modal").classList.add("aberto");
  document.getElementById("m-nome").value = "";
  document.getElementById("m-endereco").value = "";
  document.getElementById("m-regiao").value = "";
  document.getElementById("m-pagamento").value = "Dinheiro";
}
function atualizarContagem(checkbox, nome){
  if(checkbox.checked){
    if(selecionados.size >= prodSel.limite){
      checkbox.checked = false;
      alert(`Limite de ${prodSel.limite} acompanhamento(s) atingido!`);
      return;
    }
    selecionados.add(nome);
  }else{
    selecionados.delete(nome);
  }
  atualizarBotoesIngredientes();
}
function atualizarBotoesIngredientes(){
  const labels = document.querySelectorAll("#m-ingred label");
  labels.forEach(lbl=>{
    const cb = lbl.querySelector("input");
    if(!cb.checked && selecionados.size >= prodSel.limite){
      lbl.classList.add("desativado");
      cb.disabled = true;
    }else{
      lbl.classList.remove("desativado");
      cb.disabled = false;
    }
  });
}
function fecharModal(){
  document.getElementById("modal").classList.remove("aberto");
  prodSel = null;
  selecionados.clear();
}
function enviar(){
  const nome = document.getElementById("m-nome").value.trim();
  const endereco = document.getElementById("m-endereco").value.trim();
  const regiao = document.getElementById("m-regiao").value.trim();
  const pagamento = document.getElementById("m-pagamento").value;
  
  if(!nome || !endereco){
    alert("Preencha Nome e Endereço!");
    return;
  }
  
  if(selecionados.size > prodSel.limite){
    alert(`Você pode escolher no máximo ${prodSel.limite} acompanhamento(s)!`);
    return;
  }
  const texto = encodeURIComponent(
    "🍇 *NOVO PEDIDO - AÇAÍ MANIA*%0A%0A" +
    "📦 *Produto:* " + prodSel.nome + "%0A" +
    "💰 *Valor:* R$ " + prodSel.preco.toFixed(2).replace('.',',') + "%0A" +
    "🥣 *Acompanhamentos:* " + (selecionados.size > 0 ? Array.from(selecionados).join(", ") : "Nenhum") + "%0A%0A" +
    "👤 *Cliente:* " + nome + "%0A" +
    "📍 *Endereço:* " + endereco + "%0A" +
    "🗺️ *Região:* " + (regiao || "Não informada") + "%0A" +
    "💳 *Pagamento:* " + pagamento
  );
  
  window.open("https://wa.me/" + ZAP + "?text=" + texto, "_blank");
  fecharModal();
}
render();
</script>
</body>
</html>
"""

HTML = HTML.replace("SENHA_AQUI", SENHA_ADMIN)
HTML = HTML.replace("ZAP_AQUI", WHATSAPP)

@app.get("/", response_class=HTMLResponse)
def principal():
    return HTML

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
