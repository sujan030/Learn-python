#parsing the file we read from the pc


dict1 ={}
def parse_paragraph():
    text_file = open("C:\\Users\\acer\\Desktop\\read.txt", "r")
    paragraph = text_file.read()
    words = paragraph.split()
    unique_words = set(words)
    for x in unique_words:
        count = 0
        for word in words:
            if x == word:
                count=count+1
                dict1[x] = count
    unique_word_count = len(unique_words)
    word_count = len(words)
    print("Word count: ", word_count)
    print("Unique word count: ", unique_word_count)
    print(dict1)
parse_paragraph()