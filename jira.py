import re

def crossword_cheater(pattern, wordlist):
    """
    pattern : string with letters and '*' for unknowns
    wordlist : list of words to search
    """
    # Convert pattern -> regex
    regex_pattern = "^" + pattern.replace("*", ".") + "$"
    regex = re.compile(regex_pattern, re.IGNORECASE)
    
    # Match words
    matches = [word for word in wordlist if regex.match(word)]
    return matches

if __name__ == "__main__":
    # Example dictionary (can be replaced with real dictionary file)
    wordlist = ["thickly", "thirdly", "thereby", "thinly", "truly", "quickly"]
    
    # User input
    pattern = input("Enter crossword pattern (use * for unknown letters): ").strip()
    
    results = crossword_cheater(pattern, wordlist)
    
    if results:
        print("Possible matches:", ", ".join(results))
    else:
        print("No matches found.")
