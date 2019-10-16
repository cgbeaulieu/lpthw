import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors): # I start the main meat of this code in a function conveniently called main. This will be called at the end of this script to get things going.
    line = language_file.readline() # The first thing this function does is read one line from the languages file it is given. You have done this before so nothing new here. Just readline as before when dealing with text files.
    
    if line:
        print_line(line, encoding, errors)
    return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)