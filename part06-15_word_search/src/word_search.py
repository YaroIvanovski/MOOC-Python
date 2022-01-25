# Write your solution here
import re
def find_words(search_term: str):
    search = []
    word = []

    with open("words.txt") as filename:
        for line in filename:
            word.append(line.replace("\n", ""))

    if "." not in search_term and "*" not in search_term:
        for i in range(0, len(word)):
            if search_term == word[i]:
                search.append(word[i])

    if "*" in search_term:
        if search_term.startswith("*"):
            for i in range(0, len(word)):
                if word[i].endswith(search_term[1:]):
                    search.append(word[i])
        if search_term.endswith("*"):
            for i in range(0, len(word)):
                if word[i].startswith(search_term[0:-1]):
                    search.append(word[i])
  
    if "." in search_term:
        r = re.compile(r"^%s$" % (search_term),re.DOTALL)
        for i in range(0, len(word)):
            if r.search(word[i]) is not None:
                search.append(word[i])

    return search

if __name__ == "__main__":
    print(find_words("*vokes"))


"""Suggested solution
def find_words(search_term: str):
    results = []
 
    with open("words.txt") as file:
        # This will be needed later
        hakusana_ilman_tahtea = search_term.replace("*","")
 
        for word in file:
            word = word.replace("\n","")
            # Is there an asterisk?
            if "*" in search_term:
                # start or end?
                if search_term[0] == "*":
                    if word.endswith(hakusana_ilman_tahtea):
                        results.append(word)
                else:
                    if word.startswith(hakusana_ilman_tahtea):
                        results.append(word)
            # Is there a dot?
            elif "." in search_term:
                # same length?
                if len(search_term) == len(word):
                    found = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            found = False
                            break
                    if found:
                        results.append(word)
            # No special characters, only whole word matches count
            else:
                if word == search_term:
                    results.append(word)
    return results
"""