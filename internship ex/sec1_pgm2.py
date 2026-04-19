def is_anagram(s,t):
    if sorted(s) == sorted(t):
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")
s = input("Enter the first string: ")
t = input("Enter the second string: ")
is_anagram(s, t)