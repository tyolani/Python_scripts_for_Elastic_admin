"""
Here is a Python script that reads a file called emails.txt, extracts the user ID part of the email (the part before the @ symbol), and writes the extracted user IDs to a new file called userid.txt.
This is useful when creating users on Elastic and you only want to use the ID part given email addresses
"""


# Open the input file (emails.txt) in read mode
with open('emails.txt', 'r') as infile:
    # Read the content of the file
    lines = infile.readlines()

# Open the output file (userid.txt) in write mode
with open('userid.txt', 'w') as outfile:
    # Loop through each line (email) in the input file
    for line in lines:
        # Strip any surrounding whitespace and split by the '@' to extract the user ID
        user_id = line.strip().split('@')[0]
        # Write the user ID to the output file
        outfile.write(user_id + '\n')

print("User IDs extracted and saved to userid.txt")

"""
Explanation:

    The script reads each line (email address) from emails.txt.
    It splits each email address by the @ symbol and takes the first part as the user ID.
    The extracted user IDs are written to userid.txt, one per line.

Make sure to place your emails.txt file in the same directory as the script or provide the full path.

"""
