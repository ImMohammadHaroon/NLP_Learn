# tokenization of words and sentences.
# Tokenization is the process of breaking down a text into words and sentences.

from nltk import sent_tokenize , word_tokenize

example_text = "D. Robert & Lorri Franz have been full time professional wildlife photographers for over twenty five years. With undergraduate degrees in wildlife management and geology and graduate work in earth science, Robert has an extensive knowledge of the natural world. Their nature and wildlife images have been extensively published (over ten thousand published images including hundreds of front covers) worldwide with images featured in, Audubon Magazine, National Wlidlife, Sierra Magazine, Smithsonian Magazine, Defenders Magazine, National Geographic, Das Tier Magazine, Sports Afield, Field and Stream and many more. Their photographic prints have hung in the Smithsonian and the United States Congress. They are also accomplished assignment photographers specializing in nature and environmental issues. Clients have included Adolph Coors, Wildlife Conservation Society, Field and Stream Magazine, The Trust for Public Lands, Via Magazine, Greater Yellowstone Coalition and others. Their photography is represented by a number of the worlds leading stock photo agencies such as Getty Images, Alamy, Windigo Images, and Okapia. " 
"Robert and Lorri have won many awards for their photography over the years. In 1989 Robert won the Colorado Outdoors Magazine Nature Photography Contest. In 1993 he won the Wyoming Wildlife Magazines Nature Photography Contest. Also in 1993 Robert and Lori won an award for a published calendar image from the Roger Tory Peterson Institute of Natural History, In 2001 and 2004 Robert had winning images the prestigious Nature's Best photography contest. in 2003 Robert won image of the Year for Nature Photographers.net. In 2006, 2008 and again in 2010 Robert finished 2nd in the Images for Conservation Pro Tour of Nature Photography contest held in different locations in Texas. This is the world's most challenging nature photo contest and the truest test of all around nature photography skills. You can see the winning portfolios at imagesforconservation.org. In 2007 Digital Photography Magazine prociaimed Robert as one the worlds best wildlife photographers"
output = sent_tokenize(example_text)
output = word_tokenize(example_text)
print(output)


# what is corpus, corpora?
# A corpus is a data set 
# Corpora is the plural of corpus. 
