from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"meu nome e (.*)",
        ["Eai %1, Tudo bem com você?",]
    ],
     [
        r"qual e o seu nome ?",
        ["Meu nome é zé pequeno e o seu?",]
    ],
    [
        r"como vai voce ?",
        ["Estou indo bem\nE você ?",]
    ],
    [
        r"desculpe (.*)",
        ["Suave","beleza, sem problemas",]
    ],
    [
        r"eu estou (.*) muito bem",
        ["Muito bom ouvir isso","Mais que beleza :)",]
    ],
    [
        r"oi|ola",
        ["Eai", "Olá",]
    ],
    [
        r"(.*) idade?",
        ["Porra cara difícil falar de idade eu sou uma porra de um código idiota",]
        
    ],
    [
        r"o que (.*) quer ?",
        ["Me oferece dinheiro que eu quero",]
        
    ],
    [
        r"(.*) criado ?",
        ["Sei la cara alguma coisa com pthon ai, e uns código kibado ","o nicolas copiou de uns sites ai ;)",]
    ],
    [
        r"(.*) (mora|cidade) ?",
        ['Carmo do Rio Claro, perto das casinhas',]
    ],
    [
        r"clima em (.*)?",
        ["O clima aqui %1 ta uma bosta recentemente","Tá quente pra caraio em %1","Tá frio em %1, mas a verdade é que nem sei, n tenho sensores de temperatura"]
    ],
    [
        r"eu trabalho com (.*)?",
        ["%1 é uma coisa daora, ouvi falar disso. Mas ando ocupado esses dias.",]
    ],
[
        r"(.*)chovendo em (.*)",
        ["%2 é foda né","Porra vei %2 tá de sacanagem"]
    ],
    [
        r"como (.*) (.*)",
        ["Como %1 %2? Não entendi nada ainda to sendo desenvolvido seu capeta",]
    ],
    [
        r"(.*) (futebol|jogo) ?",
        ["Eu gosto de LOL e não sou viado",]
    ],
    [
        r"quem (.*) seu idolo?",
        ["Ricardo Milos","Gerson","Renato do Bar da esquina"]
],
    [
        r"qual (.*) (ator|cantor)?",
        ["Brad Pitt","Luan Santana"]
],
    [
        r"quit",
        ["Falou cara depois nois ce fala:) ","Foi bom falar com você seu GAY :)"]
],
    [
        r"legal",
        ["que?"]
],
]
def chatty():
    print("Eai, eu sou um bot bosta de comunicação simples no ZAPZAP ;)\nPor favor escreve tudo em minusculo e sen acento pois ainda sou burro. Digite 'quit' que paramos de conversar ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    chatty()