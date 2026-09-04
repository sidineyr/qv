/* global QUESTIONS, DIMENSIONS, calculateScores */
// questions.js is loaded dynamically here to keep the dashboard and survey on the same model.
const script = document.createElement("script");
script.src = "questions.js";
script.onload = initialise;
document.head.appendChild(script);

function initialise() {
  const $ = id => document.getElementById(id);
  const welcome = $("welcome"), survey = $("survey"), complete = $("complete");
  const consent = $("consent"), start = $("start-button"), resume = $("resume-button");
  const form = $("question-form"), options = $("options"), next = $("next-button");
  let current = 0;
  let answers = JSON.parse(localStorage.getItem("qv-draft") || "{}");
  const hasDraft = Object.keys(answers).length > 0 && Object.keys(answers).length < QUESTIONS.length;

  consent.addEventListener("change", () => start.disabled = !consent.checked);
  if (hasDraft) resume.classList.remove("hidden");
  start.addEventListener("click", () => { answers = {}; localStorage.removeItem("qv-draft"); openSurvey(0); });
  resume.addEventListener("click", () => openSurvey(Math.min(Object.keys(answers).length, QUESTIONS.length - 1)));
  $("exit-button").addEventListener("click", showWelcome);
  $("back-button").addEventListener("click", () => { if (current > 0) { current--; renderQuestion(); } else showWelcome(); });
  $("restart-button").addEventListener("click", () => { answers = {}; openSurvey(0); });
  form.addEventListener("submit", event => {
    event.preventDefault();
    if (answers[QUESTIONS[current].id] === undefined) return;
    if (current < QUESTIONS.length - 1) { current++; renderQuestion(); }
    else finish();
  });

  function showWelcome() { survey.classList.add("hidden"); complete.classList.add("hidden"); welcome.classList.remove("hidden"); }
  function openSurvey(index) { current = index; welcome.classList.add("hidden"); complete.classList.add("hidden"); survey.classList.remove("hidden"); renderQuestion(); }
  function renderQuestion() {
    const q = QUESTIONS[current], selected = answers[q.id];
    $("dimension-label").textContent = DIMENSIONS[q.dimension].name;
    $("progress-label").textContent = `${current + 1} de ${QUESTIONS.length}`;
    $("question-text").textContent = q.text;
    $("progress-bar").style.width = `${((current + 1) / QUESTIONS.length) * 100}%`;
    document.querySelector("[role=progressbar]").setAttribute("aria-valuenow", current + 1);
    options.innerHTML = "";
    q.options.forEach((label, value) => {
      const choice = document.createElement("label");
      choice.className = `option-card${selected === value ? " selected" : ""}`;
      choice.innerHTML = `<input type="radio" name="answer" value="${value}" ${selected === value ? "checked" : ""}><span class="option-dot"></span><span>${label}</span>`;
      choice.querySelector("input").addEventListener("change", () => {
        answers[q.id] = value; localStorage.setItem("qv-draft", JSON.stringify(answers));
        [...options.children].forEach(el => el.classList.remove("selected")); choice.classList.add("selected"); next.disabled = false;
      });
      options.appendChild(choice);
    });
    next.disabled = selected === undefined;
    next.textContent = current === QUESTIONS.length - 1 ? "Concluir" : "Continuar";
    $("back-button").textContent = current === 0 ? "Sair" : "Voltar";
    setTimeout(() => $("question-text").focus?.(), 0);
  }
  function finish() {
    const history = JSON.parse(localStorage.getItem("qv-results") || "[]");
    history.push({ id: Date.now(), date: new Date().toISOString(), answers, scores: calculateScores(answers) });
    localStorage.setItem("qv-results", JSON.stringify(history)); localStorage.removeItem("qv-draft");
    survey.classList.add("hidden"); complete.classList.remove("hidden");
  }
}

