import dis

code = b'\x97\x00d\x01}\x01d\x02}\x02d\x03d\x00d\x00d\x04\x85\x03\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x03d\x05}\x04d\x06}\x05d\x07D\x00]\x1c}\x06|\x04t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x06|\x05z\x0c\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00z\r\x00\x00}\x04|\x05d\x08z\r\x00\x00}\x05\x8c\x1d|\x00d\x08\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00z\x02\x00\x00d\tz\x05\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x07d\x05}\x08d\nD\x00].}\x06t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x06\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\t|\td\x0bz\n\x00\x00d\x0cz\x06\x00\x00}\n|\x08t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\n|\x01z\x0c\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00z\r\x00\x00}\x08\x8c/d\r}\x0b|\x02|\x03z\x00\x00\x00|\x04z\x00\x00\x00|\x07z\x00\x00\x00|\x08z\x00\x00\x00|\x0bz\x00\x00\x00}\x0cd\x0eS\x00'
consts = [None, 79, '{7ctLj4', 'FSqgAcpFMrU3qhfu1jNpf', -1, '', 16, b'\\)\\umQDqpk`h(jL', 1, 87, 'ALs[', 69, 128, 'L}', '{8hHVpauQQYxfSCQodUoBn8uZWY9Pi952QC9WP13oDpQNt9cswHJxdBbadrY}']
 
varnames = ['key', 'val', 'p1', 'p2', 'p3', 'x', 'c', 'p4', 'p5', 'enc', 'sub', 'p6', 'flag']
 
names = ['chr', 'ord']


def analyze_bytecode(bytecode, constants, variable_names, name_list):
    current_state = "operation"

    for idx, instruction in enumerate(bytecode):
        instruction = instruction

        if current_state == "operation":
            print()
            output_end = "\n"
            if instruction > dis.HAVE_ARGUMENT:
                current_state = "argument1"
                output_end = "\n\t "
            print(f"{idx}.\t[{hex(instruction)}]{dis.opname[instruction]}", end=output_end)

        elif current_state == "argument1":
            argument = None
            
            if previous_op.startswith("STORE"):
                if previous_op.endswith("FAST"):
                    argument = "Storing in " + variable_names[instruction]

            elif previous_op.startswith("LOAD"):
                if previous_op.endswith("FAST"):
                    argument = "Retrieving from " + variable_names[instruction]
                elif previous_op.endswith("CONST"):
                    argument = constants[instruction]
                elif previous_op.endswith("METHOD") or previous_op.endswith("GLOBAL"):
                    if instruction > 2:
                        continue
                    argument = name_list[instruction]
            print(f"[{hex(instruction)}]{argument}")
            current_state = "operation"

        previous_op = dis.opname[instruction]


analyze_bytecode(code, consts, varnames, names)