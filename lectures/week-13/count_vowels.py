import sys

def vowels_in_string(data) :
    return { v : data.count(v) for v in 'aeiou' }

if __name__ == '__main__' :
    if len(sys.argv) < 2 :
        print("Usage: python count_vowels.py file")
        sys.exit(2)

    file_name = sys.argv[1]
    with open(file_name, 'r') as fp :
        data = fp.read()
        print(vowels_in_string(data))
