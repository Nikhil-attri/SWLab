
import re
import os
from collections import defaultdict

class CrosswordCheater:
    def __init__(self, wordlist_file="wordlist.txt"):
        """Initialize the crossword cheater with a wordlist file"""
        self.words = []
        self.load_wordlist(wordlist_file)
    
    def load_wordlist(self, filename):
        """Load words from a text file"""
        try:
            # Try to load from the specified file
            with open(filename, 'r', encoding='utf-8') as file:
                self.words = [word.strip().lower() for word in file.readlines() if word.strip()]
            print(f"✅ Loaded {len(self.words)} words from {filename}")
        except FileNotFoundError:
            print(f"⚠️ {filename} not found. Creating a sample wordlist...")
            self.create_sample_wordlist(filename)
    
    def create_sample_wordlist(self, filename):
        """Create a sample wordlist for demonstration"""
        sample_words = [
            "thickly", "thirdly", "quickly", "quietly", "clearly", "closely",
            "broadly", "briefly", "greatly", "lightly", "rightly", "tightly",
            "monthly", "ghostly", "jointly", "courtly", "shortly", "sweetly",
            "swiftly", "directly", "perfectly", "completely", "absolutely",
            "wonderful", "beautiful", "powerful", "peaceful", "helpful",
            "careful", "grateful", "fearful", "cheerful", "harmful",
            "python", "programming", "computer", "science", "technology",
            "algorithm", "function", "variable", "database", "network",
            "security", "software", "hardware", "internet", "website",
            "application", "development", "framework", "library", "module"
        ]
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for word in sample_words:
                    file.write(word + '\n')
            self.words = sample_words
            print(f"✅ Created sample wordlist with {len(sample_words)} words")
        except Exception as e:
            print(f"❌ Error creating sample wordlist: {e}")
            # Fallback to using the sample words directly
            self.words = sample_words
    
    def pattern_to_regex(self, pattern):
        """Convert a pattern with asterisks to a regex pattern"""
        # Escape special regex characters except asterisks
        escaped = re.escape(pattern)
        # Replace escaped asterisks with regex wildcard
        regex_pattern = escaped.replace(r'\*', '.')
        return f"^{regex_pattern}$"
    
    def find_matches(self, pattern):
        """Find all words that match the given pattern"""
        if not pattern:
            return []
        
        pattern = pattern.lower().strip()
        regex_pattern = self.pattern_to_regex(pattern)
        
        try:
            compiled_regex = re.compile(regex_pattern)
            matches = [word for word in self.words if compiled_regex.match(word)]
            return sorted(matches)
        except re.error as e:
            print(f"❌ Invalid pattern: {e}")
            return []
    
    def find_matches_by_length(self, length):
        """Find all words of a specific length"""
        return sorted([word for word in self.words if len(word) == length])
    
    def find_matches_containing(self, letters):
        """Find all words containing specific letters"""
        letters = letters.lower()
        return sorted([word for word in self.words if all(letter in word for letter in letters)])
    
    def get_statistics(self):
        """Get statistics about the loaded wordlist"""
        if not self.words:
            return {}
        
        length_dist = defaultdict(int)
        for word in self.words:
            length_dist[len(word)] += 1
        
        return {
            'total_words': len(self.words),
            'shortest_word': min(self.words, key=len),
            'longest_word': max(self.words, key=len),
            'average_length': sum(len(word) for word in self.words) / len(self.words),
            'length_distribution': dict(length_dist)
        }

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("🎯 CROSSWORD CHEATER")
    print("="*50)
    print("1. Find words matching pattern (with *)")
    print("2. Find words by length")
    print("3. Find words containing specific letters")
    print("4. View wordlist statistics")
    print("5. Exit")
    print("="*50)

def display_matches(matches, pattern=""):
    """Display the matching words in a formatted way"""
    if not matches:
        print("❌ No matches found!")
        return
    
    print(f"\n✅ Found {len(matches)} match(es)" + (f" for pattern '{pattern}'" if pattern else "") + ":")
    print("-" * 40)
    
    # Display in columns for better readability
    cols = 3
    for i in range(0, len(matches), cols):
        row = matches[i:i+cols]
        print("  ".join(f"{word:<15}" for word in row))
    
    print("-" * 40)

def main():
    """Main function to run the crossword cheater program"""
    print("🚀 Starting Crossword Cheater Program...")
    
    # Initialize the crossword cheater
    cheater = CrosswordCheater()
    
    if not cheater.words:
        print("❌ No words loaded. Exiting...")
        return
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                pattern = input("\nEnter pattern (use * for unknown letters): ").strip()
                if pattern:
                    print(f"\n🔍 Searching for words matching '{pattern}'...")
                    matches = cheater.find_matches(pattern)
                    display_matches(matches, pattern)
                else:
                    print("❌ Please enter a valid pattern!")
            
            elif choice == '2':
                try:
                    length = int(input("\nEnter word length: ").strip())
                    if length > 0:
                        print(f"\n🔍 Searching for {length}-letter words...")
                        matches = cheater.find_matches_by_length(length)
                        display_matches(matches, f"{length} letters")
                    else:
                        print("❌ Please enter a positive number!")
                except ValueError:
                    print("❌ Please enter a valid number!")
            
            elif choice == '3':
                letters = input("\nEnter letters that must be in the word: ").strip()
                if letters:
                    print(f"\n🔍 Searching for words containing '{letters}'...")
                    matches = cheater.find_matches_containing(letters)
                    display_matches(matches, f"containing '{letters}'")
                else:
                    print("❌ Please enter some letters!")
            
            elif choice == '4':
                stats = cheater.get_statistics()
                print("\n📊 WORDLIST STATISTICS")
                print("=" * 30)
                print(f"Total words: {stats['total_words']}")
                print(f"Shortest word: {stats['shortest_word']} ({len(stats['shortest_word'])} letters)")
                print(f"Longest word: {stats['longest_word']} ({len(stats['longest_word'])} letters)")
                print(f"Average length: {stats['average_length']:.2f} letters")
                
                print("\nLength distribution:")
                for length, count in sorted(stats['length_distribution'].items()):
                    print(f"  {length} letters: {count} words")
            
            elif choice == '5':
                print("\n👋 Thanks for using Crossword Cheater! Goodbye!")
                break
            
            else:
                print("❌ Invalid choice! Please select 1-5.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

def demo():
    """Demonstration function showing program capabilities"""
    print("\n🎬 DEMONSTRATION MODE")
    print("=" * 50)
    
    cheater = CrosswordCheater()
    
    # Demo patterns
    demo_patterns = [
        "th***ly",
        "c**e",
        "pro*****ng",
        "***ful",
        "*y*h*n"
    ]
    
    for pattern in demo_patterns:
        print(f"\n🔍 Testing pattern: '{pattern}'")
        matches = cheater.find_matches(pattern)
        display_matches(matches[:10], pattern)  # Show only first 10 matches
        
        if len(matches) > 10:
            print(f"... and {len(matches) - 10} more matches")

if __name__ == "__main__":
    print("Choose mode:")
    print("1. Interactive Mode")
    print("2. Demo Mode")
    
    try:
        mode = input("Enter choice (1-2): ").strip()
        if mode == '2':
            demo()
        else:
            main()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")