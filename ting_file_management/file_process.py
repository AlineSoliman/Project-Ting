from ting_file_management.file_management import txt_importer


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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
