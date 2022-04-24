import sys
output=""
with open("Output.txt") as f:
    for line in f:
        if not line.isspace():
            output+=line
            
f= open("Output.txt","w")
f.write(Output)
