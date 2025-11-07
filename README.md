# push-and-pop-for-linux
push and pop cwd tool
<br />Written for Python3
<br />The function definition in the bashrc function to add text file needs to be added to the end of your ".bashrc" file.<br />I typically place push and pop.py in my current user bin folder.  
<br /><br />I realized 5 years later that I never described what push and pop are...  I used these type functions on old unix systems so much that I was thinking they were self evident or people would look at the code and realize what was going on.  OK, that is a little stupid... Push saves the current work directory to a file and you can then cd anywhere you want to go.  Type pop and you resote back to the previously saved folder.  so once traversing to a folder, save it with push.  Then go somewhere else and push it... your psh list keeps growing... Pop to travel backwards like an undo for your previous CD.
