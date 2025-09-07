class StackUnderflowError(Exception):
    pass

def evaluate(input_data):
    stack = []
    commands = {
        '+': lambda: stack.append(stack.pop() + stack.pop()),
        '-': lambda: stack.append(stack.pop(-2) - stack.pop()),
        '*': lambda: stack.append(stack.pop() * stack.pop()),
        '/': lambda: stack.append(stack.pop(-2) // stack.pop()),
        'dup': lambda: stack.append(stack[-1]),
        'drop': lambda: stack.pop(),
        'swap': lambda: stack.extend([stack.pop(), stack.pop()]),
        'over': lambda: stack.append(stack[-2]),
    }

    def execute(forth, CD = commands):

        #adding new definitions momentarily  
        if forth[0] == ':':
            colon, command_name, *command_token, semicolon = forth.lower().split()
            
            if command_name.isnumeric() or ((command_name[0] == '-') and command_name[1:].isnumeric()):
                raise ValueError("illegal operation")

            command_copy = {**CD} # to archive og definitons b4 new updates to the live dictionary 
            commands[command_name] = lambda: execute( ' '.join(command_token), command_copy) # apply execute function for new command, join back CDS as string to run function  
            return

        for i in forth.lower().split():
            if i in CD: #use CD instead of commands to get the og defintion for the operation 
                CD[i]() # Get the operation and run its assigned function (lambda)
            else:
                try: stack.append(int(i)) # if operation not found it is hopefully a number that just needs to be added to stack until stack can be used for a operation --> int() will fail (throw an exception) if it's not a valid integer
                except: raise ValueError("undefined operation") 

    try:
        for line in input_data:
            execute(line) # commands is default so doesnt need ot be mentioned in arguement 

    except IndexError:
        raise StackUnderflowError("Insufficient number of items in stack")
    except ZeroDivisionError:
        raise ZeroDivisionError("divide by zero")

    return stack
