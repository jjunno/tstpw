from classes.ruleset import Ruleset

class Password:
    def __init__(self, original):
      self.original = original
      self.filenames = ["surnames_fi_avoindata.txt", "firstnames_men_fi_avoindata.txt", "firstnames_women_fi_avoindata.txt", "lang_fi_kotus.txt", "100k-most-used-passwords-NCSC.txt"]
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
      rule_methods = [
            r.prepend_ruleset,
            r.append_ruleset,
            r.upper_case,
            r.char_capitalization,
            r.leet_style,
            r.repititon,
            r.dates
      ]
      return any(rule() for rule in rule_methods)