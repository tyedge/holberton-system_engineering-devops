# holberton-systems_engineering-devops/0x01-shell_permissions

Overview: This project is about using the shell to assign and managing permissions.

0-iam_betty - changes the current user id to betty
1-who_am_i - identifies the current user by printing the effective user id
2-groups - prints out a list of all the groups to which the current user belongs
3-new_owner - makes betty the owner of the current file
4-empty - creates an empty file with the name hello
5-execute - gives the owner of the file hello execution permission
6-multiple_permissions - gives execution permission to both the owner and group owner of the file, and read permission to the other users
7-everybody - gives execution permission to the owner, group owner, and all other users (everyone) of the file hello
8-James_Bond - modifies the permissions of the hello file to give read/write/execute permission to all users other than thefile owner and group owner, who are stripped of all rights 
9-John_Doe - uses the change mode command (chmod) to modify the file permissions of hello, giving the file owner read/write/execute permission, the group owner read/execute permission, and all the other users write/execute permission 
10-mirror_permissions - copy the permissions from to olleh to hello (sudo chmod	 --reference=oellh hello) 
11-directories_permissions - adds execute permission to the subdirectories of the current directory for the owner, group owner, and all other users (DIRECTORIES ONLY, not files)
12-directory_permissions - creates a new directory called dir_holberton with 751 permissions (owner - read/write/execute permission, group owner - read/execute permission, and other users - execute permission)
13-change_group - change the group owner of the file hello to holberton  
14-change_owner_and_group - changes the owner (to betty) and the group owner (to holberton) of the files AND directories of the working directory (pwd)  
15-symbolic_link_permissions - changes the owner of the _hello file to betty and its group owner to holberton
16-if_only - conditionally changes the owner of the hello file to betty ONLY IF the current user is guillaume

Document last edited by Ty Edge on Wednesday, January 30, 2019. 