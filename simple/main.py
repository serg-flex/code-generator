#  Setup simple int for encoding message
CODE_KEY = 5
#  Get source message from stdin
source = input("Enter message for coding: \n")


#  Encoding message using our CODE_KEY
def encode_source(source: str) -> str:
    #  Convert ascii to int and add CODE_KEY value to it
    converted = [ord(char) + CODE_KEY for char in source]
    #  Return string with new ascii codes for symbols
    return "".join(chr(char) for char in converted)


#  Decoding message using our CODE_KEY
def decode_message(source: str) -> str:
    #  Convert ascii to int and subtruct CODE_KEY value from it
    converted = [ord(char) - CODE_KEY for char in source]
    #  Return string with new ascii codes for symbols
    return "".join(chr(char) for char in converted)


#  Print encoded and decoded message
result = encode_source(source)
print(f"Coded message: {result}")
print(f"Decoded message: {decode_message(result)}")
