import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import pos_tag

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Sample text (for demonstration)
text = """
Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics 
concerned with the interactions between computers and human (natural) languages, and, in particular, concerns 
with programming computers to fruitfully process large natural language data.
"""

# Step 1: Tokenization (Sentence and Word Level)
sentences = sent_tokenize(text)  # Sentence Tokenization
words = word_tokenize(text)  # Word Tokenization

# Step 2: Count Word Frequency
word_freq = FreqDist(words)  # Frequency Distribution of Words

# Step 3: Remove Stop Words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Step 4: Part-of-Speech (POS) Tagging
pos_tags = pos_tag(filtered_words)

# Output Results
print("Original Text Tokenized into Sentences:")
print(sentences)
print("\nTokenized Words (with punctuation):")
print(words)
print("\nWord Frequency Count:")
print(word_freq)
print("\nFiltered Words (Stop Words Removed):")
print(filtered_words)
print("\nPOS Tagging (Filtered Words):")
print(pos_tags)
