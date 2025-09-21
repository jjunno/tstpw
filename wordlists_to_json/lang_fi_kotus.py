import json

# Read the entire content of the file.
# Words are in lines such as:
# aakkonen		substantiivi	38
# We extract the first word from each line.
# All words are written to a JSON file.
def main():
    file = open("wordlists_raw/lang_fi_kotus.txt", "r", encoding="utf-8")
    print("Read file OK")
    content = file.read()

    words = []
    for line in content.splitlines():
        words.append(line.split()[0].lower().strip())

    print("Extract words OK")
    json_str = json.dumps(words, indent=4, ensure_ascii=False)
    with open("wordlists_json/lang_fi_kotus.json", "w") as f:
        f.write(json_str)

    print("JSON write OK")
    file.close()
    print("Finished")

if __name__ == "__main__":
    main() 