import re
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+$"
text = " Moj numer telefonu to:  123-321-312 a moj email to: mkuczek@altcompit.pl"

email = re.search(pattern, text)
print(email)