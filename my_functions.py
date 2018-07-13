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


def remove_chapter_numbers(text):
    # import functions
    from textblob import TextBlob

    # split text into sentences
    sentences = TextBlob(text).sentences

    # list comprehension
    full_sentences = [str(sentence) for sentence in sentences if len(sentence.split()) > 1]

    print("Number of Sentences:", len(full_sentences))
    return (full_sentences)






