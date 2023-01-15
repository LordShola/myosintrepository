def get_code_from_secret(location,password):
    file2.connect_to_secure(location,password)



perma_link=get_code_from_secret("https://localhost:8080/data",help.get_complete_input_from_keyboard())
help.cool_stuff()
help.more_stuff(10)
help.create_super_mega_ultra_cool_thing(perma_link)