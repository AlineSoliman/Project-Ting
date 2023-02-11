from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = [
        instance.search(index)["nome_do_arquivo"]
        for index in range(len(instance))
    ]

    if path_file not in file:
        data = txt_importer(path_file)
        info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }
        instance.enqueue(info)
        return info


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return
    data = instance.dequeue()
    path_file = data["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):

    try:
        info = instance.search(position)
        print(info)
        return

    except IndexError:
        print("Posição inválida", file=sys.stderr)
