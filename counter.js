(function () {
  const container = document.getElementById('completion-counter');
  const label = document.getElementById('completion-total');
  const endpoint = String(window.QV_COUNTER_API || '').replace(/\/$/, '');
  if (!container || !label || !endpoint) return;
  container.hidden = false;
  function render(total) {
    if (!Number.isSafeInteger(total) || total < 0) throw new Error('Resposta inválida');
    label.textContent = total === 0 ? 'Seja a primeira pessoa a concluir este questionário!' : `${total.toLocaleString('pt-BR')} ${total === 1 ? 'pessoa já concluiu' : 'pessoas já concluíram'} o QV!`;
  }
  function unavailable() { label.textContent = 'Contador temporariamente indisponível'; }
  async function request(method) {
    const options = {method, cache: 'no-store', headers: {Accept: 'application/json'}};
    if (method === 'POST') { options.headers['Content-Type'] = 'application/json'; options.body = '{"completed":true}'; }
    const response = await fetch(`${endpoint}/completions`, options);
    if (!response.ok) throw new Error('Falha no contador');
    const data = await response.json(); render(data.total); return data.total;
  }
  request('GET').catch(unavailable);
  window.QVCounter = {recordCompletion: () => request('POST').catch(unavailable)};
}());
