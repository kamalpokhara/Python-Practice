# Write a Python function extract_emails(text)
# that uses a regular expression to find all
# email addresses in a given string.

import re


def ext_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    email = re.search(pattern, text)

    return email


sample_text = "hello my email is kamal207@gmail.com"
print(ext_email(sample_text))
