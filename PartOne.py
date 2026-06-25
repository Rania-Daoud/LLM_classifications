# NLP assessment template 2026

# Note: The template functions here and the dataframe format for structuring your solution is a suggested but not mandatory approach. You can use a different approach if you like, as long as you clearly answer the questions and communicate your answers clearly.

import string

import nltk
import spacy
import pandas as pd
from pathlib import Path
from os import listdir, read, path
from os.path import isfile, join, splitext


nlp = spacy.load("en_core_web_sm")
nlp.max_length = 2000000


# helper function to get the content of the file and split the file name.
def get_content(path: str, file_name: str) -> list[str]:
    f = open(f"{path}/{file_name}")
    file_name_no_extension, _ = splitext(file_name)
    title, author, year = file_name_no_extension.split('-')
    return [title, author, year, f.read()]


# Returns the Flesch-Kincaid Reading-Ease of a text (higher grade is more difficult).
def fk_level(text: str, d: dict) -> float:

    # use RegexpTokenizer to ignore punctuation.
    # also ignore numbers.
    tokenizer = nltk.RegexpTokenizer(r'[a-zA-Z]')

    # transfer text to lower case to ignore capitalization.
    document_words = tokenizer.tokenize(text.lower())

    # get sentences in the text
    sentences = nltk.sent_tokenize(text)

    # get the totl number of words in this documents.
    total_words = len(document_words)

    # get the total number of sentences in this document
    total_sentences = len(sentences)

    # calculate the number of syllables in this document
    total_syllables = 0
    for word in document_words:
        total_syllables += len(d[word][0])

    # formuala for fk_level reading ease score
    fk_level = 206.835-1.015 * total_words / \
        total_sentences-84.6 * total_syllables/total_words
    return fk_level


def count_syl(word, d):
    """Counts the number of syllables in a word given a dictionary of syllables per word.
    if the word is not in the dictionary, syllables are estimated by counting vowel clusters

    Args:
        word (str): The word to count syllables for.
        d (dict): A dictionary of syllables per word.

    Returns:
        int: The number of syllables in the word.
    """
    pass


def read_novels(path="texts/novels") -> pd.DataFrame:
    # get the file names
    file_names = [f for f in listdir(path) if isfile(join(path, f))]

    # get the list of title, author, year, content.
    names_and_contents = map(
        lambda file_name: get_content(path, file_name), file_names)

    # create the dataframe.
    df = pd.DataFrame(data=names_and_contents, columns=[
                      "title", "author", "year", "text"])

    # set the year as index and sort by it.
    df = df.set_index("year")
    df = df.sort_index()
    return df


def parse(df, store_path=Path.cwd() / "pickles", out_name="parsed.pickle"):
    """Parses the text of a DataFrame using spaCy, stores the parsed docs as a column and writes 
    the resulting  DataFrame to a pickle file"""
    pass


# function to get type-token ratio
def nltk_ttr(text: str) -> float:
    # use RegexpTokenizer to ignore punctuation.
    tokenizer = nltk.RegexpTokenizer(r'\w+')

    # transfer text to lower case to ignore capitalization.
    document_words = tokenizer.tokenize(text.lower())

    # set removes duplicate values.
    unique_words = set(document_words)

    # divide unique words / all words to get ttr
    ttr = len(unique_words) / len(document_words)
    return ttr


# helper function to add ttr to a dataframe
def get_ttrs(df) -> pd.DataFrame:
    # add a new column where its value is derived from "text" column.
    # mapping function returns a map of ttr.
    # convert to a list to be able to add to DataFrame.
    df["token"] = list(map(nltk_ttr, df["text"]))
    return df


# helper function to add fk scores to a dataframe
def get_fks(df):

    # get the syllables per word mapping
    cmudict = nltk.corpus.cmudict.dict()

    # add a new column where its value is derived from "text" column.
    # mapping function returns a map of fks.
    # convert to a list to be able to add to DataFrame.
    df["fks"] = list(
        map(lambda x: round(fk_level(x, cmudict), 4), df["text"]))
    return df


# .. add functions for part (e) here


if __name__ == "__main__":
    """
    uncomment the following lines to run the functions once you have completed them
    """
    path = Path.cwd() / "texts" / "novels"
    print(path)
    # this line will fail until you have completed the read_novels function above.
    df = read_novels(path)
    print(df.head())
    nltk.download("cmudict")
    parse(df)
    print(df.head())
    get_ttrs(df)
    print(df.head())
    get_fks(df)
    print(df.head())
    # df = pd.read_pickle(Path.cwd() / "pickles" /"name.pickle")
    # call functions for part (e) here.
