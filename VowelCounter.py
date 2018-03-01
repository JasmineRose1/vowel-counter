# write a program that prints out the number of vowels in a string

# ask the user for a string

def count_vowels():
    string=raw_input("Please enter a string: ")
    vowel_sum  = 0 #initializing the sum
    # define what a vowel is
    vowels = ["a", "e", "i", "o", "u"]
    for index in range(len(string)):
        if string[index] in vowels:
            vowel_sum = vowel_sum + 1
    print vowel_sum, "vowel(s) in ", string

count_vowels()
