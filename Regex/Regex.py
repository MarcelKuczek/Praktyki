import re
pattern = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+).+ (\d{3}-\d{3}-\d{3})"
text = "  Moj email to: mkuczek@altcompit.pl. Moj numer telefonu to:  123-321-312"

emailfon = re.search(pattern, text)
email = emailfon.group(1)
fon = emailfon.group(2)
print("email: " + str(email))
print("fon: " + str(fon))