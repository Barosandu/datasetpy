from dataset import dataset

from gensim.models.phrases import Phrases, Phraser
from gensim.models import FastText
import pandas as pd
import subprocess
# python3 LegaROutils/utils/data/embeddings.py
sentences_per_article = [entry[0] + entry[1] for entry in dataset]
print(len(sentences_per_article))
sentences = []
for s in sentences_per_article:
    sentences += s
print(len(sentences))

# reading from convention
convention_content = open("/LegaROutils/utils/convention.txt").read()
convention_articles = convention_content.split("gasan")
print(convention_articles)
print(len(convention_articles))
sentences += convention_articles
print(len(sentences))
print("Shuffling\n")
import random
random.shuffle(sentences)
#Initializing the model
# model = FastText(sentences, vector_size = 300, window = 5, min_count = 5, workers = 4, min_n = 1, max_n = 4, ve)
# #Building Vocabulary
# model.save("/LegaROutils/utils/model/ftembeddings1.ft")

i = 0
with open("/LegaROutils/utils/data/dttxt.txt", "a") as f:
    for s in sentences:
        f.write(s + "\n")
        i += 1
        if i % 50 == 0:
            print(f"Ran through {i} sentences\n")

print("FT training!")     
# subprocess.call(["./fasttext/fasttext", "skipgram", "-input", "/LegaROutils/utils/data/datatxt.txt", "-output", "/LegaROutils/model"])

# ./fastText/fasttext skipgram -input /LegaROutils/utils/data/dttxt.txt -output /LegaROutils/model