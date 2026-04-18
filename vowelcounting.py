word = input("Enter the word: ")
vowels = "aeiouAEIOU"
count = 0
for ch in word:
	if ch not in vowels:
		count +=1
print("Vowel Count is: ",count)

