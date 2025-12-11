"""

You're building a very small text editor. You’re given a list of commands. Each command is either:

"type X" → append character X to the end of the string

"undo" → delete the last character, if any

Return the final string after processing all commands.

Example:
Commands: ["type a", "type b", "undo", "type c"] → "ac"

Take a moment.
You can think out loud.”

"""

def text_editor(commands):
    result = ""

    for cmd in commands:
        if cmd.startswith("type"):
            type_char, char = cmd.split(" ")
            result += char
        else:
            result = result[:-1]


    return result
