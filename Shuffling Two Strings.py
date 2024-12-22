import secrets

def secure_jumble_strings(string1, string2):
    # Combine both strings into a single list of characters
    combined = list(string1 + string2)
    
    # Securely shuffle the list
    for i in range(len(combined) - 1, 0, -1):
        # Generate a secure random index
        j = secrets.randbelow(i + 1)
        # Swap the current element with the random index
        combined[i], combined[j] = combined[j], combined[i]
    
    # Join the shuffled characters back into a string
    jumbled = ''.join(combined)
    return jumbled

# Get input strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Generate the securely jumbled string
result = secure_jumble_strings(string1, string2)
print("Securely jumbled string:", result)
