class TextProcessor:
    # Implement method overloading for format_text method

    def format_text(self, text1, text2 = ''):
        self.text1 = text1
        self.text2 = text2
        if text2 == '':
            self.text1 = self.text1.upper()
            return self.text1

        if text2:
            return self.text1 + self.text2

# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
