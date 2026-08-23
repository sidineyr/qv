const DIMENSIONS = {
  fisica: { name: "Saúde física", color: "#2e8b74" },
  emocional: { name: "Bem-estar emocional", color: "#7c6bb0" },
  social: { name: "Conexões sociais", color: "#d07855" },
  trabalho: { name: "Trabalho", color: "#3f79a8" },
  ambiente: { name: "Ambiente e segurança", color: "#b28a32" },
  proposito: { name: "Propósito e lazer", color: "#b75f79" }
};

const SCALE = ["Nunca", "Raramente", "Às vezes", "Na maioria das vezes", "Sempre"];
const QUESTIONS = [
  ["fisica", "Você tem energia suficiente para realizar suas atividades diárias?"],
  ["fisica", "Você tem dormido bem e acordado com disposição?"],
  ["fisica", "Você pratica alguma atividade física durante a semana?"],
  ["fisica", "Sua alimentação tem contribuído para você se sentir bem?"],
  ["emocional", "Você tem se sentido calmo e capaz de lidar com o estresse?"],
  ["emocional", "Você tem se sentido feliz e satisfeito com a vida?"],
  ["emocional", "Você consegue reconhecer e expressar seus sentimentos?"],
  ["emocional", "Você encontra motivação para realizar suas atividades?"],
  ["social", "Você tem pessoas com quem pode contar quando precisa?"],
  ["social", "Você se sente parte de uma comunidade ou grupo?"],
  ["social", "Você consegue reservar tempo para amigos ou familiares?"],
  ["social", "Suas relações pessoais têm sido respeitosas e acolhedoras?"],
  ["trabalho", "Você se sente valorizado no seu trabalho ou atividade principal?"],
  ["trabalho", "Você dispõe das ferramentas necessárias para realizar bem seu trabalho?"],
  ["trabalho", "Você percebe oportunidades de aprender e se desenvolver?"],
  ["trabalho", "Você consegue equilibrar trabalho, descanso e vida pessoal?"],
  ["ambiente", "Você se sente seguro onde mora e circula diariamente?"],
  ["ambiente", "Sua moradia oferece conforto, ventilação e espaço adequados?"],
  ["ambiente", "Você tem acesso satisfatório a serviços básicos e saúde?"],
  ["ambiente", "Sua situação financeira permite atender às necessidades essenciais?"],
  ["proposito", "Você reserva tempo para atividades de lazer que aprecia?"],
  ["proposito", "Você sente que suas escolhas estão alinhadas com o que é importante para você?"],
  ["proposito", "Você tem projetos ou objetivos que despertam entusiasmo?"],
  ["proposito", "Você encontra momentos de sentido, reflexão ou espiritualidade?"],
].map((item, index) => ({ id: index + 1, dimension: item[0], text: item[1], options: SCALE }));

function calculateScores(answers) {
  const grouped = {};
  Object.keys(DIMENSIONS).forEach(key => grouped[key] = []);
  QUESTIONS.forEach(q => grouped[q.dimension].push(Number(answers[q.id] ?? 0)));
  const dimensions = {};
  Object.entries(grouped).forEach(([key, values]) => {
    const average = values.reduce((sum, value) => sum + value, 0) / values.length;
    dimensions[key] = Math.round((average / 4) * 100);
  });
  const overall = Math.round(Object.values(dimensions).reduce((a, b) => a + b, 0) / Object.keys(dimensions).length);
  return { overall, dimensions };
}

