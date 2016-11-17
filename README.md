#Library database

Homework from Safeboard internship.  
This task was made using MVC pattern.

Info about `all users` and `all books` is stored in files with the same names and **cannot** be changed using with the program.

Info about `users with books` and `available books` is also stored in files with the same names and **can** be changed using with the program. 
While the program is working info is stored im RAM and when the program exits correctly (using `Quit` option) info is written to the files.

**Program functions:**
 1. Show list of all users  
 2. Show list of all books  
 3. Show list of users with books  
 4. Show list of users with overdue books  
 5. Show list of available books  
 6. Give user a book  
 7. Receive a book from a user    
  
You will need all files from this repository to run the program. You will also need **Python 3**.    
You can launch the program by running `lib_controller.py`
 
 **UPDATE:** Choosing a source was added.  
` All functions for loading and writing data are equal now. 
But each of them can be changed inside (loading from url, another file type etc.)
and interface will not change.
Only DATA_ADDRESSES in lib_controller.py will have to be changed.`