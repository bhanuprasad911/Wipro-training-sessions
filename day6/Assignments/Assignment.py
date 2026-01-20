import re
#1. Uses re.match() to check whether a string starts with a valid employee ID in the format EMP followed by 3 digits (e.g., EMP123)
empid = "EMP123"
result = re.match(r"EMP\d{3}", empid)
if result:
    print("Match found")
    print(result.group())
else:print("Match not found")

# 2. Uses re.search() to find the first occurrence of a valid email address in a given text
emailid = "my email ids are bhanuprasad@gmail.com and bhanut@gmail.com"
result2 = re.search(r"[a-zA-Z]+@[a-zA-Z]+.[a-zA-Z]{2,}", emailid)

if result2:
    print("Match found")
    print(result2.group())
else:print("Match not found")


#3. Demonstrates the use of meta-characters (., *, +, ?) and special sequences (\d, \w, \s) in the patterns

text = "Year: 2026. User: bhanu_911.   Color: colour vs color. files: aa.txt, aaa.txt, a.txt"

print("--- Metacharacters (., *, +, ?) ---")

# 1. Dot (.): Matches any single character (except newline)
# Matches "Year" or "User" or any 4-letter word ending in 'r'
print(f"Dot (.):       {re.findall(r'..r', text)}") 


# 2. Question Mark (?): Previous character is optional (0 or 1 time)

print(f"Question (?):  {re.findall(r'colou?r', text)}")

# 3. Asterisk (*): Previous character repeats 0 or more times

print(f"Asterisk (*):  {re.findall(r'ba*', 'b ba baa baaa')}")

# 4. Plus (+): Previous character repeats 1 or more times

print(f"Plus (+):      {re.findall(r'aa+', text)}")


print("\n--- Special Sequences (\\d, \\w, \\s) ---")

# 5. \d: Matches any digit [0-9]

print(f"Digits (\\d):   {re.findall(r'\d+', text)}")

# 6. \w: Matches any 'word' character (a-z, A-Z, 0-9, and underscore)
print(f"Word (\\w):     {re.findall(r'User: (\w+)', text)}")

# 7. \s: Matches any whitespace (space, tab, newline)
print(f"Space (\\s):    {re.findall(r'User:.*\s{3}', text)}")




# 4. Prints matched groups using capturing parenthese
  
pattern = r"(\d{2})-(\d{2})-(\d{4})"

text = "Today's date is 20-01-2026."
match = re.search(pattern, text)

if match:
    print(f"Full Match (group 0): {match.group(0)}")
    print(f"Day        (group 1): {match.group(1)}")
    print(f"Month      (group 2): {match.group(2)}")
    print(f"Year       (group 3): {match.group(3)}")
    
    # You can also get all groups at once as a tuple
    print(f"All Groups tuple:     {match.groups()}")
else:
    print("No date found in the format DD-MM-YYYY")


