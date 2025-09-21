# Iterates all name files from avoindata.
# In each file, each line is a single name, which we extract.
# All names are written to new type specific text files.
def main():
    filenames = ['surnames_fi_avoindata.txt', 'firstnames_men_fi_avoindata.txt', 'firstnames_women_fi_avoindata.txt']
    for filename in filenames:
        file = open(f"wordlists_raw/{filename}", "r", encoding="utf-8")
        content = file.read()
        print(f"Read file {filename} OK")

        new_file = open(f"wordlists_parsed/{filename}", "w", encoding="utf-8")
        for line in content.splitlines():
            new_file.write(line.lower().strip() + '\n')

        print("Rewrite files OK")
        file.close()
        new_file.close()
    print("Finished")

if __name__ == "__main__":
    main()