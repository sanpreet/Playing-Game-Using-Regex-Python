#############Playing Game with Regular exppressions*********************************
# Email Validation with some emails
#Rules for writing the valid emails
#First character must be a alphabet
#Second character must be a letter
# Third is a wild card character
#Fourth Character must be @
#FITH Character [a-z] comes within Plus so you can add as many charaters as you can but it must be only lower aplhabets.
#It is followed by dot
#Here you can write only three characters, first one being lower alphaber character followed by two  wild card character
import re
def test_email(pattern):
    pattern = re.compile(pattern)
    # return pattern
    emails = ["j1_@example.com", "sany26.com@gmail.com", "s9%@gmail.c@#1","432",'j1_@example1.com','s1(@hmail.fco']
    for email in emails:
            if not re.match(pattern, email):
                print "You failed to match %s" % (email)
            else:
                print "Pass"

pattern = r"(^[a-z][0-9].+@[a-z]+\.[a-z]..$)"
print (pattern)
output = test_email(pattern)
