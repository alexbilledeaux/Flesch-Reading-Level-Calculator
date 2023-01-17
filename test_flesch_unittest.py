import flesch

content = flesch.readFileIn('unit_test.txt')
assert len(flesch.getSentences(content)) == 4, f"Expected 4 sentences. Recieved {len(flesch.getSentences(content))}."
assert len(flesch.getWords(content, False)) == 23, f"Expected 23 words. Recieved {len(flesch.getWords(content, False))}."
assert flesch.getNumSyllables(content) == 33, f"Expected 30 syllables. Recieved {flesch.getNumSyllables(content)}."

print("All tests successful!")