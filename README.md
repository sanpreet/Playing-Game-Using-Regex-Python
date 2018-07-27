# Playing-Game-Using-Regex-Python
## Playing a simple game using the follwing conditions which is set by me and Using Regular Expression in Python
### Email Validations using the following conditions :hushed:  
       1.) First character must be a alphabet
       2.) Second character must be a letter
       3.) Third is a wild card character
       4.) Fourth Character must be @
       5.) Fifth Character [a-z] comes within Plus so you can add as many charaters as you can but it must be only lower aplhabets.
       6.) It is followed by dot
       7.) Finally you can write only three characters, first one being lower alphaber character followed by two  wild card character
       
       
### Please the see the above conditions in the form of single line using Regex Expression :flashlight:
```
r"(^[a-z][0-9].+@[a-z]+\.[a-z]..$)"
```

### Hope you will play the game by passing emails based on the above condition in the following line of the code
```
emails = ["j1_@example.com", "sany26.com@gmail.com", "s9%@gmail.c@#1","432",'j1_@example1.com','s1(@hmail.fco']
```
Thanks for reading my readme file.
