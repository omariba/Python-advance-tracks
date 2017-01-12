You are given a bunch of files with three different file extension (i.e .txt, .py and.png) all stored in the files folder. Create a program that categorizes all the files based on the extensions. The program then creates different folders based on the extensions and stores all the files with that extension into the folders. Note The folders should be created inside the files directory. Example if one of the file extensions is png it would create a png folder and keep all the files that have a png file extension into that folder. Different file extensions are however handled differently as follows 
* If its a .txt file, then return the first five lines of the file. Notice, it should should still work even if the file has less than five lines and if does not have anything thing in it, it should just return 
    "'name of the file' is empty" -> notice 'name of the file' is the actual name of the file.
* If its a .png file, then return its dimensions of the image.
* If its a .csv file, then return the number of columns of each csv file and any random entry/row of data in the csv file. Handle empty files appropriately in this case as well. 

Requirements for your program.
* It should have test cases
* It should utilize abstraction
