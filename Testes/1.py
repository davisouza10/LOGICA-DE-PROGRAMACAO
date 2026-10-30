"""Mercadinho Dendezeiros: cadastro de números de série."""

from __future__ import annotations

import os
import tempfile
from collections.abc import Callable, Iterator
from pathlib import Path

ARQUIVO_DADOS = Path(__file__).with_name("numeros_serie.txt")

MENU = """
=== MERCADINHO DENDEZEIROS ===
1 - Cadastrar número de série
2 - Listar números de série
0 - Sair
"""


class SerieInvalidaError(ValueError):
    """Número de série vazio ou inválido."""


class SerieDuplicadaError(ValueError):
    """Número de série já cadastrado."""


class RepositorioSeries:
    """Guarda os números de série e persiste em arquivo texto.

    Usa um dict como "conjunto ordenado": mantém a ordem de cadastro
    e permite checar duplicidade em O(1).
    """

    def __init__(self, caminho: Path) -> None:
        self._caminho = caminho
        self._series: dict[str, None] = dict.fromkeys(self._ler_arquivo())

    def __len__(self) -> int:
        return len(self._series)

    def __iter__(self) -> Iterator[str]:
        return iter(self._series)

    def adicionar(self, bruto: str) -> str:
        """Normaliza, valida e grava um número de série. Retorna o valor salvo."""
        serie = bruto.strip().upper()

        if not serie:
            raise SerieInvalidaError("O número não pode ficar vazio.")
        if serie in self._series:
            raise SerieDuplicadaError(f"{serie} já está cadastrado.")

        self._series[serie] = None
        try:
            self._gravar_arquivo()
        except OSError:
            del self._series[serie]  # mantém memória e disco consistentes
            raise
        return serie

    def _ler_arquivo(self) -> list[str]:
        try:
            texto = self._caminho.read_text(encoding="utf-8")
        except FileNotFoundError:
            return []
        return [linha.strip() for linha in texto.splitlines() if linha.strip()]

    def _gravar_arquivo(self) -> None:
        """Grava em arquivo temporário e troca no final (escrita atômica)."""
        conteudo = "\n".join(self._series) + "\n"
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=self._caminho.parent,
            suffix=".tmp",
            delete=False,
        ) as tmp:
            caminho_tmp = Path(tmp.name)
            try:
                tmp.write(conteudo)
            except OSError:
                caminho_tmp.unlink(missing_ok=True)
                raise
        os.replace(caminho_tmp, self._caminho)


# --- Interface de terminal -------------------------------------------------


def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pausar() -> None:
    input("\nPressione ENTER para continuar...")


def cadastrar(repo: RepositorioSeries) -> None:
    print("\n== CADASTRO DE NÚMEROS DE SÉRIE ==")
    try:
        serie = repo.adicionar(input("Digite o número de série: "))
    except (SerieInvalidaError, SerieDuplicadaError) as erro:
        print(erro)
    except OSError as erro:
        print(f"Não foi possível salvar os dados: {erro}")
    else:
        print(f"{serie} cadastrado com sucesso!")


def listar(repo: RepositorioSeries) -> None:
    print("\n== NÚMEROS DE SÉRIE ==")
    if not repo:
        print("Nenhum número de série cadastrado.")
        return
    for i, serie in enumerate(repo, start=1):
        print(f"{i}. {serie}")
    print(f"\nTotal: {len(repo)}")


def main() -> None:
    repo = RepositorioSeries(ARQUIVO_DADOS)
    acoes: dict[str, Callable[[RepositorioSeries], None]] = {
        "1": cadastrar,
        "2": listar,
    }

    while True:
        limpar_tela()
        print(MENU)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\nSaindo do programa...")
            return

        acao = acoes.get(opcao)
        if acao is None:
            print("Opção inválida!")
        else:
            acao(repo)
        pausar()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrado pelo usuário.")