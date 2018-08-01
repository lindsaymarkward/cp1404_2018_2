# Read a Markdown file and copy all of the headings to another file
in_file = open("text.md")
out_file = open("headings.md", "a")
# text = in_file.read()
# print(repr(text))

for line in in_file:
    if line.startswith('#'):
        print(line.strip(), file=out_file)
in_file.close()
out_file.close()
