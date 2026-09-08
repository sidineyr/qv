"""Converte um questionário numerado em texto para JSON estruturado.

Este utilitário é independente do questionário publicado em ``questions.js``.
Ele existe para organizar rascunhos sem executar código ou misturar conteúdo
incompleto ao site.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


PADRAO_PERGUNTA = re.compile(r"^(\d+)[.)]\s+(.+)$")
PADRAO_OPCAO = re.compile(r"^([a-zA-Z])[.)]\s+(.+)$")


def converter_questionario(texto: str) -> list[dict[str, object]]:
    """Extrai perguntas e opções de um texto; rejeita blocos incompletos."""
    perguntas: list[dict[str, object]] = []
    atual: dict[str, object] | None = None

    for linha_bruta in texto.splitlines():
        linha = linha_bruta.strip().removesuffix("/").strip()
        if not linha:
            continue

        pergunta = PADRAO_PERGUNTA.match(linha)
        if pergunta:
            if atual is not None:
                _validar_pergunta(atual)
                perguntas.append(atual)
            atual = {
                "id": len(perguntas) + 1,
                "numero_original": int(pergunta.group(1)),
                "pergunta": pergunta.group(2).strip(),
                "opcoes": [],
            }
            continue

        opcao = PADRAO_OPCAO.match(linha)
        if opcao:
            if atual is None:
                raise ValueError("Foi encontrada uma opção antes da primeira pergunta")
            opcoes = atual["opcoes"]
            assert isinstance(opcoes, list)
            opcoes.append(
                {
                    "id": opcao.group(1).lower(),
                    "texto": opcao.group(2).strip(),
                }
            )

    if atual is not None:
        _validar_pergunta(atual)
        perguntas.append(atual)

    if not perguntas:
        raise ValueError("Nenhuma pergunta válida foi encontrada")
    return perguntas


def _validar_pergunta(pergunta: dict[str, object]) -> None:
    opcoes = pergunta.get("opcoes")
    if not isinstance(opcoes, list) or len(opcoes) < 2:
        numero = pergunta.get("numero_original", "?")
        raise ValueError(f"A pergunta {numero} precisa ter ao menos duas opções")
    identificadores = [opcao["id"] for opcao in opcoes]
    if len(identificadores) != len(set(identificadores)):
        numero = pergunta.get("numero_original", "?")
        raise ValueError(f"A pergunta {numero} contém opções repetidas")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrada", type=Path, help="arquivo TXT de origem")
    parser.add_argument(
        "-o",
        "--saida",
        type=Path,
        help="arquivo JSON de destino; sem esta opção, imprime na tela",
    )
    args = parser.parse_args()

    perguntas = converter_questionario(args.entrada.read_text(encoding="utf-8"))
    resultado = json.dumps(perguntas, ensure_ascii=False, indent=2) + "\n"
    if args.saida:
        args.saida.write_text(resultado, encoding="utf-8")
    else:
        print(resultado, end="")


if __name__ == "__main__":
    main()
