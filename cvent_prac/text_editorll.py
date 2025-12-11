"""
You are building a simple text editor with three commands:

"type X" → append character X to the end of the string

"undo" → undo the last type operation

"redo" → redo the last undone type operation

Rules:

undo removes the last typed character and stores it in a stack so it can be re-added if redo is called.

redo only works if there is something to redo.

Any new "type X" command clears the redo history (just like real editors).

Return the final text string.

"""

def text_editor2(commands):
    text = ""
    redo_stack = []

    for cmd in commands:
        # your logic here
        if cmd.startswith("type"):
            command, char = cmd.split(" ")
            text += char
            redo_stack = []
        elif cmd == "undo":
            redo_stack.append(text[-1])
            text = text[:-1]
        elif cmd == "redo" and redo_stack:
            text += redo_stack.pop()


    return text
