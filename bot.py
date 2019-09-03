from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.chat.util import Chat

while True:
    response = str(input('user: '))
    token = word_tokenize(response)
    print('machine: ',token)
