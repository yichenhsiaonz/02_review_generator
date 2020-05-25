import random

rng_number = random.randint(1, 2)

print(rng_number)
skeleton_1 = "<Adjective> but/and <Adjective>, <Book Title> is <Plot summary>"
skeleton_2 = "Set in <Time/place> <Title> is the story of <Plot summary>"

if rng_number == 1:
    print(skeleton_1)
else:
    print(skeleton_2)
