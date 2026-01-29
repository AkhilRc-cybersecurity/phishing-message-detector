message = input("Enter the message: ")

phishing_keywords = [
    "urgent",
    "click here",
    "verify",
    "account suspended",
    "password",
    "bank",
    "otp",
    "free",
    "winner",
    "limited time"
]

message = message.lower()

is_phishing = False

for word in phishing_keywords:
    if word in message:
        is_phishing = True
        break

if is_phishing:
    print("⚠️ This message is PHISHING")
else:
    print("✅ This message looks SAFE")