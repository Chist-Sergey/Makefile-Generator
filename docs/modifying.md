## General

To customize your apps and shortcuts, please edit  
them in the source file.  

Currently, it's fit to open applications for macOS,
but you can modify it to whatever your needs are.

## Syntax

To open an application in macOS,  
the Terminal command will look like:  

    open -a Application  
    open -a "Application Name"  

Let's give it a shourtcut named "a"
The row in genmakefile would look like:

    'a': 'a:\n\t@open -a Application'

Note that the key begins with the name of a shortcut,  
as well as with a pair of special characters.

"\\n" is a 'new line', and "\\t" is a 'tabulation'.
"@" sign removes the feedback when the command is called.

Those are the hardships of this script... for now.  