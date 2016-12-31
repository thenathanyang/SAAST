def calculate_check(isbn):
    # Calculate the check digit of an ISBN from the first 9 digits
    
    check = sum([x*int(y) for x, y in zip(range(1,10), list(isbn))]) % 11 
    if check == 10:
        check = "X"
    return check

def is_isbn(isbn):
    # Check whether ISBN is correct or not
    if not (isinstance(isbn, basestring)):
    	raise ValueError("Invalid ISBN-10 code")
    else:
    	if (len(isbn) != 10):
    		raise ValueError("Invalid ISBN-10 code")
    	else:
    		return str(calculate_check(isbn)) == str(isbn[9])

if __name__ == "__main__":
	print "This program checks to see if a given ISBN is valid."
	print "It can process ISBN-10 codes.\n"
	isbn = raw_input("Enter the ISBN-10 code to check: ")
	if (is_isbn(isbn)):
		print isbn + " is a valid ISBN-10 code."
	else:
		print isbn + " is not a valid ISBN-10 code."
		print "Expected " + str(calculate_check(isbn)) + ", but found " + str(isbn[9]) + "."
