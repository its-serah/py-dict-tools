#Global variables
class1_info = {
    "section" : "A",
    "level" : "Graduate",
    "lab" : "yes",
    "student_count": 24,  #camel case naming 
}

class2_info = {
    "section" : "C",
    "level" : "undergraduate",
    "floor" : 3,
    "student_count": 14,  #camel case naming 
}

#Dictionaries Merger Function implementation

def merge_dictionaries (class1_info,class2_info):
    class3_info = {}
    # Copy class1_info into class3_info
    for key in class1_info:
        class3_info[key] = class1_info[key]

    # Copy class2_info into class3_info 
    for key in class2_info:
        class3_info[key] = class2_info[key]  

    return class3_info   


#Dictonaries Generator Function

def generate_dictionaries ():
    print("Welcome To Dictionaries Generater Where We Generate Dictionaries From Your Sentences!")
    sentence = input("Please enter a full english sentence")

    # Convert sentence to lowercase if needed
    if not sentence.islower():
        sentence = sentence.lower()

    # Split sentence into words
    words = sentence.split()

    # Calculate total words
    word_total = len(words)

    word_frequencies = {}

    # Loop through words and count occurrences
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1

     # Final dictionary with both word count and word occurrences
    result = {
        "word_count": word_total,   # Total number of words
        "word_frequencies": word_frequencies  # Word frequency dictionary
    }

    print("Generated Dictionary:", result)  
    return result


