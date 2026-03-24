# Removing Whitespaces, var assignment, tabs new lines, and f-string 
name = 'There is no other name '
name = name.rstrip()
print(f"{name.upper()}:\n\tPeter\n\tJohn\n\tThomas")

# Removing prefixes
nostarch_url = 'apostle_paul.com'
nostarch_url = nostarch_url.removeprefix('apostle')
print(nostarch_url)

# Escaping a famous quote
quote = "Someone said \"The Earth is located the right distance from the Sun.\""
print(quote)