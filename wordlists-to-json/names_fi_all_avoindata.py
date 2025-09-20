import json

# Iterates all name files from avoindata.
# In each file, each line is a single name, which we extract.
# All names are written to type specific JSON file.
def main():
    filenames = ['surnames_fi_avoindata', 'firstnames_men_fi_avoindata', 'firstnames_women_fi_avoindata']
    for filename in filenames:
        file = open(f"wordlists-raw/{filename}.txt", "r", encoding="utf-8")
        print(f"Read file {filename} OK")
        content = file.read()

        names = []
        for line in content.splitlines():
            names.append(line)

        print("Extract names OK")
        json_str = json.dumps(names, indent=4)
        with open(f"wordlists-json/{filename}.json", "w") as f:
            f.write(json_str)

    print("JSON write OK")
    file.close()
    print("Finished")

if __name__ == "__main__":
    main() 