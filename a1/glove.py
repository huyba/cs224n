from std_imports import *


def load_embedding_model():
    """ Load GloVe Vectors
        Return:
            wv_from_bin: All 400000 embeddings, each lengh 200
    """
    import gensim.downloader as api
    wv_from_bin = api.load("glove-wiki-gigaword-200")
    print("Loaded vocab size %i" % len(wv_from_bin.vocab.keys()))
    return wv_from_bin


def main():
    # -----------------------------------
    # Run Cell to Load Word Vectors
    # Note: This will take several minutes
    # -----------------------------------
    wv_from_bin = load_embedding_model()


if __name__ == "__main__":
    main()
