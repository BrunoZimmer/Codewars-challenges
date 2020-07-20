def reverse_words(str):
  return ' '.join(s[::-1] for s in str.split(' '))


# def reverse_words_first(text):
#     separated_words = text.split(' ')
#     #print(separated_words)
    
#     def Reverse_Word (word):
#         return word[::-1]
    
#     final_text = " ".join(list(map(Reverse_Word, separated_words)))
    
#     print(final_text)

#     return final_text