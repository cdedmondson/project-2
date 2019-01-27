import random  # import random module


#  This function gereates a random key
def keyGen():
    random_key = ""  # Initialize random key
    already_selected = []  # List of already selected letters
    alphabets = "bpzhgocvjdqswkimlutneryaxf"  # Initialize alphabet
    # While length of the random key is not equal to 26
    while len(random_key) != 26:
        i = random.randint(0, 25)  # Create random integer within range 0 - 25
        if not (i in already_selected):
            random_key = random_key + alphabets[i]
            already_selected.append(i)
    return random_key  # Return random key result


#  This function encrypts plaintext
def substitutionEncrypt(plainText, key):
    cipher = ""  # Initialize cipher text
    alphabets = "bpzhgocvjdqswkimlutneryaxf"  # Initialize alphabet
    for i in plainText:
        j = alphabets.find(i)
        k = key[j]
        cipher = cipher + k
    return cipher


# Test drive function
def testDrive(keyCode, setofstrings):
    key = ""  # Initialize key
    if keyCode == "":  # If key is blank assign default key
        key = "bpzhgocvjdqswkimlutneryaxf"
    elif keyCode == "r":  # Else if key equals "r" generate key
        key = keyGen()
    print("Key: ", key)  # Display key to user

    for string in setofstrings:
        print(string, "->", substitutionEncrypt(string, key))
    print("")


#  Test cases
testDrive("", ["face", "blow"])
testDrive("r", ["face", "blow"])
testDrive("", ["wonderful", "python", "java", "doedlugvusu"])
testDrive("r", ["wonderful", "python", "java", "doedlugvusu"])


'''

        Tests:

        Key:  bpzhgocvjdqswkimlutneryaxf
        face -> face
        blow -> blow
        
        Key:  mzbqyafukwjcltneihvxsogdpr
        face -> rdfs
        blow -> mial
        
        Key:  bpzhgocvjdqswkimlutneryaxf
        wonderful -> wonderful
        python -> python
        java -> java
        doedlugvusu -> doedlugvusu
        
        Key:  bruvjihxogpyscnqdzketwlfma
        wonderful -> siegtwazd
        python -> rlkvie
        java -> ofxf
        doedlugvusu -> gitgdzjxzyz
        
'''