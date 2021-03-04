''' The assignment is rather simple, given a string of text i'd like to detect IP Addresses and Persons/Names in the
    string. For example: for input "Bob found that 127.0.0.1 was bad and 123.4.5.6 was safe." Should return that
    127.0.0.1 and 123.4.5.6 are IPAddresses and that Bob is a person. You may use any python packages you wish and
    any data structures/print statements etc to return or show your results. I'm most looking for general discussion
    for any kind of weaknesses with the approach that you would take
'''

# Import Block
import re
import spacy
import en_core_web_sm


# Functions
def is_valid_ip(ip):
    '''
    :param ip: string of text that could represent an IPv4 address
    :return: True if IP
    '''
    nums = ip.split(sep=".")
    return len(nums) == 4 and all(0 <= int(num) < 256 for num in nums)


def find_ips(input_string):
    '''
    :param input_string: String to tested
    :return: list of strings containing potential IP matches
    '''
    regex_pattern = r'((?<=[^a-zA-Z0-9.])|(?=^))([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})(?=[^a-zA-Z0-9.]|$|\s|\.$)'
    # regex with 3 groups:
    # 1- (\b including '.')
    # 2- (4 sets of numbers separated by '.')
    # 3- (end of string OR \b including '.' OR '.' at end of string

    ips = [x.group() for x in re.finditer(regex_pattern, input_string)]
    return [ip for ip in ips if is_valid_ip(ip)]


if __name__ == '__main__':
    test_string = "Bob found that 127.0.0.1 was bad and 123.4.5.6 was safe."
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(test_string)

    print('--- Names ---')
    print([entity.text for entity in doc.ents if entity.label_ == "PERSON"])

    print('\n\n--- IPs ---')
    print(find_ips(test_string))
