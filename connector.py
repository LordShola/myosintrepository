def get_code_from_secret(location,password):
    file2.connect_to_secure(location,password)

def get_input():
    input=""
    while help.get_input_stream()==True:
        input+=help.get_input_from_keyboard()

    return input


perma_link=get_code_from_secret("https://pastebin.com/SyjRsXih",get_input())
help.create_super_mega_ultra_cool_thing(perma_link)