#Read text from an input document and add a hashtag at the beginning of every line
#It writes out a file named hashTagOutFile_Output as the output
def add_hashtag():
    #This line below, takes an input from the prompt with the path and fileName
    infile_shell = input("Type the path and fileName that you want to hashtag ")
    infile_name = infile_shell.rsplit('\\',1)
    print ("This is the input file: " +(infile_name) [-1])
    outName= ("C:\Git_HL\HeidiProjectsForFun\hashtagOut_"+(infile_name) [-1])
    infile = open(infile_shell,'r')
    content = iter(infile.readline,'')
    outfile = open(outName, 'w')
    #I have to take the file name and make an output name to create a new file
    #outfile = open(infile,'w')
    linenum = 1
    for line in content:
        outfile.write("#"+line)
        linenum=linenum+1
    infile.close()
    outfile.close()
    print ("This is the output file: "+outName)
add_hashtag()




