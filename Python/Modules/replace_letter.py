def replace_character(word, index, letter):
  """
  Replaces a character in a string at a given index.

  Args:
    word: The input string.
    index: The index of the character to replace (0-based).
    letter: The new character to replace with.

  Returns:
    The modified string with the character replaced.
  """

  if 0 <= index < len(word):
    return word[:index] + letter + word[index+1:]
  else:
    return "Invalid index."

# Get input from the user
word = input("Enter a word: ")
index = int(input("Enter the index of the character to replace: "))
letter = input("Enter the new character: ")

# Replace the character and print the result
new_word = replace_character(word, index, letter)
print("Modified word:", new_word)