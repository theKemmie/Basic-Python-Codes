def reverse_words(text):
  # split the text into a list of words
  words = text.split()

  # reverse the list of words
  reversed_words = words[::-1]

  # join the reversed words into a single string
  reversed_text = ' '.join(reversed_words)

  return reversed_text
