# Justification: This program not only meets the basic requirements of generating sentences with the specified structure, but also includes additional features such as prepositional phrases, adverbs, and adjectives, enhancing the complexity and variety of the generated sentences.

# Import the random module for generating random selections
import random

# Define the dataset with quantity and tense pairs
data = [
  [1, 	'past'],
  [1,	'present'],
  [1,	'future'],
  [2,	'past'],
  [2,	'present'],
  [2,	'future'],  
]

# The main function that iterates over the dataset and generates sentences
def main():
  for i in data:
    # Call the make_sentence function with quantity and tense from the dataset
    sentence = make_sentence(i[0], i[1])
    # Print the generated sentence
    print(sentence)

# The make_sentence function generates a sentence with a determiner, noun, verb, and two prepositional phrases
def make_sentence(quantity, tense):
  part_one = determinate_adjective_noun(quantity).capitalize()
  prepositional = get_prepositional_phrase(quantity)
  adverb = get_adverb()
  verb = get_verb(quantity, tense)
  part_two = determinate_adjective_noun(quantity)
  prepositional_two = get_prepositional_phrase(quantity)

  sentence = f"{part_one} {prepositional} {adverb} {verb} {part_two} {prepositional_two}."
  return sentence

# The get_determiner function returns a randomly chosen determiner based on the quantity
def get_determiner(quantity):
  if quantity == 1:
      determiners = ["a", "one", "the"]
  else:
      determiners = ["some", "many", "the"]

  determiner = random.choice(determiners)
  return determiner

# The get_noun function returns a randomly chosen noun based on the quantity
def get_noun(quantity):
  if quantity == 1:
    nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
  else:
    nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

  noun = random.choice(nouns)
  return noun

# The get_verb function returns a randomly chosen verb based on the quantity and tense
def get_verb(quantity, tense):
  if tense == "past":
    verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
  elif tense == "present" and quantity == 1:
    verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
  elif tense == "present" and quantity != 1:
    verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
  elif tense == "future":
    verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

  verb = random.choice(verbs)
  return verb

# The get_preposition function returns a randomly chosen preposition
def get_preposition():
  prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

  preposition = random.choice(prepositions)
  return preposition

# The get_prepositional_phrase function returns a randomly chosen prepositional phrase
def get_prepositional_phrase(quantity):
  prepositional_phrase = (f'{get_preposition() } {get_determiner(quantity)} {get_adjective()} {get_noun(quantity)}')
  return prepositional_phrase

# The get_adjective function returns a randomly chosen adjective
def get_adjective():
  adjectives = ["good", "bad", "happy", "sad", "big", "small", "beautiful", "ugly", "smart", "silly", "fast", "slow", "hot", "cold", "easy", "difficult", "young", "old", "rich", "poor", "loud", "quiet", "clean", "dirty", "strong", "weak", "brave", "afraid", "kind", "mean"]

  adjective = random.choice(adjectives)
  return adjective

# The get_adverb function returns a randomly chosen adverb
def get_adverb():
  adverbs = ["quickly", "slowly", "carefully", "quietly", "anxiously", "happily", "sadly", "easily", "hardly", "gently", "abruptly", "skillfully", "clumsily", "cleverly", "absent-mindedly", "lazily", "bravely", "shyly", "passionately", "politely", "rudely", "kindly", "furiously", "cautiously", "honestly", "discreetly", "efficiently", "faithfully", "elegantly", "energetically"]

  adverb = random.choice(adverbs)
  return adverb

# The determinate_adjective_noun function returns a randomly chosen determiner, adjective, and noun
def determinate_adjective_noun(quantity):
  phrase = f'{get_determiner(quantity)} {get_adjective()} {get_noun(quantity)}'
  return phrase

# Call the main function to start the program
main()