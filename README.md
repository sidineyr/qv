# Quality View

Aplicação web estática para responder e visualizar um questionário de qualidade de vida.

## Páginas

- `index.html`: questionário progressivo com salvamento automático.
- `dashboard.html`: resultados, histórico local e exportação CSV.

## Privacidade

As respostas ficam apenas no `localStorage` do navegador. Nenhuma informação é enviada a servidor.

## Publicação

O site é compatível com GitHub Pages e não exige etapa de build.

## Autoria e créditos

- Idealização, direção e decisões editoriais: **Sidiney Rodrigues**.
- Arquitetura, programação, experiência, acessibilidade, testes e documentação: desenvolvimento assistido por **OpenAI Codex**, sob direção humana.

O Quality View é um projeto independente. A menção às tecnologias utilizadas não representa patrocínio, parceria formal ou aprovação institucional do conteúdo.

## Contador global de conclusões

O contador segue o princípio de privacidade do Horizonte: registra somente um total agregado quando as 24 perguntas são concluídas. Respostas, resultados e identificadores não são enviados.

A API está em `counter-worker/` e usa Cloudflare Workers com D1. Depois de criar o banco e implantar o Worker, informe sua URL em `counter-config.js`. A interface permanece oculta enquanto a URL não estiver configurada.

