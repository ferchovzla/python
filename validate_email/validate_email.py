# Python program to validate an Email 

# re module provides support 
# for regular expressions 
import re 

# Regular expression for validating an Email 
regex = '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$'
	
# Function for validating an Email 
def validate_email(email): 

	# use the match function with pattern regex and email 
	if(re.search(regex,email)): 
		print(email+": (_/) VALID") 
	else: 
		print(email+": (X) INVALID") 
	
 
if __name__ == '__main__' : 
	
	emails = ["fernandomontilla@gmail.com", \
	          "fernando.montilla.02@gmail.com", \
	          "fernando.@montilla.02@gmail.com", \
	          "my.ownsite@mydomain.org",\
	          "my.$%wrongname@mydomain.net",\
	          "venezuela.info",\
	          "ferchodeveloper@myempresa.com.ve"]

	for email in emails:
		validate_email(email)

    