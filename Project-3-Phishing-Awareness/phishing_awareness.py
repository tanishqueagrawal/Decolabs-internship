import re

print("=" * 50)
print("      PHISHING AWARENESS ANALYZER")
print("=" * 50)

message = input("\nPaste the email/message:\n\n")

red_flags = []

keywords = [
    "urgent",
    "verify",
    "password",
    "bank",
    "login",
    "click here",
    "limited time",
    "winner",
    "free",
    "claim",
    "gift",
    "otp",
    "account suspended",
    "update",
    "confirm",
    "prize"
]

for word in keywords:
    if word.lower() in message.lower():
        red_flags.append(f"Suspicious keyword found: '{word}'")

urls = re.findall(r'https?://\S+|www\.\S+', message)

if urls:
    red_flags.append("Contains website link(s)")
    for url in urls:
        if "bit.ly" in url or "tinyurl" in url:
            red_flags.append(f"Shortened URL detected: {url}")

if "@" not in message and ("bank" in message.lower() or "login" in message.lower()):
    red_flags.append("Message does not contain a verified sender.")

print("\n========== ANALYSIS ==========")

if len(red_flags) == 0:
    print("No phishing indicators detected.")
    print("Risk Level : LOW")
else:
    print("Possible Phishing Detected!\n")
    print("Red Flags:")
    for i, flag in enumerate(red_flags, 1):
        print(f"{i}. {flag}")

    if len(red_flags) <= 2:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    print(f"\nRisk Level : {risk}")

print("\nStay alert. Never click unknown links or share passwords/OTP.")