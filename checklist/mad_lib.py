import random

# Create an Array with 12 nouns
nouns = ["cat", "toe", "broom", "clock", "doggie", "gamer", "motown", "hacker", "pirate", "teacher pet", "brush"]
noun_x = input("Enter a noun: ")
nouns.append(noun_x)

# Create an Array with 5 verbs
verbs = ["running", "smelling", "talking", "crawl", "kicking"]

# Create an Array with 5 adjectives
adjectives = ["old", "new", "fuzzy", "quick", "sweet"]

# Create an Array with 6 Names
names = ["Paul", "Sofia", "Kate", "Mark", "Jude", "Charlene"]

# Randomly select items from the arrays
rnoun = random.choice(nouns)
rname = random.choice(names)

# Output
print(f"My best {rnoun} {rname} is a pro at serving detentions and suggests bringing the following items to make it through the hour:")

rnoun = random.choice(nouns)
print(f"A/An {rnoun} phone - but don't use it for texting; instead use it as a watch, a calculator, or a/an ")

rnoun = random.choice(nouns)
rverb = random.choice(verbs)
print(f"{rnoun} And be sure to turn it to {rverb} so it doesn't ring.")

rnoun = random.choice(nouns)
print(f"An i-{rnoun} to listen to music. Cover up the earphones by wearing a hooded ")

rnoun = random.choice(nouns)
print(f"{rnoun} Some tissues, in case you need to blow your nose.")

rverb = random.choice(verbs)
radj = random.choice(adjectives)
print(f"Blank paper and something to {rverb} with. Use these {radj} items to compose love songs to your crush.")

rname = random.choice(names)
print(f"{rname} draw a comic strip featuring")

rname = random.choice(names)
rnoun = random.choice(nouns)
print(f"{rname} as the underwear-wearing superhero Captain {rnoun} or even do something crazy like your homework.")

rnoun = random.choice(nouns)
radj = random.choice(adjectives)
print(f"A pair of {rnoun} glasses - you might as well look {radj} while you're there!")
