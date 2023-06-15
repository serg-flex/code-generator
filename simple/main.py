#  Setup simple int for coding message
CODE_KEY = 5
#  Get source message from stdin
source = input("Enter message for coding: \n")


#  Coding message using our CODE_KEY
def code_source(source: str) -> str:
    #  Convert ascii to int and add CODE_KEY value to it
    converted = [ord(char) + CODE_KEY for char in source]
    #  Return string with new ascii codes for symbols
    return "".join(chr(char) for char in converted)


def decode_message(source: str) -> str:
    converted = [ord(char) - CODE_KEY for char in source]
    return "".join(chr(char) for char in converted)


#  Print coded and decoded message
result = code_source(source)
print(f"Coded message: {result}")
print(f"Decoded message: {decode_message(result)}")
