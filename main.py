from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# DADOS DA LOJA
WHATSAPP = "5598984098706"
SENHA_ADMIN = "lima1234"

IMAGENS = {
    "logo": "https://i.imgur.com/nO8pKAF.jpeg",
    "copo250": "https://i.imgur.com/QAdEt8p.jpeg",
    "copo350": "https://i.imgur.com/us6ORLD.jpeg",
    "copo400": "https://i.imgur.com/WQP0p2f.jpeg",
    "copo770": "https://i.imgur.com/51zouzO.jpeg",
    "comboSupremo": "https://i.imgur.com/58ips2n.jpeg",
    "comboMania": "https://i.imgur.com/VN4AEQU.jpeg"
}

HTML = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Açaí Mania</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}}
body{{background:#0b0914;color:#fff}}
header{{background:linear-gradient(135deg,#9333ea,#7e22ce);padding:20px 15px}}
.cab{{max-width:1000px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:15px}}
.esq{{display:flex;align-items:center;gap:12px}}
.logo{{width:55px;height:55px;border-radius:50%;object-fit:cover;border:2px solid #fff}}
.tit h1{{font-size:1.2rem}}
.tit p{{color:#e9d5ff;font-size:.8rem}}
.dir{{display:flex;gap:10px;align-items:center}}
.status{{padding:6px 14px;border-radius:20px;font-weight:bold;font-size:.85rem}}
.aberto{{background:#22c55e}}
.fechado{{background:#ef4444}}
.btn-adm{{background:#f472b6;border:none;color:#fff;padding:7px 14px;border-radius:20px;font-weight:bold;cursor:pointer}}
.container{{max-width:1000px;margin:25px auto;padding:0 15px}}
h2{{font-size:1.4rem;color:#e9d5ff;margin-bottom:5px;margin-top:40px}}
.sub{{color:#a78bfa;margin-bottom:10px;font-size:.9rem}}
.aviso{{color:#c4b5fd;font-style:italic;font-size:.85rem;margin-bottom:25px;text-align:center}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px}}
.card{{background:linear-gradient(145deg,#312e81,#4c1d95);border-radius:14px;padding:18px}}
.tipo{{display:inline-block;background:rgba(255,255,255,.2);padding:3px 10px;border-radius:10px;font-size:.7rem;font-weight:bold;margin-bottom:10px}}
.foto{{width:100%;height:160px;object-fit:cover;border-radius:10px;margin-bottom:12px;background:#2a1b5e}}
.card h3{{font-size:1rem;margin-bottom:4px}}
.card p{{color:#d8b4fe;font-size:.8rem;margin-bottom:12px}}
.foot{{display:flex;justify-content:space-between;align-items:center}}
.preco{{font-weight:bold;color:#86efac;font-size:1.1rem}}
.btn-montar{{background:#f472b6;border:none;color:#fff;padding:8px 18px;border-radius:8px;font-weight:bold;cursor:pointer}}
.btn-montar:disabled{{background:#555;cursor:not-allowed;opacity:.6}}
.painel{{display:none;margin-top:35px;background:#1e1b4b;border:3px solid #a855f7;border-radius:14px;padding:25px}}
.painel.mostrar{{display:block}}
.head-adm{{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}}
.head-adm h3{{color:#f9a8d4}}
.btn-fechar{{background:#ef4444;border:none;color:#fff;padding:6px 12px;border-radius:6px;cursor:pointer;font-weight:bold}}
.secao{{background:#312e81;padding:15px;border-radius:10px;margin-bottom:15px}}
.secao h4{{color:#ddd6fe;margin-bottom:10px}}
.botoes-status{{display:flex;gap:10px;margin-bottom:5px}}
.btn-status{{padding:10px 20px;border-radius:8px;border:none;font-weight:bold;cursor:pointer}}
.btn-sim{{background:#22c55e;color:#fff}}
.btn-nao{{background:#4b5563;color:#ddd}}
.btn-ativo{{box-shadow:0 0 0 2px #fff}}
.lista-chk{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:8px}}
.lista-chk label{{background:#1e1b4b;padding:8px 12px;border-radius:6px;display:flex;align-items:center;gap:8px;cursor:pointer;font-size:.9rem}}
.fundo{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.85);justify-content:center;align-items:center;padding:20px;z-index:9999}}
.fundo.aberto{{display:flex}}
.janela{{background:#312e81;border:3px solid #a855f7;border-radius:14px;padding:25px;max-width:420px;width:100%;max-height:90vh;overflow-y:auto}}
.janela h3{{margin-bottom:5px}}
.janela-sub{{color:#c4b5fd;font-size:.9rem;margin-bottom:15px}}
.aviso-limite{{color:#fcd34d;font-size:.85rem;margin-bottom:12px}}
label.block{{display:block;margin:15px 0 5px;color:#ddd6fe;font-weight:bold}}
input[type=text], select{{width:100%;padding:10px;border-radius:8px;border:2px solid #6366f1;background:#1e1b4b;color:#fff;margin-bottom:10px}}
.grupo{{display:flex;flex-direction:column;gap:6px;margin-bottom:10px}}
.grupo label{{display:flex;align-items:center;gap:8px;padding:6px;cursor:pointer;border-radius:4px;transition:background .2s}}
.grupo label:hover{{background:#4c1d95}}
.grupo label.desativado{{opacity:.5;cursor:not-allowed}}
.btns{{display:flex;gap:10px;margin-top:15px}}
.btn-canc{{flex:1;padding:12px;border:none;border-radius:8px;background:#ef4444;color:#fff;font-weight:bold;cursor:pointer}}
.btn-env{{flex:1;padding:12px;border:none;border-radius:8px;background:#22c55e;color:#fff;font-weight:bold;cursor:pointer}}
.grid-acomp{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-top:15px}}
.item-acomp{{background:#1e1b4b;padding:10px;border-radius:8px;text-align:center;font-size:.9rem}}
.grid-cremes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:15px;margin-top:15px}}
.item-creme{{background:#1e1b4b;padding:15px;border-radius:10px;text-align:center}}
.valor-creme{{color:#fcd34d;font-weight:bold;margin-top:5px}}
.creme-checkbox{{margin-top:10px}}
</style>
</head>
<body>
<header>
  <div class="cab">
    <div class="esq">
      <img src="{IMAGENS['logo']}" alt="Logo Açaí Mania" class="logo">
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
  <p class="aviso">📸 *Imagens meramente ilustrativas. Você é quem monta seu açaí do jeitinho que quiser!*</p>
  <div class="grid" id="cardapio"></div>

  <h2>🍬 Acompanhamentos Disponíveis</h2>
  <p class="sub">Inclusos no seu copo, de acordo com a quantidade escolhida:</p>
  <div class="grid-acomp" id="lista-acompanhamenos"></div>

  <h2>🍫 Cremes Adicionais</h2>
  <p class="sub">Acrescente ao seu pedido — R$ 4,00 cada:</p>
  <div class="grid-cremes" id="lista-cremes"></div>

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

    <label class="block">Adicionar Cremes (opcional):</label>
    <div class="grupo creme-checkbox" id="m-cremes"></div>
    
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
const SENHA = "{SENHA_ADMIN}";
const ZAP = "{WHATSAPP}";
let lojaAberta = true;
let prodSel = null;
let selecionados = new Set();
let cremesSel = new Set();

const imagens = {{
    logo: "{IMAGENS['logo']}",
    copo250: "{IMAGENS['copo250']}",
    copo350: "{IMAGENS['copo350']}",
    copo400: "{IMAGENS['copo400']}",
    copo770: "{IMAGENS['copo770']}",
    comboSupremo: "{IMAGENS['comboSupremo']}",
    comboMania: "{IMAGENS['comboMania']}"
}};

const produtos = [
  {{id:1,nome:"Copo Açaí 250ml",tipo:"Copo",preco:10.00,limite:2,desc:"2 acompanhamentos inclusos",img:imagens.copo250,ativo:true}},
  {{id:2,nome:"Copo Açaí 350ml",tipo:"Copo",preco:12.00,limite:4,desc:"4 acompanhamentos inclusos",img:imagens.copo350,ativo:true}},
  {{id:3,nome:"Copo Açaí de 400ml",tipo:"Copo",preco:15.00,limite:5,desc:"5 acompanhamentos inclusos",img:imagens.copo400,ativo:true}},
  {{id:4,nome:"Copo Açaí 770ml",tipo:"Copo",preco:25.00,limite:7,desc:"7 acompanhamentos inclusos",img:imagens.copo770,ativo:true}},
  {{id:5,nome:"Combo Supremo",tipo:"Combo",preco:45.00,limite:4,desc:"4 copos de 350ml, 4 acompanhamentos em cada",img:imagens.comboSupremo,ativo:true}},
  {{id:6,nome:"Combo Mania",tipo:"Combo",preco:42.00,limite:5,desc:"3 copos de 400ml, 5 acompanhamentos em cada",img:imagens.comboMania,ativo:true}}
];

const acompanhamentos = [
  {{nome:"Amendoim",ativo:true}},
  {{nome:"Paçoca",ativo:true}},
  {{nome:"Granola",ativo:true}},
  {{nome:"Tapioca",ativo:true}},
  {{nome:"Cereal Crocante",ativo:true}},
  {{nome:"Sucrilhos",ativo:true}},
  {{nome:"Disquete",ativo:true}},
  {{nome:"Banana",ativo:true}},
  {{nome:"Uva",ativo:true}},
  {{nome:"Morango",ativo:true}},
  {{nome:"Leite em Pó",ativo:true}},
  {{nome:"Bis",ativo:true}},
  {{nome:"Jujuba",ativo:true}}
];

const cremes = [
  {{nome:"Creme de Nutella",valor:4.00,ativo:true}},
  {{nome:"Creme de Ninho",valor:4.00,ativo:true}}
];

function render(){{
  const grid = document.getElementById("cardapio");
  grid.innerHTML = "";
  produtos.filter(p=>p.ativo).forEach(p=>{{
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <span class="tipo">${{p.tipo}}</span>
      <img src="${{p.img}}" alt="${{p.nome}}" class="foto" loading="lazy">
      <h3>${{p.nome}}</h3>
      <p>${{p.desc}}</p>
      <div class="foot">
        <span class="preco">R$ ${{p.preco.toFixed(2).replace('.',',')}}</span>
        <button class="btn-montar" onclick="abreModal(${{p.id}})" ${{!lojaAberta?'disabled':''}}>
          ${{lojaAberta?'Montar':'Fechado'}}
        </button>
      </div>
    `;
    grid.appendChild(card);
  }});

  const ac = document.getElementById("lista-acompanhamenos");
  ac.innerHTML = "";
  acompanhamentos.filter(a=>a.ativo).forEach(a=>{{
    ac.innerHTML += `<div class="item-acomp">✅ ${{a.nome}}</div>`;
  }});

  const cr = document.getElementById("lista-cremes");
  cr.innerHTML = "";
  cremes.filter(c=>c.ativo).forEach(c=>{{
    cr.innerHTML += `<div class="item-creme"><strong>${{c.nome}}</strong><div class="valor-creme">R$ ${{c.valor.toFixed(2).replace('.',',')}}</div></div>`;
  }});

  const lp = document.getElementById("lista-prod");
  lp.innerHTML = "";
  produtos.forEach((p,i)=>{{
    const lbl = document.createElement("label");
    lbl.innerHTML = `<input type="checkbox" ${{p.ativo?'checked':''}} onchange="toggleProd(${{i}})"> ${{p.nome}}`;
    lp.appendChild(lbl);
  }});

  const li = document.getElementById("lista-ing");
  li.innerHTML = "";
  acompanhamentos.forEach((ig,i)=>{{
    const lbl = document.createElement("label");
    lbl.innerHTML = `<input type="checkbox" ${{ig.ativo?'checked':''}} onchange="toggleIng(${{i}})"> ${{ig.nome}}`;
    li.appendChild(lbl);
  }});

  const el = document.getElementById("sts");
  if(lojaAberta){{
    el.className = "status aberto";
    el.textContent = "🟢 Aberto";
    document.getElementById("botao-abrir").classList.add("btn-ativo");
    document.getElementById("botao-fechar").classList.remove("btn-ativo");
  }}else{{
    el.className = "status fechado";
    el.textContent = "🔴 Fechado";
    document.getElementById("botao-abrir").classList.remove("btn-ativo");
    document.getElementById("botao-fechar").classList.add("btn-ativo");
  }}
}}

function loginAdm(){{
  const s = prompt("Senha do Administrador:");
  if(s===SENHA){{
    document.getElementById("painel").classList.add("mostrar");
  }}else if(s!==null){{
    alert("Senha incorreta!");
  }}
}}

function fecharPainel(){{
  document.getElementById("painel").classList.remove("mostrar");
}}

function mudarLoja(abrir){{
  lojaAberta = abrir;
  render();
}}

function toggleProd(i){{
  produtos[i].ativo = !produtos[i].ativo;
  render();
}}

function toggleIng(i){{
  acompanhamentos[i].ativo = !acompanhamentos[i].ativo;
  render();
}}

function abreModal(id){{
  if(!lojaAberta){{alert("A loja está fechada no momento!");return;}}
  prodSel = produtos.find(x=>x.id===id);
  selecionados.clear();
  cremesSel.clear();
  
  document.getElementById("m-titulo").textContent = `${{prodSel.nome}} - R$ ${{prodSel.preco.toFixed(2).replace('.',',')}}`;
  document.getElementById("m-sub").textContent = prodSel.desc;
  document.getElementById("aviso-limite").textContent = `Escolha até ${{prodSel.limite}} acompanhamento(s)`;
  
  const cont = document.getElementById("m-ingred");
  cont.innerHTML = "";
  acompanhamentos.filter(x=>x.ativo).forEach(ig=>{{
    const lbl = document.createElement("label");
    lbl.innerHTML = `<input type="checkbox" value="${{ig.nome}}" onchange="atualizarContagem(this, '${{ig.nome}}')"> ${{ig.nome}}`;
    cont.appendChild(lbl);
  }});

  const contCr = document.getElementById("m-cremes");
  contCr.innerHTML = "";
  cremes.filter(x=>x.ativo).forEach(cr=>{{
    const lbl = document.createElement("label");
    lbl.innerHTML = `<input type="checkbox" value="${{cr.nome}}" onchange="alternarCreme(this, '${{cr.nome}}')"> ${{cr.nome}} - R$ ${{cr.valor.toFixed(2).replace('.',',')}}`;
    contCr.appendChild(lbl);
  }});
  
  document.getElementById("modal").classList.add("aberto");
  document.getElementById("m-nome").value = "";
  document.getElementById("m-endereco").value = "";
  document.getElementById("m-regiao").value = "";
  document.getElementById("m-pagamento").value = "Dinheiro";
}}

function atualizarContagem(checkbox, nome){{
  if(checkbox.checked){{
    if(selecionados.size >= prodSel.limite){{
      checkbox.checked = false;
      alert(`Limite de ${{prodSel.limite}} acompanhamento(s) atingido!`);
      return;
    }}
    selecionados.add(nome);
  }}else{{
    selecionados.delete(nome);
  }}
}}

function alternarCreme(checkbox, nome){{
  if(checkbox.checked) cremesSel.add(nome);
  else cremesSel.delete(nome);
}}

function fecharModal(){{
  document.getElementById("modal").classList.remove("aberto");
  prodSel = null;
  selecionados.clear();
  cremesSel.clear();
}}

function enviar(){{
  const nome = document.getElementById("m-nome").value.trim();
  const endereco = document.getElementById("m-endereco").value.trim();
  const regiao = document.getElementById("m-regiao").value.trim();
  const pagamento = document.getElementById("m-pagamento").value;
  
  if(!nome || !endereco){{ alert("Preencha Nome e Endereço!"); return; }}
  
  if(selecionados.size > prodSel.limite){{
    alert(`Máximo de ${{prodSel.limite}} acompanhamento(s)!`);
    return;
  }}

  const totalAdicional = cremesSel.size * 4.00;
  const valorTotal = prodSel.preco + totalAdicional;
  const textoCremes = cremesSel.size > 0 
    ? `🍫 Cremes: ${{[...cremesSel].join(", ")}} (+ R$ ${{totalAdicional.toFixed(2).replace('.',',')}})\\n` : "";

  const mensagem = encodeURIComponent(
    `🍇 *NOVO PEDIDO - AÇAÍ MANIA*\\n\\n` +
    `📦 *Produto:* ${{prodSel.nome}}\\n` +
    `💰 *Valor:* R$ ${{prodSel.preco.toFixed(2).replace('.',',')}}\\n` +
    textoCremes +
    `💵 *Total:* R$ ${{valorTotal.toFixed(2).replace('.',',')}}\\n\\n` +
    `🥣 *Acompanhamentos:* ${{[...selecionados].join(", ") || "Nenhum"}}\\n\\n` +
    `👤 *Cliente:* ${{nome}}\\n` +
    `📍 *Endereço:* ${{endereco}}\\n` +
    `🗺️ *Região:* ${{regiao || "Não informada"}}\\n` +
    `💳 *Pagamento:* ${{pagamento}}`
  );
  
  window.open(`https://wa.me/${ZAP}?text=${mensagem}`, "_blank");
  fecharModal();
}}

render();
</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def principal():
    return HTML

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
