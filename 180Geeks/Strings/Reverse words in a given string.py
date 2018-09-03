# Given a String of length N reverse the whole string without reversing the individual words in it. Words are separated by dots.

strA = "i.like.this.program.very.much"
words = strA.split(".")

def rev_str(words):
    rev_words = words[::-1]
    # return rev_words

    rev_words_str = ".".join(rev_words)
    return rev_words_str

print(f"Original string: {strA}")
print(f"Reverdes string: {rev_str(words)}")