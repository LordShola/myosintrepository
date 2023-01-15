def get_code_from_secret(location,password):
    file2.connect_to_secure(location,password)



perma_link=get_code_from_secret("https://localhost:8080/data",help.get_complete_input_from_keyboard())
#debug testing
file2.debug("Test1")
help.cool_stuff()
help.more_stuff(10)
file2.debug("test:"+str(file2.sha256(help.get_complete_input_from_keyboard())))
help.create_super_mega_ultra_cool_thing(perma_link)
file2.debug("part 2 worked!")