letter = '''Dear <|Name|>, 
            You are selected!
            <|Date|>''' 
print(letter.replace("<|Name|>", "MrBean").replace("|<|Date|>", "29 April 2100"))
