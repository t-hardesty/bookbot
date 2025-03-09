def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = 0
        words = file_contents.split()
        for word in words:
            word_count += 1
    return print(word_count)
main()