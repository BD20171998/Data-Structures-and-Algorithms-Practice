#193. Valid Phone Numbers
# https://leetcode.com/problems/valid-phone-numbers/

# Read from the file file.txt and output all valid phone numbers to stdout.


grep -E '^\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4}$|^[0-9]{3}\-[0-9]{3}\-[0-9]{4}$' file.txt

#grep -E '^(\([0-9]{3}\) [0-9]{3}-[0-9]{4})$|^([0-9]{3}-[0-9]{3}-[0-9]{4})$' file.txt
