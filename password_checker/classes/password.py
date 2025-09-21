from classes.ruleset import Ruleset

class Password:
    def __init__(self, original):
        self.original = original
        self.filenames = ["firstnames_men_fi_avoindata.txt", "firstnames_women_fi_avoindata.txt", "surnames_fi_avoindata.txt", "lang_fi_kotus.txt", "100k-most-used-passwords-NCSC.txt"]
        self.words = []

        print(f"Original password is \"{original}\"")
        self.read_files()

    def read_files(self):
        for filename in self.filenames:
                file = open(f"material/wordlists_parsed/{filename}", "r", encoding="utf-8")
                content = file.read()
                for line in content.splitlines():
                    self.words.append(line)
                
        print(f"{len(self.filenames)} files read, total {len(self.words)} words found")

    # Does original password exist in words as it is
    def is_in_lists(self):
        for word in self.words:
            if word == self.original:
                return True
        return False
    
    def apply_ruleset(self):
        r = Ruleset(self)
        if r.prepend_ruleset():
              return True
        if r.append_ruleset():
              return True
        if r.upper_case():
              return True
        if r.char_capitalization():
              return True
        if r.leet_style():
              return True
        if r.repititon():
              return True
        if r.dates():
              return True
        return False