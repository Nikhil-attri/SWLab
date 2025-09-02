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
