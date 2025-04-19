import csv

file_path_csv = r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\email.csv"
file_path_txt = r"C:\Users\joeyh\OneDrive\Desktop\CPSC - 130\PYTHON\email_template.txt"

print("Email Creator")
print()

with open(file_path_txt, 'r') as file:
    text = file.read()

with open(file_path_csv, newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        first = row[0].strip().title()
        email = row[2].strip().lower()

        emails = text.replace("{name}", first).replace("{email}", email)

        print("===============================================")
        print(emails)


-----------------------------------------------------------------------------------------


print("Pig Latin Translator")
print()

def pig_latin(text):
    vowels = 'aeiou'
    if text[0] in vowels:
        return text + 'ay'
    else:
        for i, letter in enumerate(text):
            if letter in vowels:
                return text[i:] + text[:i] + 'ay'
        return text + 'ay'
    
def pig_latin_phrase(sentence):
    punctuation = "!.,;:-?"
    for p in punctuation:
        sentence = sentence.replace(p, '')

    words = sentence.split()
    output = []
    for word in words:
        output.append(pig_latin(word))
    
    return " ".join(output)

def main():
    try_again = 'y'
    while try_again.lower() == 'y':
        sentence = input("Enter Text: ")
        print(f"English: {sentence}")
        print(f"Pig Latin: {pig_latin_phrase(sentence)}")
        try_again = input("Would you like to try again? (y/n): ")
        if try_again == 'y':
            continue
        elif try_again == 'n':
            print("Bye!")
            break
        else:
                print("invalid input!")
                pass


if __name__ == "__main__":
    main()

