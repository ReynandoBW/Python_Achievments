import random

def Randomise(original):
    randomised = ''.join(random.sample(original, len(original)))
    return randomised

print(Randomise("hallo"))
print(Randomise("Jotaro"))
print(Randomise("Kono Dio da"))



