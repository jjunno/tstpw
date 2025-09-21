# Read the entire content of the file.
# Words are in lines such as:
# aakkonen		substantiivi	38
# We extract the first word from each line.
# All words are written to a new txt file.
def main():
    file = open("material/wordlists_raw/lang_fi_kotus.txt", "r", encoding="utf-8")
    content = file.read()
    print("Read file OK")
    
    new_file = open("material/wordlists_parsed/lang_fi_kotus.txt", "w", encoding="utf-8")
    for line in content.splitlines():
        new_file.write(line.split()[0].lower().strip() + '\n')

    print("Rewrite file OK")
    file.close()
    new_file.close()
    print("Finished")

if __name__ == "__main__":
    main() 