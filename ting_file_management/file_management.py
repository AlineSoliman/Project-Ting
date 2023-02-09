import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return print(ValueError("Formato inválido"), file=sys.stderr)

    try:
        with open(path_file, mode='r') as file:
            result = file.read().split('\n')
            return result

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
