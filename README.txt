
Read me
 How to use the Application:
1.       The Application upon starting has a default value set to 8 which you can easily change by adjusting the slider horizontally.
2.       The Checkboxes (by default all components are checked out) can be adjusted so as to satisfy which type of characters you may want to exclude out
3.       Please only fill the username if you are planning to save the file to txt or whatever method. So that it saves with your password so that you can retrieve it really quickly.
4.       Pressing generate password will randomly select the characters present from the selected checkboxes and provide an output in the textbox
5.       Pressing save password to clipboard will save the password generated in the textbox to copy to clipboard so you can paste it anywhere u like
6.       Pressing save password to text file will save the password and username to the text file (by default) created.
 



CODING:
Window design:
By using Tkinter, We can design the window using its label feature so using the grid() method we can place  the check boxes in the same row but different column.
So, using the same principle.
I decided to place most of the labels in the 10th column nth row.
So that the labels button is in the same column.
 
While the checkboxes have been placed slightly to the left of the column and the right of the column and then we have an aligned the buttons to the left so that the boxes align parallel to each other.
Then another label indicating to enter username in the text box below if the user wanted to save the password.
The textbox of the height=1 and width =40 then takes the input for username
Then I have inserted a button”Generate password” which calls the “Passwordgen()” so that it generates the passwords and writes the output generated on the text box right below it
Textbox below the button”Generate password” is of the height=1 and width =40 then provides the output from the “Passwordgen()” function.
Then there is one more button called “Copytoclip()” which copies the password to clipboard so that you can paste the info elsewhere.
Lastly the last button called “file_input()” creates or save to a pre-existing file and then that file directory is then used by the file write mode which then appends the username and password to the file.
 
 
 

Passwordgen():
The password generator functions contain components in an array and takes in the input using the checkboxes and scale.
It is triggered using a button “Generate password”

All the characters stored in the list
UPCASE_CHARACTERS contains all the uppercase characters from ‘A’ to ‘Z’
LOCASE_CHARACTERS contains all the lowercase characters from ‘a’ to ‘z’
SYMBOLS contains all the symbol characters from ‘@’ to ‘<’
DIGITS contains all the numbers from ‘1’ to ‘0’

Depending on whether the check boxes is ticked or not the COMBINED_LIST adds the component if the checkboxes are ticked
Temp_pass (Which again filtered similarly to the COMBINED_LIST) initially contains 4 characters randomly selected from the each of the components (To guarantee that if you select all the 4 checkboxes there is 100% chance all the selected checkboxes component at least appears once).
 
Then the next part converts the Temp_pass into an array Temp_pass_list and shuffle it so as to prevent it from having a consistent pattern (So as to not have same repeating component at the beginning).
The last part of the function is to display the randomly shuffled pass list into a string which is then displayed in the text box for password.
 
Copytoclip():
The button “Click here to copy password” calls this function and then clears the clipboard and then appends the password stored in the Textbox to the clipboard.
 
file_input():
The button “Click here to save password to text file” calls this function which then request for saving a txt file to directory and then writes the generated data to the file.(By default the value is set for a .txt file).
This write format is in append mode so that if you have saved the password earlier in this file.
It will write on top of the previous passwords.
 
 
 
 
 



