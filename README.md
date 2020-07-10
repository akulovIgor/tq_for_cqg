Gets a list of pairs from a config file (sample config file 1 is provided below), and replace value1 by value2 for all matches in given text file (sample text file 1 is provided below). All values in config file are unique. Names of both files are passed as command line parameters. Outputs the changed text file in the line order from the end to the beginning.

Sample config file 1

a=z

b=y

c=x

Sample text file 1

djf#aemfaofna%

b#sjf_ansvo!

cnhjrfyjvth3nxr

The script is written in Python 3.8.3.

Script run example:

python main.py ./data/config.txt ./data/text.txt