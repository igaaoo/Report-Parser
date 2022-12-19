# Import files from folder
import os

rootPath = "Apps"

# Get elements and errors from report


def getElementsAndErrors(content):
    elementsAndErros = list(filter(lambda x: x.startswith("com") or x.startswith("ufc") or x.startswith(
        "[") or x.startswith("Rótulo do item") or x.startswith("Tamanho do texto") or x.startswith("Área de toque") or x.startswith("Contraste da imagem") or x.startswith("Descrições de itens") or x.startswith("Contraste do texto"), content))

    pairs = zip(elementsAndErros[0::2], elementsAndErros[1::2])

    final = list(set(pairs))

    return final


# Get all files from folders
for root, dirs, files in os.walk(rootPath):

    for dire in dirs:
        content = []

        files = os.listdir(root + "/{}/" .format(dire))

        for file in files:
            if file.endswith(".txt"):  # Only txt files
                infile = open(root + "/{}/" .format(dire) +
                              file, encoding='utf-8')
                content += infile.read().split('\n')

        # Get all reports from folder
        reports = [f for f in files if f.endswith(".txt")]

        # Print collected data
        print("________________________________________________________________________")
        print("\n")

        print("Aplicativo Analisado: ")
        print(dire)
        print("\n")

        print("Relatórios encontrados: ")
        print(reports)
        print("\n")

        elementsAndErros = getElementsAndErrors(content)
        infile.close()

        errorsTotal = list(
            filter(lambda x:  x.startswith("Rótulo do item") or x.startswith("Tamanho do texto") or x.startswith("Área de toque") or x.startswith("Contraste da imagem") or x.startswith("Descrições de itens") or x.startswith("Contraste do texto"), content))

        errors = {}

        for element in errorsTotal:
            if element in errors:
                errors[element] += 1
            else:
                errors[element] = 1

        print("Tipos de erros: ")
        print(errors)
        print("\n ")

        print("Menor quantidade de erro: ")
        print(min(errors, key=errors.get) +
              ": {}" .format(min(errors.values())))
        print("\n")

        print("Maior quantidade de erro: ")
        print(max(errors, key=errors.get) +
              ": {}" .format(max(errors.values())))
        print("\n")

        print("Quantidade de erros únicos em elementos: ")
        print(len(elementsAndErros))

        print("\n ")

        print("Elementos e erros: ")
        print(elementsAndErros)

        print("\n ")
