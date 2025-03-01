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


#Function storing information about employees

def company_management():
    # Dictionary storing employee information
    company_employees = {
        "Engineering": {
            "Alice": {"age": 30, "role": "Software Engineer"},
            "Bob": {"age": 28, "role": "DevOps Engineer"}
        },
        "HR": {
            "Charlie": {"age": 35, "role": "HR Manager"}
        }
    }
    print(company_employees)

    # Adding a new Employee
    company_employees.setdefault("Engineering", {})["David"] = {"age": 27, "role": "Data Scientist"}
    print(company_employees)

    # Nested function to count total employees
    def count_total_employees():
        total = sum(len(department) for department in company_employees.values())
        return total

    print(count_total_employees())


# Function to invert a dictionary where values become keys and keys become a list of values
def invert_dictionary(original_dict):
    inverted_dict = {}  

    # Loop through the original dictionary
    for key, value in original_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)  
        else:
            inverted_dict[value] = [key] 

    return inverted_dict  
