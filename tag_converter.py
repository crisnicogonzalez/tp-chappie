from nltk import help,download
download('tagsets')


def get_meaning_from_tag(tag):
    return {
        "ADJ": "adjetive",
        "ADV": "adverb",
        "SNJ": "conjunction",
        "DET": "determiner",
        "EX": "existencial",
        "FW": "foreign word",
        "MOD": "modal verb",
        "NN": "noun, common, singular or mass",
        "NP": "proper noun",
        "NUM": "number",
        "PRO": "pronoum",
        "P": "preposition",
        "TO": "the word to",
        "UH": "interjection",
        "V": "verb",
        "VD": "past tense",
        "VG": "present participle",
        "VN": "past participle",
        "WH": "WH determiner",
        "NNP": "noun, proper, singular"
    }[tag]


def get_meaning_from_nltk(tag):
    help.upenn_tagset(tag)

def print_tagger_result(tagger_result):
    for x in tagger_result:
        print x[0]
        get_meaning_from_nltk(x[1])
