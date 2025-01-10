file_path = "books/frankenstein.txt"

with open(file_path) as f:
    file_contents = f.read()

wordcount = len(file_contents.split())
file_contents = file_contents.lower()

# Count letters
letter_counts = {}

for c in file_contents:
    if c.isalpha():
        if c in letter_counts:
            letter_counts[c] += 1
        else:
            letter_counts[c] = 1

sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

# Print report
print(f"--- Begin report of {file_path} ---")
print(f"{wordcount} words found in the document")
for k, v in sorted_letter_counts:
    print(f"The '{k}' character was found {v} times")

print("--- End report ---")
