from sys import argv

# copy file
open(argv[2], 'w').write(open(argv[1]).read())
