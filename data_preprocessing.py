import pandas as pd
import numpy as np

RATINGS_PATH = "./data/ratings.csv"
TAGS_PATH = "./data/tags.csv"
MOVIES_PATH = "./data/movies.csv"
GENOME_TAGS_PATH = "./data/genome-tags.csv"
GENOME_SCORES_PATH = "./data/genome-scores.csv"
NUM_OF_SAMPLES = 100000


def read_data():
    ratings_df = pd.read_csv(RATINGS_PATH, nrows=NUM_OF_SAMPLES, low_memory=False)
    tags_df = pd.read_csv(TAGS_PATH, nrows=NUM_OF_SAMPLES, low_memory=False)
    movies_df = pd.read_csv(MOVIES_PATH, low_memory=False)
    genome_tags_df = pd.read_csv(GENOME_TAGS_PATH, low_memory=False)
    genome_scores_df = pd.read_csv(GENOME_SCORES_PATH, nrows=NUM_OF_SAMPLES, low_memory=False)


if __name__ == '__main__':
    pass
