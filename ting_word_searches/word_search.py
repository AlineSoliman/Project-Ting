def exists_word(word, instance):
    data = []
    lines = []

    for value in range(len(instance)):
        file = instance.search(value)

        for item, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                lines.append({'linha': item + 1})

        if lines:
            data.append(
                {
                    'palavra': word,
                    'arquivo': file['nome_do_arquivo'],
                    'ocorrencias': lines,
                }
            )

    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
