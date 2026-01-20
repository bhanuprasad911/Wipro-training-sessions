import re

def validate_password(password):
    """
    Validates a strong password based on specific rules using lookahead assertions.
    Rules:
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    
    # Regex Pattern Explanation:
    # ^                         : Start of string
    # (?=.*[a-z])               : Lookahead - at least one lowercase letter
    # (?=.*[A-Z])               : Lookahead - at least one uppercase letter
    # (?=.*\d)                  : Lookahead - at least one digit
    # (?=.*[@$!%*?&])           : Lookahead - at least one special character
    # [A-Za-z\d@$!%*?&]{8,}     : Match any combination of allowed chars, min length 8
    # $                         : End of string
    
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    if re.match(pattern, password):
        return f"'{password}' is a Valid Strong Password"
    else:
        return f"'{password}' is Invalid (Weak Password)"

def demonstrate_modifiers():
    """
    Demonstrates how re.IGNORECASE, re.MULTILINE, and re.DOTALL affect pattern matching.
    """
    print("\n--- Modifier Demonstrations ---")

    # 1. re.IGNORECASE
    # Matches letters regardless of case (A matches a)
    text = "Python Programming"
    pattern_ignore = r"python"
    
    match = re.search(pattern_ignore, text, re.IGNORECASE)
    print(f"\n1. re.IGNORECASE: Searching 'python' in '{text}'")
    print(f"   Match Found: {match.group() if match else 'None'}")

    # 2. re.MULTILINE
    # Allows ^ and $ to match start/end of each line, not just start/end of string
    text_multiline = """First Line
Second Line
Third Line"""
    pattern_multiline = r"^Second" # Looks for 'Second' at the start of a line
    
    # Without modifier (fails because 'Second' isn't at start of string)
    no_mod = re.search(pattern_multiline, text_multiline)
    # With modifier (succeeds because 'Second' is at start of line 2)
    with_mod = re.search(pattern_multiline, text_multiline, re.MULTILINE)
    
    print(f"\n2. re.MULTILINE: Searching '^Second' in multi-line text")
    print(f"   Without Modifier: {no_mod}")
    print(f"   With Modifier:    {with_mod.group() if with_mod else 'None'}")

    # 3. re.DOTALL
    # Makes the '.' character match everything, including newlines (\n)
    text_dotall = "Hello\nWorld"
    pattern_dotall = r"Hello.World" # The dot needs to match \n
    
    # Without modifier (fails because . does not match \n)
    no_mod_dot = re.match(pattern_dotall, text_dotall)
    # With modifier (succeeds because . matches \n)
    with_mod_dot = re.match(pattern_dotall, text_dotall, re.DOTALL)
    
    print(f"\n3. re.DOTALL: Matching 'Hello.World' against 'Hello\\nWorld'")
    print(f"   Without Modifier: {no_mod_dot}")
    print(f"   With Modifier:    {with_mod_dot.group() if with_mod_dot else 'None'}")

# --- Main Execution ---

# 1. Test Password Validation
print("--- Password Validation Tests ---")
passwords_to_test = [
    "weak",             # Too short
    "onlylowercase1",   # No uppercase
    "ONLYUPPERCASE1",   # No lowercase
    "NoDigits!!",       # No digits
    "NoSpecialChar1",   # No special char
    "Strong@Pass1"      # Valid
]

for pwd in passwords_to_test:
    print(validate_password(pwd))

demonstrate_modifiers()