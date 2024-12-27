from textblob import TextBlob

text = """
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
"""

blob = TextBlob(text)
blob.tags
blob.noun_phrases


text2 = "Python is a high-level, general-purpose programming language."
wiki = TextBlob(text2)
wiki.tags
# print(wiki.noun_phrases)

fact = "Frogs have tiny eyes."
factCheck = TextBlob(fact)
# print(factCheck.sentiment)


#Function here explains the tag correlated to an inputted word.

#tag dictionary explaining tags, each one as a key value pair.
tag_dictionary = {
    "CC":"coordinating conjunction",
    "CD" :"cardinal digit",
    "DT" :"determiner",
    "EX": "existential there",
    "FW": "foreign word",
    "IN" :"preposition/subordinating conjunction",
    "JJ" :"adjective", # Big
    "JJR":"adjective, comparative", #Bigger
    "JJS" :"adjective, superlative", #Biggest
    "LS": "list marker 1)",
    "MD" :"modal could, will",
    "NN": "noun, singular", #desk
    "NNS": "noun plural", #desks
    "NNP":"proper noun, singular", #Harrison
    "NNPS": "proper noun, plural", #Americans
    "PDT": "predeterminer", #all the kids
    "POS":"possessive ending", #parent‘s
    "PRP": "personal pronoun", #I, he, she
    "PRP$": "possessive pronoun", #my, his, hers
    "RB": "adverb, very", #silently,
    "RBR": "adverb, comparative", #better
    "RBS": "adverb, superlative", #best
    "RP": "particle give up",
    "TO":"to go TO the store.",
    "UH": "interjection", #errrrrrrrm
    "VB": "verb, base form", #take"
    "VBD":"verb, past tense", #took
    "VBG":"verb, gerund/present participle", #taking
    "VBN":"verb, past participle", #taken
    "VBP":"verb, sing. present, non-3d", #take
    "VBZ":"verb, 3rd person sing. present", #takes
    "WDT":"wh-determiner", #which
    "WP":"wh-pronoun", #who, what
    "WP$":"possessive wh-pronoun", #whose
    "WRB":"wh-adverb" #where, when
}
#grabs the word from user input
tag_sentence = TextBlob(input("Input a word to be analyzed: "))
#assigns a tuple to the word and tag
items= tag_sentence.tags
#for loop to find the matching tag
for key,value in tag_dictionary.items():
        #if matching, print the term and definition of the tag. 
        if key == items[0][1]:
            print (f"{key}: {value}.")




#Takes input into a concatenated Textblob sentence-list, and spits it out in order of input and indented as intended.

poem = TextBlob("")
#POEM: "My aching bones. They rattle with fear. For the time of spooks. has decidedly come near. "
for i in range(4):
    poem_input = input(f"Input line {i+1} of the poem: ")
    # adds line to sentence list
    poem+=poem_input + " "
for i in poem.sentences:
    #sentences counts each period as the end of a sentence, and segments them.
    #With that in mind, this for loop prints each line separately
    print(i)


#prints out words if they are used multiple times in an input.

#turns the input into a textblob object.
story = TextBlob(input("Tell me a quick story, I will only show repeated words: "))
    #word_counts makes a dictionary of all the words in the given textblob
    #with the key being the word, and the value being how many times it was repeated.
for item in story.word_counts:
    #if the frequency of a word in the input is 2 or more times, it gets printed with the frequency value.
    if story.word_counts[item] >= 2:
        print(f"{item}: {story.word_counts[item]}.")


