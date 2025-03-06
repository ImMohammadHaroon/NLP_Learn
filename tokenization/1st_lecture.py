from nltk import sent_tokenize

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
output = sent_tokenize(example_text)
print(output)
