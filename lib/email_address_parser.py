# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
        emails_found = email_pattern.findall(self.emails)
        return sorted(set(emails_found))
