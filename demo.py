import io
import numpy as np
from scipy.spatial.distance import pdist
from WordCount import Text
import click

@click.command()
@click.option("--text", default="Pride", help="Text file")
@click.option("--number", default=20, help="how many most and least words")
def MostLeastVariance(text, number):
    src_path = 'wiki.en.vec'
    nmax = 50000  # maximum number of word embeddings to load

    src_embeddings, src_id2word, src_word2id = load_vec(src_path, nmax)
    
    text_file = Text(text,number)
    common_list=text_file.mostCommon()
    least_list=text_file.leastComon()

    print("MOST USED_WORDS")
    mean,var,Y = get_scores(common_list, src_embeddings, src_id2word)
    print("variance",np.mean(var))
    print(np.mean(Y))
    print("LEAST USED_WORDS")
    mean,var,Y = get_scores(least_list, src_embeddings, src_id2word)
    print("variance",np.mean(var))
    print(np.mean(Y))



def load_vec(emb_path, nmax=50000):
    vectors = []
    word2id = {}
    with io.open(emb_path, 'r', encoding='utf-8', newline='\n', errors='ignore') as f:
        next(f)
        for i, line in enumerate(f):
            word, vect = line.rstrip().split(' ', 1)
            vect = np.fromstring(vect, sep=' ')
            assert word not in word2id, 'word found twice'
            vectors.append(vect)
            word2id[word] = len(word2id)
            if len(word2id) == nmax:
                break
    id2word = {v: k for k, v in word2id.items()}
    embeddings = np.vstack(vectors)
    return embeddings, id2word, word2id



def get_nn(word, src_emb, src_id2word, tgt_emb, tgt_id2word, K=5):
    print("Nearest neighbors of \"%s\":" % word)
    word2id = {v: k for k, v in src_id2word.items()}
    word_emb = src_emb[word2id[word]]
    scores = (tgt_emb / np.linalg.norm(tgt_emb, 2, 1)[:, None]).dot(word_emb / np.linalg.norm(word_emb))
    k_best = scores.argsort()[-K:][::-1]
    for i, idx in enumerate(k_best):
        print('%.4f - %s' % (scores[idx], tgt_id2word[idx]))

def get_scores(wordlist, src_emb, src_id2word):
    word_array=np.zeros((len(wordlist),300), dtype=np.float32)
    for i, word in enumerate(wordlist):
        #print("Nearest neighbors of \"%s\":" % word)
        word2id = {v: k for k, v in src_id2word.items()}
        if word in word2id:
            word_array[i,:] = src_emb[word2id[word]]
        else:
            print(word," cannot be found!")

    mean = np.mean(word_array,axis=0)
    var = np.var(word_array,axis=0)
    Y = pdist(word_array, 'euclidean')
    return mean,var,Y

if __name__ == "__main__":
    MostLeastVariance()

    