import json
import nltk
import plotly.express as px
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def topic_modeling(input_data: str, save_file_path: str):
    nltk.download('stopwords')
    nltk.download('punkt')
    # load input data from json file
    with open(input_data, 'r') as j:
        data = json.loads(j.read())

    # create a list of texts from the input data
    texts = [item["text"] for item in data]

    # create a list of stopwords to filter out
    stop_words = set(stopwords.words("german"))

    # create a list of tokens (words) from the texts
    tokens = [word_tokenize(text) for text in texts]

    # filter out stopwords from the list of tokens
    filtered_tokens = [[word for word in token if word not in stop_words] for token in tokens]

    # create a tf-idf vectorizer and fit it to the list of tokens
    vectorizer = TfidfVectorizer(tokenizer=lambda doc: doc, lowercase=False)
    X = vectorizer.fit_transform(filtered_tokens)

    # create an LDA model and fit it to the tf-idf matrix
    lda = LatentDirichletAllocation(n_components=5)
    lda.fit(X)

    # get the top keywords for each topic
    keywords = []
    for topic_idx, topic in enumerate(lda.components_):
        keywords.append([vectorizer.get_feature_names()[i] for i in topic.argsort()[:-10 - 1:-1]])

    # convert the list to a JSON string
    list_json = json.dumps(keywords)

    # save the JSON string to a file
    with open(save_file_path, "w") as f:
        f.write(list_json)

if __name__ == "__main__":
    topic_modeling(
        input_data="../../data/raw/reviews.json",
        save_file_path="../../data/processed/keywords.json",
    )
