import string
import random

def generate_random_quastions():
    print('Want to generate random question?\n1.yes\n2.no\n')
    ch=int(input('ENTER YOUR CHOICE :'))
    if ch==1:
        rand_no=int(input('ENTER NO OF QUESTIONS SETS TO BE GENERATED RANDOMLY :'))
        for n in range(rand_no):
            print("QUESTION SET :",n+1,"\n")
            for i in range(5):
                with open('QuestionBank.txt','r') as f:
                    fi=f.readlines()
                    length = len(fi)
                    #print('no of lines in the file :',length)
                    r1 = random.randint(0, length - 1)
                    print(i+1,".",fi[r1])
        exit()
    elif ch==2:
        print('Exit statement!')
        exit()
        #mainscreen()
    else:
        print('Invalid choice!')
        exit()
        #mainscreen()

def keycheck(final_words,text):
    with open('syllabus.txt', 'r') as file:
        for line in file:
            cleared_line = line.replace('\n', '').replace('-', '').replace(',', '').replace('.',
                                                                                            '')  # removing extra new lines in syllabus.txt
            # print(cleared_line)
            word = cleared_line.lower()
            if word in final_words:
                print('AND THE QUESTION IS FROM SYLLABUS')
                Add_to_QuesBank(text)
    print('BUT THE QUESTION IS NOT FROM SYLLABUS')
    print('INVALID QUESTION\n')
    generate_random_quastions()

def Add_to_QuesBank(text):
    file1=open('QuestionBank.txt','a+')
    file1.write('\n')
    file1.write(text)
    print('Updated the Question Bank Successfully!')
    generate_random_quastions()

def mainscreen():
    text=input('ENTER A QUESTION :')
    textt=text.lower()
    file = open("QuestionBank.txt")
    #print(file.read())
    for text1 in file:
        text2=text1.lower()
        #print(text2)
        if textt in text2:
            print("Question is already present!Please enter another question!")
            mainscreen()

    lower_case = text.lower()  #converting the text to lower case

    cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation)) #removing the punctuations

    tokenized_words=cleaned_text.split();
    # print('tokenized words :',tokenized_words)

    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                          "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                          "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
                          "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
                          "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                          "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                          "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                          "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                          "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                          "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    final_words=[]
    for word in tokenized_words:
         if word not in stop_words:
            final_words.append(word)
    #print('final words :',final_words)  #printing without stop_words


    with open('read.txt','r') as bloom_words:
         for wordss in bloom_words:
             cleared_line1 = wordss.replace('\n', '')
             words1=cleared_line1.lower()
             if words1 in tokenized_words:    #here we are taking tokenized words instead of keywords because some tokenized words may be question words
                  print('BLOOMS TAXONOMY QUESTION')
                  keycheck(final_words,text)
    print('NOT BLOOMS TAXONOMY QUESTION')
    print('INVALID QUESTION')
    generate_random_quastions()

mainscreen()


