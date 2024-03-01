import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import wikipedia

# nltk.download("wordnet")
# nltk.download("punkt")
# nltk.download('averaged_perceptron_tagger')
# nltk.download("vader_lexicon")
# nltk.download("twitter_samples")


def lemma_sentence(sentence: str):
    # make sure to have a lower case words, upper case won't work with lemmatize()
    # dividing sentence into words also called tokenization
    tokens = nltk.word_tokenize(sentence.lower())
    # to have a valid part of sentence use
    pos_tags = nltk.pos_tag(tokens)
    lemma_result = []
    lemmatizer = WordNetLemmatizer()
    for token, pos_tag in zip(tokens, pos_tags):
        # only first letter
        pos = pos_tag[1][0].lower()
        if pos not in ("v", "n", "a", "r"):  # verb, noun, adjective, adverb
            continue
        lemma_result.append(lemmatizer.lemmatize(token, pos))

    return lemma_result


def process(sentence: str, question_to_ask: str) -> str:
    text_tokens = nltk.sent_tokenize(sentence)
    text_tokens.append(question_to_ask)
    vectorizer = TfidfVectorizer(tokenizer=lemma_sentence)
    document = vectorizer.fit_transform(text_tokens)

    values = cosine_similarity(document[-1], document[:-1])
    index = values.argsort()[0][-1]

    values_flat = values.flatten()
    values_flat.sort()
    coeff = values_flat[-1]
    return text_tokens[index] if coeff > 0.4 else "I don't know"


while True:
    topic = input("What topic are you interested in?:\n")
    question = input("What do you want to know?\n")
    if (question or topic) in {"quit", "q", "close", "end"}:
        break
    wikipedia.set_lang("en")
    text = wikipedia.page({topic}).content
    output = process(text, question)
    print(output)
