/* global DIMENSIONS */
const history = JSON.parse(localStorage.getItem("qv-results") || "[]");
const $ = id => document.getElementById(id);

if (!history.length) {
  $("empty-state").classList.remove("hidden");
  $("export-button").classList.add("hidden");
} else {
  $("dashboard-content").classList.remove("hidden");
  const latest = history[history.length - 1];
  const entries = Object.entries(latest.scores.dimensions).sort((a, b) => b[1] - a[1]);
  const best = entries[0], attention = entries[entries.length - 1];
  $("result-date").textContent = `Última resposta em ${formatDate(latest.date)}`;
  $("overall-score").textContent = latest.scores.overall;
  $("overall-label").textContent = scoreLabel(latest.scores.overall);
  $("best-dimension").textContent = DIMENSIONS[best[0]].name;
  $("best-copy").textContent = `${best[1]} pontos · seu destaque atual`;
  $("attention-dimension").textContent = DIMENSIONS[attention[0]].name;
  $("attention-copy").textContent = `${attention[1]} pontos · merece mais cuidado`;
  $("insight-title").textContent = `Um próximo passo em ${DIMENSIONS[attention[0]].name.toLowerCase()}`;
  $("insight-copy").textContent = insightFor(attention[0]);

  Object.entries(latest.scores.dimensions).forEach(([key, value]) => {
    const row = document.createElement("div"); row.className = "dimension-row";
    row.innerHTML = `<div class="dimension-copy"><span>${DIMENSIONS[key].name}</span><strong>${value}</strong></div><div class="bar-track"><div class="bar-fill" style="width:${value}%;background:${DIMENSIONS[key].color}"></div></div>`;
    $("dimension-bars").appendChild(row);
  });

  suggestionsFor(attention[0]).forEach(text => {
    const item = document.createElement("div"); item.className = "suggestion"; item.innerHTML = `<span>✓</span><p>${text}</p>`; $("suggestions").appendChild(item);
  });
  [...history].reverse().forEach((item, index) => {
    const row = document.createElement("div"); row.className = "history-item";
    row.innerHTML = `<div><strong>${index === 0 ? "Resposta mais recente" : "Resposta anterior"}</strong><span>${formatDate(item.date)}</span></div><div class="history-score"><strong>${item.scores.overall}</strong><span>/100</span></div>`; $("history").appendChild(row);
  });
}

$("export-button").addEventListener("click", () => {
  const header = ["data", "indice_geral", ...Object.keys(DIMENSIONS)];
  const rows = history.map(x => [x.date, x.scores.overall, ...Object.keys(DIMENSIONS).map(k => x.scores.dimensions[k])]);
  const csv = [header, ...rows].map(row => row.join(",")).join("\n");
  const link = document.createElement("a"); link.href = URL.createObjectURL(new Blob([csv], {type:"text/csv"})); link.download = "quality-view-resultados.csv"; link.click(); URL.revokeObjectURL(link.href);
});
$("clear-button")?.addEventListener("click", () => { if (confirm("Apagar todo o histórico de respostas deste navegador?")) { localStorage.removeItem("qv-results"); location.reload(); } });

function formatDate(date) { return new Intl.DateTimeFormat("pt-BR", { dateStyle: "long", timeStyle: "short" }).format(new Date(date)); }
function scoreLabel(score) { return score >= 80 ? "Equilíbrio muito positivo" : score >= 60 ? "Bom equilíbrio geral" : score >= 40 ? "Há espaço para cuidar" : "Momento de atenção"; }
function insightFor(key) { return ({fisica:"Pequenas rotinas consistentes tendem a funcionar melhor do que grandes mudanças passageiras.",emocional:"Reconhecer como você está é um começo importante. Reserve espaço para nomear emoções e pedir apoio.",social:"Conexões de qualidade podem começar com um contato simples e intencional.",trabalho:"Observe qual ajuste concreto pode tornar sua rotina mais sustentável nesta semana.",ambiente:"Conforto e segurança influenciam o bem-estar. Comece pelo aspecto do ambiente que está ao seu alcance.",proposito:"Atividades com significado não precisam ser grandiosas; precisam fazer sentido para você."})[key]; }
function suggestionsFor(key) { return ({fisica:["Escolha um horário regular para dormir durante três dias.","Inclua dez minutos de movimento em um momento possível do dia."],emocional:["Faça uma pausa breve e registre como se sente.","Converse com alguém de confiança ou procure apoio profissional se precisar."],social:["Envie uma mensagem para alguém importante hoje.","Planeje um encontro simples, sem cobrança de perfeição."],trabalho:["Defina uma prioridade realista para o próximo dia.","Converse sobre uma ferramenta ou limite que faria diferença na rotina."],ambiente:["Escolha um pequeno ponto da casa para tornar mais confortável.","Mapeie um serviço ou recurso público disponível perto de você."],proposito:["Reserve vinte minutos para uma atividade que lhe dá prazer.","Escreva um objetivo pequeno que gostaria de realizar neste mês."]})[key]; }

