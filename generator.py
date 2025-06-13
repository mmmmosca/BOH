def esolang_ascii_printer(text):
    # Start with an empty cell for compatibility with your interpreter
    lines = [""]

    # Store each character's ASCII code in a new cell
    for c in text:
        lines.append(str(ord(c)))

    # Output each character using the .N command (where N is the cell index)
    for i in range(1, len(text) + 1):
        lines.append(f".{i}")

    # Optionally, add a halt command if you want
    lines.append("!")

    return "\n".join(lines)

# Example usage:
input_text = input("Enter the text to generate esolang code for: ")
print(esolang_ascii_printer(input_text))