"""
Recieves command from Linebot, and generates message based on the commanda

"""

import re

def pattern_match_new(msg:str) -> int:
    """
    Input: '!new' -> Output: 3
    Input: '! new' -> Output: 3
    Input: '! new 3' -> Output: 3
    Input: '!new 9' -> Output: 9
    Input: '! new 10' -> Output: None
    Input: '!new 10' -> Output: None
    Input: '! newa' -> Output: None
    Input: '!newa' -> Output: None
    """
    pattern = r'^! ?new(?: (\d{1}))?$'

    # Match the pattern against the input string
    match = re.match(pattern, msg)

    if match:
        # Extract the number if it exists, otherwise return 3
        number = match.group(1)
        return int(number) if number is not None else 3
    else:
        # Return None if the input does not match the pattern
        return 0




def pattern_match_record(msg:str) -> list[str]:
    """
    Input: '!new' -> Output: 3
    Input: '! new' -> Output: 3
    Input: '! new 3' -> Output: 3
    Input: '!new 9' -> Output: 9
    Input: '! new 10' -> Output: None
    Input: '!new 10' -> Output: None
    Input: '! newa' -> Output: None
    Input: '!newa' -> Output: None
    """
    pattern = r'^\? ?([a-zA-Z]+(?: [a-zA-Z]+)*) *$'


    # Match the pattern against the input string
    match = re.match(pattern, msg)

    if match:
        # Extract the matching part of the string
        matched_string:str = match.group(1)
        # Split the string by spaces to get the list of words
        words = matched_string.split()
        return words
    else:
        # Return None if the input does not match the pattern
        return []



# def message_handler(msg:str):
#     leading_symbol = msg[0]
#     command = msg[1:].strip()


#     if leading_symbol == "!":
#         return "Parsing with ChatGPT"
#     elif leading_symbol == "?":
#         return "Interacting with server"
#     else:
#         return "Invalid command"


def message_handler(msg:str):
    leading_symbol = msg[0]
    command = msg[1:].strip()


    # match ! new
    if vocab_n := pattern_match_new(msg):
        return f"get_vocab_from_GPT({vocab_n})"

    # match ? a b c, indicating that the user does not recognize vocabulary a, b and c
    if unknown_match_list := pattern_match_record(msg):
        # record(unknown_match_list)
        return f"Word list {unknown_match_list} saved"
    else:
        return "Invalid command"

