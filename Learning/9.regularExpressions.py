print("65. Regular Expressions")
# Powerful tool for various kinds of string manipulation
# Very useful:
# Verifying that strings match a pattern (for instance, that a string has the format of an email address)
# performing substitutions in a strings
# can be accessed using re module.
# re.match can be used to determine whether it matches at the beginning of a string
# If it does, match returns an object representing the match, if not, it returns None.
# We use raw strings as r"expression"
import re
pattern = r"spam"
if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No Match")
# Other functions are re.search and re.findall
# re.search: find match anywhere in the string
# re.findall: list of all substrings that match a pattern
pattern = r"spam"
if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")
if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")
print(re.findall(pattern, "eggspamsausagespam"))
# Match will fail, since it only looks at the start of the string
# Search will succeed.
# re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.
# The regex search returns an object with several methods that give details about it.
# group: which returns the string matched,
# start and end: which returns the start and ending positions of the first match
# span: Which returns the start and end positions of the first match as the tuple
pattern = r"pam"
match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
# Search and Replace
# Most important re methods that use regular expressions is sub
# re.sub(pattern, repl, string, count=0)
# This method replaces all occurences of the pattern in string with repl, substituting all
# occurences, unless count provided.
# This method returns the modified string
string = "My name is David. Hi David"
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)


print("66. Simple Metacharacters")
# metacharacters are what make regular expressions more powerful
# To avoid backslah problems, we use the raw string, which is normal string with r in front of it.
# Metacharacters
# dot (.)
# Matches any character, other than a new line.
pattern = r"gr.y"
if re.match(pattern, "grey"):
    print("Match 1")
if re.match(pattern, "gray"):
    print("Match 2")
if re.match(pattern, "blue"):
    print("Match 3")
# Two other metacharacters: ^ and $
# These match the start and end of a string
pattern = r"^gr.y$"
if re.match(pattern, "grey"):
    print("Match 1")
if re.match(pattern, "gray"):
    print("Match 2")
if re.match(pattern, "stingray"):
    print("Match 3")
# The pattern "^gr.y$" means that the string should start with gr, then follow with any character,
# except a newline, and end with y


print("67. Character Classes")
# Provide a way to match only one of a specific set of characters.
# A character class is created by putting the characters it matches inside square brackets.
pattern = r"[aeiou]"
if re.search(pattern, "grey"):
    print("Match 1")
if re.search(pattern, "quertyuiop"):
    print("Match 2")
if re.search(pattern, "rhythm myths"):
    print("Match 3")
# The pattern [aeiou] in the search function matches all strings that contain any one of the charcters defined.
# Range of characters
# class [a-z] matches all lowecase alphabetic characters
# class [G-P] : Fro G to P
# class [0-9]: matches any digit
# Multiple range: [A-Za-z]
pattern = r"[A-Z][A-Z][0-9]"
if re.search(pattern, "LS8"):
    print("Match 1")
if re.search(pattern, "E3"):
    print("Match 2")
if re.search(pattern, "1ab"):
    print("Match 3")
# Place ^ at the start of a character class to invert it.
# Match any character other than the ones included
# Other metacharacters such as $ and ., have no meaning within character classes.
# metacharacter ^ has no meaning unless it is the first character in the class
pattern = r"[^A-Z]"
if re.search(pattern, "this is all quiet"):
    print("Match 1")
if re.search(pattern, "AbCdEfG123")
    print("Match 2")
if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")
# The pattern [^A-Z] excludes uppercase strings.


print("68, More Metacharacters")
# Some more metacharacters are *, +, ?, { and }
# These specify number of repetitions
# * means "zero or more repetitions"
# This "previous thing" can be single character, a class, or a group of characters in parentheses
pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamegg"):
    print("Match 2")
if re.match(pattern, "spam"):
    print("Match 3")
# + : one or more repetitions
pattern = r"g+"
if re.match(pattern, "g"):
    print("Match 1")
if re.match(pattern, "gggggggggg"):
    print("Match 2")
if re.match(pattern, "abc"):
    print("Match 3")
# * : 0 or more
# + : 1 or more
# ? : zero or one repetitions
pattern = r"ice(-)?cream"
if re.match(pattern, "ice-cream"):
    print("Match 1")
if re.match(pattern, "icecream"):
    print("Match 2")
if re.match(pattern, "sausages"):
    print("Match 3")
if re.match(pattern, "ice--ice"):
    print("Match 4")
# Curly Braces
# Used to represent the number of repetitions between two numbers
# {x,y} means "between x and y repetitions of something"
# {0,1} is same thing as ?
# If x is missing, then it is taken as zero
# if y is missing, then it is taken as infinity
pattern = r"9{1,3}$"
if re.match(pattern, "9"):
    print("Match 1")
if re.match(pattern, "999"):
    print("Match 2")
if re.match(pattern, "9999"):
    print("Match 3")


print("69. Groups")
# Creating by surrounding part of regular expression by parentheses.
pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamspamspamegg"):
    print("Match 2")
if re.match(pattern, "spam"):
    print("Match 3")
# contents of the group can be accessed using group function
# group(0) and group(): returns whole match
# group(n) where n>0 : returns the nth group from the left
# method groups() returns all groups up from 1
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())
# Groups can be nested
# Named groups and non-capturing groups.
# Named groups have format: (?P<name>...), where name is the name of the group and ... is the content,
# except they can be accessed by group(name) in addition to its number.
# Non-capturing groups have the format (?:...).
# They are not accessible by group method, so they can be added to an existing regular expression
# without breaking the numbering
pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())
# Imp metacharacter is |
# | means "or".
pattern = r"gr(a|e)y"
match = re.match(pattern, "gray")
if match:
    print("Match 1")
match = re.match(pattern, "grey")
if match:
    print("Match 2")
match = re.match(pattern, "griy")
if match:
    print("Match 3")


print("70. Special Sequences")
# Various special sequences
# Written as backslash followed by another character.
# backslash and a number between 1 and 99.
# e.g. \1 ro \17
pattern = r"(.+) \1"
match = re.match(pattern, "word word")
if match:
    print("Match 1")
match = re.match(pattern, "?! ?!")
if match:
    print("Match 2")
match = re.match(pattern, "abc cde")
if match:
    print("Match 3")
# "(.+)\1" is not the same as "(.+)(.+)" because \1 refers to the first group's subexpression, which is
# the matched expression itself, and not the regex pattern
# More useful special sequences are \d, \s and \w
# These match digits, whitespace and word characters respectively
# In ASCII, they are equivalent to [0-9], [\t\n\r\f\v] and [a-zA-Z0-9_]
# \w mathces letters with accents
# \D, \S and \W mean the opposite to the lower-case version.
# \D matches anything that isn't a digit
pattern = r"(\D+\d)"
match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1")
match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")
match = re.match(pattern, " ! $?")
if match:
    print("Match 3")
# (\D+\d) matches one or more non-digits followed by a digit.
# Additional sequences are \A, \Z and \b.
# The sequence \A and \Z matching the beginning and end of a string, respectively.
# The sequence \b matches the empty string between \w and \W characters, or \w characters and
# the beginning or end of the string.
# it represents the boundary between words.
# \B matches the empty string anywhere else.
pattern = r"\b(cat)\b"
match = re.search(pattern, "The cat sat!")
if match:
    print("Match 1")
match = re.search(pattern, "We s>cat<tered?")
if match:
    print("Match 2")
match = re.search(pattern, "We scattered.")
if match:
    print("Match 3")
# "\b(cat)\b" basically matches the word "cat" surrounded by word boundaries.
# Print Match 1 and Match 2


print("71. Email Extraction")
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
# [\w\.-]+ matches one or more word character, dot or dash
string = "Please contact info@sololearn.com for assitance"
match = re.search(pattern, string)
if match:
    print(match.group())
