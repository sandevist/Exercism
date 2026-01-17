class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    """
    Evaluate a Forth program.
    
    Args:
        input_data: List of strings representing the Forth program lines
        
    Returns:
        List representing the final stack state
    """
    stack = []
    definitions = {}
    
    # Process each line of input
    for line in input_data:
        tokens = tokenize(line)
        i = 0
        while i < len(tokens):
            token = tokens[i].lower()
            
            # Handle word definitions
            if token == ':':
                if i + 3 >= len(tokens):
                    raise ValueError("incomplete word definition")
                
                # Get word name (next token)
                word_name = tokens[i + 1].lower()
                
                # Check if word name is a number
                if word_name.isdigit() or (word_name.startswith('-') and word_name[1:].isdigit()):
                    raise ValueError("illegal operation")
                
                # Find the end of definition (;)
                j = i + 2
                definition_tokens = []
                while j < len(tokens) and tokens[j] != ';':
                    subtoken = tokens[j].lower()
                    # EXPAND DEFINITIONS IMMEDIATELY
                    if subtoken in definitions:
                        definition_tokens.extend(definitions[subtoken])
                    else:
                        definition_tokens.append(subtoken)
                    j += 1
                
                if j >= len(tokens):
                    raise ValueError("unclosed word definition")
                
                # Store the definition
                definitions[word_name] = definition_tokens
                i = j + 1  # Skip past the semicolon
                continue
            
            # Check if token is a defined word
            if token in definitions:
                # Process the definition tokens (already expanded)
                def_tokens = definitions[token]
                k = 0
                while k < len(def_tokens):
                    def_token = def_tokens[k].lower()
                    process_token(def_token, stack, definitions)
                    k += 1
                i += 1
                continue
                
            # Process regular token
            process_token(token, stack, definitions)
            i += 1
    
    return stack


def tokenize(line):
    """Convert a line into tokens, handling comments"""
    tokens = []
    current_token = ""
    in_comment = False
    
    for char in line:
        if char == '\\':
            in_comment = True
            continue
        elif in_comment:
            if char == '\n':
                in_comment = False
            continue
            
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
        else:
            current_token += char
    
    if current_token:
        tokens.append(current_token)
        
    return tokens


def process_token(token, stack, definitions):
    """Process a single token"""
    # Check if token is a number
    if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
        stack.append(int(token))
        return
        
    # Arithmetic operations
    if token == '+':
        check_stack_size(stack, 2, "+")
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
        
    elif token == '-':
        check_stack_size(stack, 2, "-")
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
        
    elif token == '*':
        check_stack_size(stack, 2, "*")
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
        
    elif token == '/':
        check_stack_size(stack, 2, "/")
        b = stack.pop()
        a = stack.pop()
        if b == 0:
            raise ZeroDivisionError("divide by zero")
        result = a // b
        if a * b < 0 and a % b != 0:
            result += 1
        stack.append(result)
        
    # Stack manipulation operations
    elif token == 'dup':
        check_stack_size(stack, 1, "DUP")
        stack.append(stack[-1])
        
    elif token == 'drop':
        check_stack_size(stack, 1, "DROP")
        stack.pop()
        
    elif token == 'swap':
        check_stack_size(stack, 2, "SWAP")
        top = stack.pop()
        second = stack.pop()
        stack.append(top)
        stack.append(second)
        
    elif token == 'over':
        check_stack_size(stack, 2, "OVER")
        stack.append(stack[-2])
        
    else:
        # Check if it's a defined word with symbols (like dup-twice)
        if token in definitions:
            def_tokens = definitions[token]
            k = 0
            while k < len(def_tokens):
                def_token = def_tokens[k].lower()
                process_token(def_token, stack, definitions)
                k += 1
        else:
            raise ValueError("undefined operation")


def check_stack_size(stack, required_size, operation):
    """Check if stack has enough elements for an operation"""
    if len(stack) < required_size:
        raise StackUnderflowError("Insufficient number of items in stack")