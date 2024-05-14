"""
    Programa desenvolvido por João Bastos:Ivo Azevedo:Filipe Pedro
"""

import random
import time

frases_motivacionais = [
    "Acredite em si mesmo e todos os seus sonhos se tornarão realidade.",
    "Não importa o quão difícil seja a jornada, o importante é nunca desistir.",
    "O sucesso é a soma de pequenos esforços repetidos dia após dia.",
    "A única maneira de fazer um excelente trabalho é amar o que você faz.",
    "Se você pode sonhar, você pode fazer.",
    "A vida é 10% o que acontece conosco e 90% como reagimos a isso.",
    "A melhor maneira de prever o futuro é criá-lo.",
    "O único lugar onde o sucesso vem antes do trabalho é no dicionário.",
    "Não espere por oportunidades. Crie-as.",
    "O fracasso é o condimento que dá sabor ao sucesso.",
    "A persistência é o caminho do êxito.",
    "O otimismo é a fé em ação. Nada se pode levar a efeito sem otimismo.",
    "A coragem não é ausência do medo; é a persistência apesar do medo.",
    "Só se pode alcançar um grande êxito quando nos mantemos fiéis a nós mesmos.",
    "A vida é como andar de bicicleta. Para ter equilíbrio, você tem que se manter em movimento.",
    "O sucesso normalmente vem para quem está ocupado demais para procurar por ele.",
    "A vida é 10% o que acontece comigo e 90% de como eu reajo a isso.",
    "A melhor maneira de prever o futuro é inventá-lo.",
    "Eu não falhei. Eu apenas encontrei 10.000 maneiras que não funcionam.",
    "Não é o mais forte que sobrevive, nem o mais inteligente. Quem sobrevive é o mais disposto à mudança.",
    "O sucesso é ir de fracasso em fracasso sem perder o entusiasmo."
]

# função para gerar uma frase aleatoria da lista de frases motivacionais
def frase_aleatoria():
    return random.choice(frases_motivacionais)

# Display intro inicial
def introAnimation():
    intro_text = [
        "\nBem-vindo ao Sistema de Gestão de Aluguer de Automóveis!",
        "\033[1;32mDriveMates Rent-a-Car\033[0m - Luxo sem limites, viagens sem igual.\n", #  códigos de escape ANSI para negrito e cor
        "Seja Bem-vindo \033[1mProfessor Pedro\033[0m! (não se esqueça de ler o ficheiro readmeRentCar.pdf antes de iniciar)\n",
    ]
    for line in intro_text:
        print(line)
        time.sleep(1)
    input("Pressione '\033[1;32;1mEnter\033[m' para continuar...")

# Display intro final
def introAnimationOut():
    intro_text = [
        "\nDesenvolvido por João Bastos, Ivo Azevedo e Filipe Pedro.",
        "CESAE DIGITAL - Leça da Palmeira - Python\n"
    ]
    for line in intro_text:
        print(line)
        time.sleep(1)
    print("\033[1;32mFrase motivacional do dia:\n\033[0m")
    print("\033[1m" + frase_aleatoria() + "\033[0m\n")  

