import re
import getpass

def check_password_strength(password):
    """Evaluate password strength and provide suggestions."""
    # Initialize criteria flags
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_symbol = bool(re.search(r'[^\w\s]', password))
    sufficient_length = len(password) >= 8

    # Calculate score
    score = sum([has_upper, has_lower, has_digit, has_symbol, sufficient_length])
    
    # Determine strength rating
    if score <= 2:
        strength = "Very Weak"
    elif score == 3:
        strength = "Weak"
    elif score == 4:
        strength = "Moderate"
    elif score == 5:
        strength = "Strong"
    else:  # Extra long passwords
        strength = "Very Strong" if len(password) >= 12 else "Strong"

    # Generate suggestions
    suggestions = []
    if not sufficient_length:
        suggestions.append("Add more characters (minimum 8)")
    if not has_upper:
        suggestions.append("Include uppercase letters (A-Z)")
    if not has_lower:
        suggestions.append("Include lowercase letters (a-z)")
    if not has_digit:
        suggestions.append("Include numbers (0-9)")
    if not has_symbol:
        suggestions.append("Include symbols (!@#$%^&*, etc.)")
    if len(suggestions) == 0 and len(password) < 12:
        suggestions.append("Consider making it longer (12+ characters)")

    return strength, suggestions

def display_results(strength, suggestions):
    """Display formatted results to the user"""
    print("\n" + "="*40)
    print(f"Password Strength: {strength}")
    print("="*40)
    
    if suggestions:
        print("\nSuggestions for improvement:")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"{i}. {suggestion}")
    else:
        print("\nYour password is strong! Good job!")

def main():
    """Main program interface"""
    print("="*40)
    print("PASSWORD STRENGTH CHECKER".center(40))
    print("="*40)
    print("\nEnter your password for evaluation")
    print("(Password won't be displayed on screen)\n")
    
    while True:
        password = getpass.getpass("Password: ").strip()
        if password:
            break
        print("Error: Password cannot be empty. Please try again.")
    
    strength, suggestions = check_password_strength(password)
    display_results(strength, suggestions)

if __name__ == "__main__":
    main()
