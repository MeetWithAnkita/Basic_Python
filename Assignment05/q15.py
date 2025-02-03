# Input text
text = input("Enter a text: ").lower()
# Count articles
articles = text.split().count("a") + text.split().count("an") + text.split().count("the")
print("Number of articles (a, an, the):", articles)