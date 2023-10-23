import random

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas

# nltk.download("wordnet")
# nltk.download("punkt")
# nltk.download('averaged_perceptron_tagger')


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


TEXT = (
    "Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. "
    "Vegetables can be eaten either raw or cooked. "
)
QUESTION = "What are vegetables?"

text_tokens = nltk.sent_tokenize(TEXT)
text_tokens.append(QUESTION)
vectorizer = TfidfVectorizer(tokenizer=lemma_sentence)
document = vectorizer.fit_transform(text_tokens)


data_frame = pandas.DataFrame(document.toarray(), columns=vectorizer.get_feature_names_out())
print(data_frame)

values = cosine_similarity(document[-1], document[:-1])
print(values)
index = values.argsort()[0][-1]

values_flat = values.flatten()
values_flat.sort()
coeff = values_flat[-1]
print(coeff)
if coeff > 0.4:
    # most suitable sentence
    print(text_tokens[index])

nltk.download("vader_lexicon")

analyzer = SentimentIntensityAnalyzer()

HAPPY_TEXT = "Hey, what a beautiful day! How amazing it is!"
analyzer_result = analyzer.polarity_scores(HAPPY_TEXT)
print(analyzer_result)

nltk.download("twitter_samples")
samples = nltk.corpus.twitter_samples.strings()
print(samples[random.randint(1, len(samples))])
