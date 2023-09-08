# pylint: disable=anomalous-backslash-in-string
"""
.        Matches any single character
\        Escapes one of the meta characters to treat it as a regular character
[...]    Matches a single character or a range that is contained within brackets
         _- -_ order does not matter but without brackets order does matter
+        Matches the preceding element one or more times
?        Matches the preceding pattern element zero or one time
*        Matches the preceding element zero or more times
{m,n}    Matches the preceding element at least m and not more than n times
^        Matches the beginning of a line or string
$        Matches the end of a line or string
[^...]   Matches a single character or a range that is not contained within the brackets
?:...|..."Or" operator
()       Matches an optional expression
"""
import re


filenames = ["nov-12.txt", "november-14.txt", "Oct-17.txt", "Nov-22.txt"]
TEXT = "Hi there you here example@example.com @blabla some more text here and there another@example.de"


email_pattern = re.compile("[a-z]+@[a-z]+.[a-z]+")

emails = email_pattern.findall(TEXT)
print(emails)

with open("input/urls", mode="r", encoding="utf-8") as data:
    context = data.read()
url_pattern = re.compile("https?://[^ \n]+\.(?:com|org)")
urls = url_pattern.findall(context)
print(urls)
