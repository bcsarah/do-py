from pyfiglet import figlet_format
from os import system

# Auxiliary
def criar_arte_ascii(texto: str) -> Null:
    system("clear")
    print(figlet_format(texto, "small"), end="")

def titulo(cabecalho: str, descricao: str = "", opcoes: str = []) -> int:
    while True:
        criar_arte_ascii(cabecalho)

        # Descrição
        if descricao:
            for linha in descricao.splitlines():
                print(f"  {linha}")
            print()

        # Opções
        i: int = 1
        for opcao in opcoes:
            print(f"{i} -> {opcao}")
            i += 1

        # Input e Descrição
        try:
            uinput: int = int(input(">> "))
        except Exception:
            pass

        if uinput >= 0 and uinput <= i:
            return uinput