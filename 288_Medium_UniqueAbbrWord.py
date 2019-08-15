"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
"""

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.mappie = {}
        for word in dictionary:
            abbrs = self.abbreviate(word)
            if abbrs in self.mappie:
                self.mappie[abbrs].add(word)
            else:
                self.mappie[abbrs] = set()
                self.mappie[abbrs].add(word)

    def isUnique(self, word: str) -> bool:
        abbrs = self.abbreviate(word)
        if abbrs in self.mappie:
            if word not in self.mappie[abbrs]:
                return False
            else:
                if word in self.mappie[abbrs] and len(self.mappie[abbrs]) > 1:
                    return False
            
        return True
        
        
    def abbreviate(self, word: str) -> str:
        if len(word) < 3:
            return word
        abbr = word[0] + str(len(word) - 2) + word[len(word)-1]
        return abbr
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
