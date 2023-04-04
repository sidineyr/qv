import pandas as pd
from survey import Survey

# Definir as perguntas e respostas
questions = {'1. Qual é o seu peso atual?"': [' Abaixo do peso ideal "', ' Peso ideal "', ' Sobrepeso"', ' Obeso"'], '2.  Qual é a sua altura atual? "': [' Menos de 1,60m "', ' Entre 1,60m e 1,70m "', ' Entre 1,70m e 1,80m "', ' Mais de 1,80m"'], '3. Você já teve alguma doença crônica, como diabetes ou hipertensão? "': [' Sim "', ' Não"'], '4. Com que frequência você realiza exames de rotina para avaliar sua saúde? "': [' Anualmente "', ' A cada dois anos "', ' A cada três anos "', ' Raramente e) Nunca"'], '5. Você fuma? "': [' Sim, regularmente "', ' Sim, ocasionalmente "', ' Não"'], '6. Com que frequência você consome bebidas alcoólicas? "': [' Diariamente "', ' Algumas vezes por semana "', ' Algumas vezes por mês "', ' Raramente "', ' Nunca"'], '7. Você segue uma dieta saudável e balanceada? "': [' Sim, sempre "', ' Na maioria das vezes "', ' Às vezes "', ' Raramente "', ' Nunca"'], '8. Com que frequência você pratica atividade física? "': [' Diariamente "', ' 3-4 vezes por semana "', ' 1-2 vezes por semana "', ' Raramente e) Nunca"'], '.   Você costuma ter uma boa qualidade de sono? "': [' Sim, quase sempre "', ' Sim, na maioria das vezes "', ' Às vezes "', ' Raramente "', ' Nunca"'], '10. Como você se sente em relação à sua saúde geral? "': [' Excelente "', ' Boa "', ' Regular "', ' Ruim "', ' Muito ruim"'], '11. Com que frequência você se sente triste ou deprimido? "': [' Raramente "', ' Algumas vezes por mês "', ' Algumas vezes por semana "', ' Diariamente"', ' Constantemente"'], '12. Você já foi diagnosticado com alguma doença mental, como depressão ou ansiedade? "': [' Sim"', ' Não"'], '13. Com que frequência você se sente ansioso ou estressado? "': [' Raramente "', ' Algumas vezes por mês "', ' Algumas vezes por semana "', ' Diariamente "', ' Constantemente"'], '14. Com que frequência você se sente feliz e satisfeito com a vida? "': [' Diariamente "', ' Na maioria das vezes "', ' Às vezes "', ' Raramente "', ' Nunca"'], '15. Com que frequência você se sente cansado e sem energia? "': [' Raramente "', ' Algumas vezes por mês "', ' Algumas vezes por semana "', ' Diariamente "', ' Constantemente"'], '16. Com que frequência você tem problemas para dormir? "': [' Raramente "', ' Algumas vezes por mês "', ' Algumas vezes por semana "', ' Diariamente "', ' Constantemente"'], '17. Com que frequência você se sente irritado ou frustrado? "': [' Raramente "', ' Algumas vezes por mês "', ' Algumas vezes por semana "', ' Diariamente "', ' Constantemente"'], '18. Com que frequência você se sente motivado e animado para fazer as coisas? "': [' Diariamente "', ' Na maioria das vezes "', ' Às vezes d) "', 'ramente "', ' Nunca"'], '19.Você já considerou procurar ajuda profissional para problemas de saúde mental? "': [' Sim "', ' Não"'], '20.Você se sente confortável em compartilhar seus sentimentos e emoções com outras pessoas? "': [' Sim, sempre "', ' Na maioria das vezes "', ' Às vezes "', ' Raramente "', ' Nunca"'], '21. Com que frequência você se encontra com amigos ou familiares? "': [' Diariamente "', ' Algumas vezes por semana "', ' Algumas vezes por mês "', ' Raramente "', ' Nunca"'], '22. Com que frequência você se comunica com amigos ou familiares que moram longe? "': [' Diariamente "', ' Algumas vezes por semana "', ' Algumas vezes por mês "', ' Raramente e) Nunca"'], '23. Com que frequência você participa de atividades em grupo, como festas ou reuniões sociais? "': [' Diariamente "', ' Algumas vezes por semana "', ' Algumas vezes por mês "', ' Raramente "', ' Nunca"'], '24. Você se sente confortável ao conhecer novas pessoas? "': [' Sim, sempre "', ' Na maioria das vezes "', ' Às vezes "', ' Raramente "', ' Nunca"'], '25. Você tem amigos ou familiares que você pode confiar e conversar sobre assuntos pessoais? "': [' Sim, muitos "', ' Sim, alguns "', ' Poucos "', ' Nenhum"'], '26. Com que frequência você se sente sozinho ou isolado socialmente? "': [' Raramente "', ' Algumas vezes por mês "', ' Algumas vezes por semana "', ' Diariamente "', ' Constantemente"'], '27. Você se sente parte de uma comunidade ou grupo social? "': [' Sim, completamente "', ' Em grande parte "', ' Mais ou menos "', ' Pouco "', ' Nada"'], '28. Você tem um parceiro amoroso com quem pode contar? "': [' Sim, um "', ' Sim, vários ao longo do tempo "', ' Não, atualmente solteiro "', ' Não, nunca tive"'], '29. Você acha fácil se comunicar com outras pessoas? "': [' Sim, sempre "', ' Na maioria das vezes "', ' Às vezes "', ' Raramente "', ' Nunca"'], '30. Você sente que tem um equilíbrio saudável entre o tempo gasto com amigos/família e o tempo dedicado a si mesmo? "': [' Sim, sempre "', ' Na maioria das vezes "', ' Às vezes "', ' Raramente "', ' Nunca"'], '31. Qual é a sua renda mensal? "': [' Menos de R$ 1.000 "', ' R$ 1.000 - R$ 2.000 "', ' R$ 2.000 - R$ 4.000 "', ' R$ 4.000 - R$ 6.000 e) Mais de R$ 6.000"'], '32. Você tem dívidas atualmente? "': [' Sim, muitas "', ' Sim, algumas "', ' Poucas "', ' Nenhuma"'], '33. Você tem um emprego atualmente? "': [' Sim, emprego fixo "', ' Sim, trabalho temporário "', ' Não, estou desempregado "', ' Não, estou estudando"'], '34. Você tem um plano de aposentadoria? "': [' Sim, contribuo para a previdência social "', ' Sim, tenho um plano privado de aposentadoria "', ' Não, ainda não comecei a pensar sobre isso "', ' Não, não posso pagar um plano de aposentadoria"'], '35. Qual é o seu nível de educação? "': [' Ensino Fundamental incompleto "', ' Ensino Fundamental completo "', ' Ensino Médio incompleto "', ' Ensino Médio completo "', ' Ensino Superior completo"'], '36. Você tem acesso a serviços de saúde? "': [' Sim, por meio do serviço público "', ' Sim, por meio de um plano de saúde privado "', ' Não, não tenho acesso a nenhum tipo de serviço de saúde"'], '37. Você tem um carro? a) Sim, próprio e pago "': [' Sim, próprio e parcelado "', ' Sim, alugado ou emprestado "', ' Não, não tenho um carro"'], '38. Qual é o seu padrão de moradia atual? "': [' Alugado, em condições precárias "', ' Alugado, em condições razoáveis "', ' Alugado, em boas condições"', ' Próprio, em condições precárias "', ' Próprio, em boas condições"'], '39. Você tem acesso a internet em casa? "': [' Sim, internet rápida "', ' Sim, internet lenta "', ' Sim, mas uso apenas dados móveis"', ' Não, não tenho acesso a internet em casa"'], '40. Qual foi a sua última viagem de férias? "': [' Não tive férias recentemente "', ' Fiquei em casa ou cidade "', ' Fui para uma cidade próxima "', ' Fui para uma cidade distante "', ' Fui para fora do país"'], '41. Qual é o tipo de habitação onde você mora? "': [' Casa "', ' Apartamento "', ' Outro"'], '42. Qual é a sua satisfação com a localização da sua habitação? "': [' Muito satisfeito "', ' Satisfeito "', ' Neutro "', ' Insatisfeito "', ' Muito insatisfeito"'], '43. Qual é a sua satisfação com o tamanho da sua habitação? "': [' Muito satisfeito "', ' Satisfeito "', ' Neutro "', ' Insatisfeito "', ' Muito insatisfeito"'], '44. Como é a iluminação na sua habitação? "': [' Boa "', ' Razoável "', ' Ruim "', ' Inexistente"'], '45. Como é a ventilação na sua habitação? "': [' Boa "', ' Razoável "', ' Ruim "', ' Inexistente"'], '46. Como é a temperatura na sua habitação? "': [' Confortável "', ' Um pouco desconfortável "', ' Muito desconfortável"'], '47. Como é a segurança na sua habitação? "': [' Muito segura "', ' Segura "', ' Neutra "', ' Insegura "', ' Muito insegura"'], '48. Como é o ruído na sua habitação? "': [' Baixo "', ' Razoável "', ' Alto"'], '49. Qual é a qualidade do ar na sua habitação? "': [' Boa "', ' Razoável "', ' Ruim"'], '50. Como é o acesso aos serviços básicos na sua área de moradia? "': [' Fácil "', ' Razoável "', ' Difícil"'], '51. Qual é o seu nível de escolaridade? "': [' Ensino fundamental incompleto "', ' Ensino fundamental completo "', ' Ensino médio incompleto "', ' Ensino médio completo "', ' Ensino superior incompleto "', ' Ensino superior completo"'], '52. Você tem algum curso técnico ou profissionalizante? "': [' Sim "', ' Não"'], '53. Qual é o seu nível de habilidade em informática? "': [' Avançado "', ' Intermediário "', ' Básico "', ' Nenhum"'], '54. Você tem conhecimento em algum idioma estrangeiro? "': [' Sim, inglês "', ' Sim, espanhol "', ' Sim, outro idioma "', ' Não"'], '55. Qual é o seu nível de habilidade em comunicação oral? "': [' Excelente "', ' Bom "', ' Regular "', ' Ruim"'], '56. Qual é o seu nível de habilidade em comunicação escrita? "': [' Excelente "', ' Bom "', ' Regular "', ' Ruim"'], '57. Você tem habilidades em artes, como música, teatro ou dança? "': [' Sim "', ' Não"'], '58. Qual é o seu nível de habilidade em matemática? "': [' Excelente "', ' Bom "', ' Regular "', ' Ruim"'], '59. Qual é o seu nível de habilidade em liderança e gestão de equipe? "': [' Excelente "', ' Bom "', ' Regular "', ' Ruim"'], '60. Você tem habilidades em alguma área específica, como culinária, marcenaria ou costura? "': [' Sim "', ' Não"'], '61. Você já foi vítima de algum tipo de violência (roubo, assalto, agressão) nos últimos 12 meses? "': [' Sim "', ' Não"'], '62. Você se sente seguro(a) ao caminhar em sua rua ou bairro? "': [' Sempre "', ' Às vezes "', ' Raramente "', ' Nunca"'], '63. Você já presenciou algum ato de violência em seu bairro ou região? "': [' Sim "', ' Não"'], '64. Você conhece seus vizinhos? "': [' Sim, muito bem "', ' Sim, razoavelmente bem "', ' Não, apenas de vista "', ' Não, não os conheço"'], '65. Há policiamento regular em sua rua ou bairro? "': [' Sim, sempre "', ' Às vezes "', ' Raramente"', ' Não"'], '66. Você tem medo de ser vítima de um crime violento? "': [' Sim, muito medo "', ' Algum medo "', ' Pouco medo "', ' Nenhum medo"'], '67. Sua casa tem sistema de segurança (alarme, câmeras de vigilância, etc.)? "': [' Sim "', ' Não"'], '68. Você costuma tomar medidas de precaução para evitar ser vítima de um crime (ex. evitar andar sozinho à noite, trancar portas e janelas, etc.)? "': [' Sempre "', ' Às vezes "', ' Raramente "', ' Nunca"'], '69. Você se sente seguro(a) em espaços públicos, como parques e praças? "': [' Sempre "', ' Às vezes "', ' Raramente "', ' Nunca"'], '70. Você já participou de programas de educação ou prevenção de violência em sua comunidade? "': [' Sim "', ' Não"'], '71. Quantas vezes por semana você consome frutas frescas? "': [' Todos os dias "', ' 4-6 vezes por semana "', ' 2-3 vezes por semana "', ' Uma vez por semana ou menos"'], '72. Quantas vezes por semana você consome verduras e legumes? "': [' Todos os dias "', ' 4-6 vezes por semana "', ' 2-3 vezes por semana "', ' Uma vez por semana ou menos"'], '73. Você consome alimentos ricos em gordura (ex. frituras, fast food, embutidos) com que frequência? "': [' Nunca "', ' Raramente (1-2 vezes por semana) "', ' Às vezes (3-4 vezes por semana) "', ' Com frequência (mais de 5 vezes por semana)"'], '74. Você consome alimentos industrializados (ex. biscoitos, salgadinhos, refrigerantes) com que frequência? "': [' Nunca "', ' Raramente (1-2 vezes por semana) "', ' Às vezes (3-4 vezes por semana) "', ' Com frequência (mais de 5 vezes por semana)"'], '75. Você consome carne vermelha com que frequência? "': [' Todos os dias "', ' 4-6 vezes por semana "', ' 2-3 vezes por semana "', ' Uma vez por semana ou menos"'], '76. Você consome peixe com que frequência? "': [' Todos os dias "', ' 4-6 vezes por semana "', ' 2-3 vezes por semana "', ' Uma vez por semana ou menos"'], '77. Você consome laticínios com que frequência? "': [' Todos os dias "', ' 4-6 vezes por semana "', ' 2-3 vezes por semana "', ' Uma vez por semana ou menos"'], '78. Com que frequência você consome alimentos ricos em açúcar (ex. doces, sorvetes, açúcar refinado)? "': [' Nunca "', ' Raramente (1-2 vezes por semana) "', ' Às vezes (3-4 vezes por semana) "', ' Com frequência (mais de 5 vezes por semana)"'], '79. Quantos copos de água(300ml) você bebe por dia, em média? "': [' Menos de 2 copos "', ' 2-4 copos "', ' 5-8 copos "', ' Mais de 8 copos"'], '80. Você tem alguma restrição alimentar por motivo de saúde ou dieta? "': [' Sim "', ' Não"'], '81. Você está satisfeito com a sua remuneração atual? "': [' Sim, muito satisfeito "', ' Sim, razoavelmente satisfeito "', ' Não muito satisfeito "', ' Insatisfeito"'], '82. Você tem acesso a benefícios como plano de saúde, vale-refeição, vale-transporte, entre outros? "': [' Sim, todos os benefícios "', ' Sim, alguns benefícios "', ' Não tenho acesso a benefícios "', ' Não sei"'], '83. uantas horas por dia você trabalha, em média? "': [' Menos de 6 horas "', ' Entre 6 e 8 horas "', ' Entre 8 e 10 horas "', ' Mais de 10 horas"'], '84.  Você tem flexibilidade de horários ou de trabalho remoto? "': [' Sim, tenho flexibilidade de horários e trabalho remoto "', ' Sim, tenho flexibilidade de horários "', ' Sim, tenho trabalho remoto "', ' Não tenho flexibilidade de horários ou trabalho remoto"'], '85. Você considera que possui as ferramentas e recursos necessários para desempenhar seu trabalho adequadamente? "': [' Sim, tenho tudo o que preciso "', ' Sim, tenho a maioria das coisas que preciso "', ' Não tenho tudo o que preciso, mas consigo me virar "', ' Não tenho o que preciso para desempenhar meu trabalho adequadamente"'], '86. Como você avalia o seu relacionamento com seus colegas de trabalho? "': [' Excelente "', ' Bom "', ' Regular "', ' Ruim"'], '87. Você considera que seu trabalho é estressante? "': [' Não, não é estressante "', ' É um pouco estressante, mas suportável "', ' É bastante estressante, mas consigo lidar "', ' É extremamente estressante e afeta minha saúde física e mental"'], '88.Você sente que tem oportunidades de crescimento e desenvolvimento na empresa? "': [' Sim, muitas oportunidades "', ' Sim, algumas oportunidades "', ' Poucas oportunidades "', ' Nenhuma oportunidade"'], '89.Você se sente valorizado pela empresa e pelos seus superiores?"': [' Sim, muito valorizado"', ' Sim, razoavelmente valorizado "', ' Não me sinto muito valorizado "', ' Não me sinto valorizado"'], '90. Você está satisfeito com a sua carreira atual? "': [' Sim, muito satisfeito "', ' Sim, razoavelmente satisfeito "', ' Não muito satisfeito"', ' Insatisfeito"'], '91. Com que frequência você pratica atividades de lazer? "': [' Diariamente "', ' Semanalmente "', ' Mensalmente "', ' Raramente"'], '92. Qual o tipo de atividade de lazer que você mais gosta? "': [' Esportes "', ' Artes e cultura "', ' Viagens "', ' Outros (especifique)"'], '93. Você tem tempo suficiente para se dedicar a atividades de lazer? "': [' Sim, bastante tempo "', ' Sim, um pouco de tempo "', ' Não muito tempo "', ' Não tenho tempo para atividades de lazer"'], '94. Você tem recursos financeiros suficientes para realizar as atividades de lazer que gostaria? "': [' Sim, sempre "', ' Sim, na maioria das vezes "', ' Às vezes "', ' Raramente"'], '95. Você se sente motivado e energizado após praticar atividades de lazer? "': [' Sim, sempre "', ' Na maioria das vezes "', ' Às vezes "', ' Raramente"'], '96. Você costuma praticar atividades de lazer em grupo ou sozinho? "': [' Em grupo "', ' Sozinho "', ' Tanto faz"'], '97. Você considera que as atividades de lazer que pratica são saudáveis e benéficas para a sua saúde física e mental? "': [' Sim, totalmente saudáveis "', ' Sim, em sua maioria "', ' Nem sempre "', ' Não, são prejudiciais à minha saúde"'], '98. Você já experimentou alguma nova atividade de lazer nos últimos meses? "': [' Sim, várias novas atividades "', ' Sim, algumas novas atividades "', ' Não experimentei novas atividades "', ' Não tenho tempo ou interesse em experimentar novas atividades"'], '99. Qual a última atividade de lazer que você praticou? "': [' Esportes "', ' Artes e cultura "', ' Viagens "'], '100. Você acredita que as atividades de lazer são importantes para a sua qualidade de vida? "': [' Sim, extremamente importantes "', ' Sim, bastante importantes "', ' Não tão importantes "', ' Não são importantes para mim"'], '101. Você tem uma crença ou religião em que se baseia sua espiritualidade? "': [' Sim, tenho uma crença ou religião específica "', ' Não, não tenho uma crença ou religião específica"'], '102.Com que frequência você se dedica a práticas espirituais, como oração, meditação, leitura de textos sagrados, entre outras? "': [' Diariamente "', ' Semanalmente "', ' Mensalmente "', ' Raramente"'], '103. Você já teve alguma experiência que considerou espiritual? "': [' Sim, já tive várias experiências espirituais "', ' Sim, já tive algumas experiências espirituais "', ' Não, nunca tive uma experiência espiritual significativa"'], '104. Você acredita que a espiritualidade pode ajudar a melhorar sua saúde física e mental? "': [' Sim, totalmente "', ' Sim, em parte "'], ') Não acredito que a espiritualidade tenha influência sobre minha saúde"': [' 105.Você costuma frequentar algum espaço religioso ou de prática espiritual? "', ' Sim, com frequência "', ' De vez em quando "', ' Raramente "', ' Nunca"'], '106. Como a sua espiritualidade influencia suas decisões e escolhas na vida? "': [' Influencia muito "', ' Influencia em parte "', ' Não influencia"'], '107. Você tem alguma prática espiritual que te ajuda a lidar com momentos difíceis? "': [' Sim, tenho uma prática específica que me ajuda "', ' Não, não tenho uma prática específica que me ajuda "', ' Acredito que a minha espiritualidade em si já me ajuda a lidar com momentos difíceis"'], '108.Qual é a sua visão sobre a relação entre espiritualidade e felicidade? "': [' Acredito que a espiritualidade é fundamental para a felicidade "', ' Acredito que a espiritualidade pode ajudar, mas não é o único fator determinante para a felicidade "', ' Não acredito que a espiritualidade tenha relação direta com a felicidade"'], '109. Você já teve alguma crise espiritual? Como lidou com ela? "': [' Sim, já tive uma crise espiritual e consegui superá-la "', ' Sim, já tive uma crise espiritual e ainda estou lidando com ela "', ' Não, nunca tive uma crise espiritual"'], '110. Como você define sua espiritualidade? "': [' É algo muito importante e presente na minha vida "', ' É algo que faz parte da minha vida, mas não é tão importante "', ' Não considero ter uma espiritualidade definida"'], '111. Com que frequência você dedica seu tempo livre a atividades que considera produtivas? "': [' Diariamente "', ' Semanalmente "', ' Mensalmente "', ' Raramente"'], '112. Qual é o tipo de atividade produtiva que você mais gosta de fazer durante o seu tempo livre? "': [' Aprender algo novo "', ' Ler livros ou artigos relacionados à sua área de interesse "', ' Fazer algum trabalho voluntário "', ' Desenvolver algum projeto pessoal"'], '113. Você acredita que a prática de atividades produtivas durante o seu tempo livre pode trazer benefícios para a sua vida pessoal e profissional? "': [' Sim, totalmente "', ' Sim, em parte "', ' Não acredito que traga benefícios significativos"'], '114. Com que frequência você se desafia a desenvolver novas habilidades ou aprender algo novo? "': [' Sempre, estou sempre procurando aprender algo novo "', ' De vez em quando, quando tenho interesse em algo específico "', ' Raramente, não costumo buscar novos desafios"'], '115. Qual é a sua opinião sobre a importância do tempo livre para a saúde mental e física? "': [' Acredito que o tempo livre é fundamental para manter a saúde mental e física "', ' Acredito que o tempo livre pode ajudar, mas não é o único fator determinante para a saúde "', ' Não acredito que o tempo livre tenha relação direta com a saúde"'], '116. Como você escolhe as atividades produtivas que fará durante o seu tempo livre? "': [' Baseado nos seus interesses pessoais "', ' Baseado em oportunidades que surgem "', ' Baseado em necessidades profissionais ou pessoais"'], '117. Você acredita que a prática de atividades produtivas pode ser um antídoto para o tédio e a apatia? "': [' Sim, totalmente "', ' Sim, em parte "', ' Não acredito que atividades produtivas possam ajudar a combater o tédio e a apatia"'], '118. Qual é a sua opinião sobre a relação entre o tempo livre produtivo e a qualidade de vida? "': [' Acredito que o tempo livre produtivo é fundamental para melhorar a qualidade de vida "', ' Acredito que o tempo livre produtivo pode ajudar, mas não é o único fator determinante para a qualidade de vida "', ' Não acredito que o tempo livre produtivo tenha relação direta com a qualidade de vida"'], '119. Como você organiza o seu tempo livre para garantir que consiga se dedicar a atividades produtivas? "': [' Planejo com antecedência as atividades que farei "', ' Deixo as coisas fluírem naturalmente "', ' Não costumo me preocupar em organizar o meu tempo livre"'], '120. Você tem alguma meta ou projeto pessoal que deseja alcançar durante o seu tempo livre? "': [' Sim, tenho uma meta ou projeto pessoal específico que desejo alcançar "', ' Não, não tenho nenhuma meta ou projeto pessoal em mente "', ' Estou sempre em busca de novos projetos e desafios para desenvolver durante meu tempo livre "']}

# Criar um DataFrame com as perguntas e respostas
df = pd.DataFrame.from_dict(questions, orient='index', columns=['opcao1', 'opcao2', 'opcao3', 'opcao4'])

# Criar uma instância da classe Survey
survey = Survey(df)

# Exibir a primeira pergunta e opções de resposta
survey.show_question(0)

# Loop para apresentar as perguntas e coletar as respostas do usuário
for i in range(1, len(questions)):
    # Obter a resposta do usuário para a pergunta anterior
    answer = survey.get_answer(i-1)
    # Apresentar a próxima pergunta
    survey.show_question(i)
    # Coletar a resposta do usuário
    survey.collect_response(answer)

# Salvar o progresso do jogo
survey.save_results('resultados.csv')
