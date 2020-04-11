from std_imports import *

def read_corpus(category="crude"):
    """ Read files from the specified Reuter's category.
        Params:
            category (string): category name
        Return:
            list of lists, with words from each of the processed files
    """
    files = reuters.fileids(category)
    return [[START_TOKEN] + [w.lower() for w in list(reuters.words(f))] + [END_TOKEN] for f in files]


def distinct_words(corpus):
    """ Determine a list of distinct words for the corpus.
        Params:
            corpus (list of list of strings): corpus of documents
        Return:
            corpus_words (list of strings): list of distinct words across the corpus, sorted (using python 'sorted' function)
            num_corpus_words (integer): number of distinct words across the corpus
    """
    corpus_words = []
    num_corpus_words = -1

    # ------------------
    flattened_list = [y for x in corpus for y in x]
    corpus_words = sorted(list(set(flattened_list)))
    num_corpus_words = len(corpus_words)
    # ------------------

    return corpus_words, num_corpus_words


def main():
    reuters_corpus = read_corpus()
    corpus_words, num_corpus_words = distinct_words(reuters_corpus)
    print(num_corpus_words)


if __name__ == "__main__":
    main()
