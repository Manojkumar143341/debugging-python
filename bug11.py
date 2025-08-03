def anag(s1,s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)
print(anag("Listen", "Silent"))  # Expected: True