def commands(binary_str):

    commands = ['wink', 'double blink', 'close your eyes', 'jump', 'reverse']
    reversed_commands = commands[::-1]
    command_list = [reversed_commands[index] for index, binary in enumerate(binary_str)
                    if binary_str[index] == "1"]
            
    return command_list[1:] if "reverse" in command_list else command_list[::-1]



