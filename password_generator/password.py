class Password:
    def __init__(self, original):
        self.original = original
        self.filenames = ["firstnames_men_fi_avoindata.json", "firstnames_women_fi_avoindata.json", "surnames_fi_avoindata.json", "lang_fi_kotus.json"]
        self.words = []

    def read_files(self):
        for filename in self.filenames:
                file = open("wordlists_json/{filename}", "r", encoding="utf-8")
                content = file.read()
                for line in content.splitlines():
                    self.words.append = []
                    print(line)
            # with open(f"wordlists_json/{filename}", "r", encoding="utf-8") as f:
            #     data = f.read()
