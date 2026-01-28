emails = ["@adbu.com","mehedi@gmail.com", "test@@mail.com", "user@domain", "hello@world.com"]


def validate_emails(emails):
   valid_emails = []
   for email in emails:
        if email.count('@') != 1:
            continue;
        
        local,domain = email.split("@");

        if "." in domain and domain[0] != "." and (local and domain) != "":
           valid_emails.append(email);
   
   return valid_emails;

# test

output = validate_emails(emails);
print(output);

