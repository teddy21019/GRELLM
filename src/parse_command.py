"""
Recieves command from Linebot, and generates message based on the commanda

"""


def message_handler(msg:str):
    leading_symbol = msg[0]
    command = msg[1:].strip()
    if leading_symbol == "!":
        return "Parsing with ChatGPT"
    elif leading_symbol == "?":
        return "Interacting with server"
    else:
        return "Invalid command"


def message_handler2(msg:str):
    leading_symbol = msg[0]
    command = msg[1:].strip()
    if leading_symbol == "!":
        if command == "new":                        # ! new 4
            return get_vocab_from_GPT()

        elif command == "review":
            vocab_list = get_history_review_list()
            return get_vocab_from_GPT(vocab_list)

        else:
            return gpt_response(command)
        return "Parsing with ChatGPT"
    elif leading_symbol == "?":

        return "Interacting with server"
    else:
        return "Invalid command"

