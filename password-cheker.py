import re

def check_password(password):
    score = 0
    feedback = []
    if len(password) < 8:
        feedback.append("❌ Password should be at least 8 characters long.")
        print("\nPassword Strength: Very Weak 🔴")
        for f in feedback:
            print(f)
        return
    if re.search(r'[A-Z]', password):
        score += 1  
    else:
        feedback.append("❌ Password should contain at least one uppercase letter.")
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one lowercase letter.")
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")
    if re.search(r'[!@#$%^&*()-+]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character.")

    levels = ["Very Weak 🔴", "Weak 🟠", "Moderate 🟡", "Strong 🟢", "Very Strong 🔵"]
    
     
    print(f"\nPassword Strength: {levels[score]}")
    for f in feedback:
        print(f)    


check_password(input("Enter your password: ") )