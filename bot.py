from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.chat.util import Chat
#Função que separa as palavras que o usuário digita
while True:
    response = str(input('user: '))
    token = word_tokenize(response)
    print('machine: ',token)
