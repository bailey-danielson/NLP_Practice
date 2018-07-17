def text_reader(text_file):
    """Read in a text file and return a string

    Keyword Arguments:
    text_file -- string that points to a .txt file on your computer"""

    lines = []
    with open(text_file, 'r') as file:
        for line in file:
            lines.append(line)
    return " ".join(lines)


def clean_and_remove_stops(lines):
    """Remove numbers and punctuation, and standardize case

    Keyword Arguments:
    lines: string of text"""

    # import
    import re
    from nltk.corpus import stopwords

    # create set of stop words
    stop = set(stopwords.words('english'))

    lower_characters = lines.lower()
    approved_words = []
    white_list = set('abcdefghijklmnopqrstuvwxyz ')

    for word in lower_characters.split():
        if word not in stop:
            clean_word = re.sub(r'[^a-z ]+', '', word)
            approved_words.append(clean_word)

    print (  # append word(s) to stopword set:
        """stop.update(["string" , "string", "string"])""")
    return " ".join(approved_words)


def clean_text(lines):
    """Remove numbers and punctuation, and standardize case

    Keyword Arguments:
    lines: string of text"""

    lower_characters = lines.lower()
    approved_characters = []
    white_list = set('abcdefghijklmnopqrstuvwxyz ')

    for character in lower_characters:
        if character in white_list:
            approved_characters.append(character)

    return "".join(approved_characters)


def syntax_length(sentences_list):
        sentence_word_count = []
        for sentence in sentences_list:
            count = len(sentence.split())
            sentence_word_count.append(count)
        return sentence_word_count

    
def leng_sentences(text):
    # import
    import re

    # split sentences
    multiple_sentences = re.split('[?.!]', text)

    # find word count per sentence
    def syntax_length(text):
        sentence_word_count = []
        for sentence in text:
            count = len(sentence.split())
            sentence_word_count.append(count)
        return sentence_word_count

    word_count_sentence = syntax_length(multiple_sentences)

    # assign index
    sentence_number = list(range(0, len(multiple_sentences)))

    # remove sentences that are unneeded or not real
    s_leng = [i for i in word_count_sentence if i > 1]

    # re-assign index
    s_index = list(range(0, len(s_leng)))

    print("New Variables: sentence length list: {}, sentence index list: {}".format(len(s_leng), len(s_index)))
    return s_leng, s_index


def polarity_sentences(text):
    # import functions
    from textblob import TextBlob

    # split text into sentences
    sentences = TextBlob(text).sentences

    # create empty list
    polarities = []

    # function
    for sentence in sentences:
        sentences_analysis = TextBlob(str(sentence)).sentiment.polarity
        polarities.append(sentences_analysis)
        polar = TextBlob(str(sentence)).sentiment.polarity

    print("Overall Polarity: {}, Polarities (first 10): {}".format(polar, polarities[:9]))
    return polar, polarities


def polarity_sentences_list(sentences_list):
    
    #import functions
    from textblob import TextBlob

    #create list
    polarities = []

    #function
    for sentence in sentences_list:
        sentences_analysis = TextBlob(str(sentence)).sentiment.polarity
        polarities.append(sentences_analysis)

    return polarities


def subjectivity_sentences(text):
    # import functions
    from textblob import TextBlob

    # split text into sentences
    sentences = TextBlob(text).sentences

    # create list
    subjectivities = []

    # function
    for sentence in sentences:
        sentences_analysis = TextBlob(str(sentence)).sentiment.subjectivity
        subjectivities.append(sentences_analysis)
        subjectiveness = TextBlob(str(sentence)).sentiment.subjectivity

    print("Overall Subjectiveness: {}, Subjectivities (first 10): {}".format(subjectiveness, subjectivities[:9]))
    return subjectiveness, subjectivities


def subjectivity_sentences_list(sentences_list):
    
    #import functions
    from textblob import TextBlob

    #create list
    subjectivities = []

    #function
    for sentence in sentences_list:
        sentences_analysis = TextBlob(str(sentence)).sentiment.subjectivity
        subjectivities.append(sentences_analysis)

    return subjectivities


def remove_sentences_less_than_2(text):
    
    # import functions
    from textblob import TextBlob

    # split text into sentences
    sentences = TextBlob(text).sentences

    # list comprehension
    full_sentences = [str(sentence) for sentence in sentences if len(sentence.split()) > 1]

    print("Number of Sentences:", len(full_sentences))
    return (full_sentences)


def split_text(text, split_keyword):

    # funtion
    text_sections = text.split(split_keyword)

    print("Number of Sections:", len(text_sections))
    return text_sections


def create_chapter_numbers(file , chapter_titles, text_reader_function=text_reader):
    
    """insert chapter number for each chapter title
    
    file: text file 
    chapter_titles: a list of its chapter titles
    
    returns: dictionary with every chapter"""
    
    text = text_reader_function(file)
    
    for title in chapter_titles:
        index = text.find(title)
        new_text = text[:index] + "1. " + text[index:]
        text = new_text
    
    return text


def split_by_chapter_number(text):
    
    #import
    from collections import defaultdict
    from textblob import TextBlob
    
    # create empty list
    chapter_dictionary = defaultdict(list)
    chapter_number = 0

        
    # split text into sentences
    sentences = TextBlob(text).sentences

    # list comprehension
    for sentence in sentences:
        str(sentence)
        word_list = sentence.split( )
        if word_list:
            first_word = word_list[0]
            if first_word[-1] == '.':
                try:
                    float(first_word)
                    chapter_number += 1
                except:
                    pass
        chapter_dictionary[chapter_number].append(str(sentence))
    return chapter_dictionary


def remove_indexed_values(dictionary , int):
    for item in dictionary.values():
        del item[int]
    return dictionary


def create_chapter_data_frame(sentence_list , section, book_title, author):
    
    """sentence_list = list of sentences
    section = int
    book_title = title"""
    
    # import
    import pandas as pd
    
    df = pd.DataFrame()
    df["Sentence"] = sentence_list
    df["Section"] = section
    df["Book_Title"] = book_title
    df["Author"] = author
    return df


def book_df(book_chapters_dict, book_title , author):    
    
    # import
    import pandas as pd
    
    df = pd.DataFrame(columns = ["Sentence" , "Section", "Book_Title" , "Author"])
    for chapter in book_chapters_dict.keys():
        chapter_df = create_chapter_data_frame(book_chapters_dict[chapter], chapter, book_title , author)
        df = df.append(chapter_df, ignore_index = True)
    return df

