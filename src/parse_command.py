"""
Recieves command from Linebot, and generates message based on the commanda

"""

import re
import openai
from random import sample

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
    pattern = r'^\? [a-zA-Z]+( [a-zA-Z]+)* *$'

        # Match the pattern against the input string
    match = re.match(pattern, msg)

    if match:
        # Extract the part of the string after the `?` and split it into words
        matched_string = msg[2:].strip()
        # Join the words and extract unique characters
        unique_alphabets = set(matched_string.replace(" ", ""))
        return list(unique_alphabets)
    else:
        # Return None if the input does not match the pattern
        return []

def pattern_match_prompt(input_string):
    # Define the regular expression pattern
    pattern = r'^! ?(.*)$'

    # Match the pattern against the input string
    match = re.match(pattern, input_string)

    if match:
        # Extract the text after the `!`
        extracted_text = match.group(1)
        return extracted_text.strip()  # Strip leading and trailing spaces
    else:
        # Return None if the input does not match the pattern
        return ""

def pattern_match_explain(msg:str):
    pattern = r'^! ?explain$'

    return re.match(pattern, msg)

def GPT_response(message:dict[str, str]):
    # 接收回應
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", prompt=message, temperature=0.5, max_tokens=500)
    print(response)
    # 重組回應
    answer = response.choices[0].message.content.strip()
    return answer

def gen_sentence(word_list:list[str]):
    messages = [
        {"role": "system", "content": "use the following vocabularies in a sentence that resembles a GRE verbal test. After the sentence, explain why these words make sense in this context."},
        {"role": "user", "content": " ".join(word_list)},
    ]
    word_labeled  = '  '.join([f"{chr(97 + i)}) {item}" for i, item in enumerate(word_list)])

    respond = GPT_response(messages)
    respond += f"\n {word_labeled}"

    return respond


def message_handler(msg:str, vocabs):
    leading_symbol = msg[0]
    command = msg[1:].strip()


    # match ! new
    if vocab_n := pattern_match_new(msg):
        return gen_sentence(sample(vocabs, vocab_n))

    # match ? a b c, indicating that the user does not recognize vocabulary a, b and c
    if unknown_match_list := pattern_match_record(msg):
        # record(unknown_match_list)
        return f"Word list {unknown_match_list} saved"

    if pattern_match_explain(msg):
        return "Explaining current data"
    if prompt := pattern_match_prompt(msg):
        return prompt
    else:
        return "Invalid command."

