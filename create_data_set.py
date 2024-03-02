# The initial script was written by Github Copilot Chat with the following prompt:
# "Read in all the files in this directory and save the contents of them into a single file."
import os
import re

# Output file to save the contents
output_file = "bdunagan.com.txt"

# Open the output file in write mode
with open(output_file, "w") as f:
    # Iterate over all files in the folder, sorted by name
    for filename in sorted(os.listdir(".")):
        # Only use markdown files
        if filename.endswith(".md") or filename.endswith(".markdown"):
            # Open the file in read mode
            with open(filename, "r") as file:
                # Read the contents of the file
                contents = file.read()

                # Remove front matter
                contents = contents.replace("--- \n", "---\n")
                sections = contents.split("---\n")
                if len(sections) > 2:
                    contents = sections[2]

                # Remove Liquid code blocks
                contents = re.sub(
                    r"{% highlight .*? %}(.*?){% endhighlight %}",
                    "",
                    contents,
                    flags=re.DOTALL,
                )

                # Only keep writing, not code or tags
                lines_to_keep = []
                for line in contents.split("\n"):
                    # Do not include lines that start with HTML or Liquid tag
                    if not line.startswith("<") and not line.startswith("{%"):
                        # Strip out inline HTML
                        line = re.sub(r"<.*?>", "", line)
                        # Strip out inline links
                        line = re.sub(r"\[.*?\)", "", line)
                        # Save the modified line
                        lines_to_keep.append(line)
                contents = "\n".join(lines_to_keep)

                # Remove other incorrect lines.
                contents = contents.replace("\n\n\n\n", "\n\n")
                contents = contents.replace("\n\n\n", "\n\n")

                # Write the contents to the output file
                f.write(contents)
