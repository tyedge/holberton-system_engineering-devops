# holberton-systems_engineering-devops/0x02-shell_redirections

Overview: This project is about using the shell redirections and filters.

0-hello_world - this script uses the echo command to print “Hello, World” followed by a new line key to the display (Note: the echo command ends with a newline key by default)
1-confused_smiley - this script uses the echo command to print a confused smiley face (Note: the key here is to make sure that the escape key (\) is used properly to prevent the quotation marks from being interpreted as special characters)
2-hellofile - this script uses the cat command to display the /etc/passwd file in the standard output
3-twofiles - this script uses the cat command to display the /etc/passwd and /etc/hosts files in the standard output 
4-lastlines - this script uses the cat command and the tail filter (with -n option) to display the last 10 lines of the /etc/passwd file in the standard output
5-firstlines - this script uses the cat command and the head filter to display the first 10 lines of the /etc/passwd file in the standard output
6-third_line - this script uses the cat, tail (+N), and H (-n) commands to display only the third line of the iacta file
7-file - this script creates a new file with a filename that contains quotations and backslashed that have to be preserved (from interpretation) and adds the text “Holberton School” to that file using the echo command
8-cwd_state - this script writes the results of the command ls -la into a file called ls_cwd_content, which it either creates (if it doesn’t already exist) or overwrites (if the file already exists) 
9-duplicate_last_line - this script echoes (with option -e) the result of applying the tail filter (with option -1) to the iata file, and appends it to the iata file versus printing it to the standard output 
10-no_more_js - this script uses the find command with the name, type, -print0 options piped to the xargs utility (which reads space, tab, newline and end-of-file delimited strings from the results of the find command and then executes the rm utility to remove the specified files). Specifically, this script traverses the current directory and its subdirectories recursively, finds any regular files (not directories) with the .js file extension (achieved by using \ to preserve the “*” character from interpretation (like so \*.js)) and deletes them.
11-directories - this script uses the find command to search for and tally the number of directories in the current directory and all of its subdirectories - excluding the current and parent directories. It outputs the total count returned from the search.
12-newest_files - this script pipes the results of the ls -t search into the head filter to produce a list of the 10 newest files in the current directory
13-unique - this script uses the sort command with the unique filter (with the -u option) to conduct a sort on a list and display only lines within that list that appear at most one time
14-findthatword - this script uses the grep filter with the -w option to find and display any lines containing the word “root” in the /etc/passwd file
15-countthatword - this script uses the grep filter with the -c option to tally and display a total count of the lines containing the word “bin” in the /etc/passwd file
16-whatsnext - this script uses the -A 3 context switch on the grep filter to find matches to the pattern “root” and displays 3 trailing lines of context. Additionally, the -e option is activated in order to protect files that being with “-“
17-hidethisword - this script uses the grep filter with the -v (reverse results) option to yield a list of lines in the /etc/passwd file that do not contain the pattern “bin”
18-letteronly - this script uses the grep filter with the -i and -e options as well as POSIX syntax in order to output only the lines in the /etc/ssh/sshd_config file that begin with a letter
19-AZ - this script uses the tr filter to transform all the letters “A” and “c” from the input to “Z and “e”
20-hiago - this script uses the tr filter with the -d option to delete all the letters “C” and “c” from the input
21-reverse - this script uses the rev command to output the reverse of the given input 
22-users_and_homes - this script uses the sort command and pipes the result to the cut filter with options -d : -f 1, 6 (to specifically return fields 1 and 6 only, which are delimited by :) and pull just the user and home directories from the /etc/passwd file.

Document last edited by Ty Edge on Saturday, February 2, 2019.