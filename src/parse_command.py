"""
Recieves command from Linebot, and generates message based on the commanda

"""


def message_handler(msg:str):
    leading_symbol = msg[0]
    command = msg[1:]
    if leading_symbol == "!":
        return "Parsing with ChatGPT"
    elif leading_symbol == "?":
        return "Interacting with server"
    else:
        return "Invalid command"

