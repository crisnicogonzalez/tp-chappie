from nltk import *
from tag_converter import print_tagger_result
download('punkt')
download('averaged_perceptron_tagger')


text = word_tokenize("Hola mundo", "spanish")
result = pos_tag(text)
print_tagger_result(result)