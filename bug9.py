def is_anagram(s1, s2):
  s1= s1.replace(" ", "").lower()
  s2 = s2.replace(" ", "").lower()

  return sorted(s1) == sorted(s2)

print(is_anagram("Listen", "Silent"))  # Expected: True
print(is_anagram("Hello", "Olelh"))    # Expected: True
print(is_anagram("Hi", "Bye"))         # Expected: False
