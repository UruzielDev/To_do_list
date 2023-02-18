# To_do_list
The app allows users to create a to-do list, add tasks to the list, mark tasks as complete, edit tasks, delete tasks, and save the list to a file.

The app uses the Tkinter library to create a graphical user interface. The main window of the app has an entry field, where users can enter tasks they want to add to the list, and a button to add the task to the list. The window also has a listbox that displays all the tasks in the list. Users can select a task from the list and mark it as complete or delete it. They can also edit the task by changing its name or category. The app also allows users to filter the list by category or show all the tasks in the list.

When the user closes the app, it automatically saves the to-do list to a file called todo_list.pkl. When the user opens the app again, it loads the list from the file and displays it in the listbox.

This app is a good example of how to use the Tkinter library to create a graphical user interface and how to use the pickle library to save and load data to and from a file. It also demonstrates how to use object-oriented programming to create classes for the to-do list and its items

More to do in the future : 
1.Implement an Update button for the edit.
2.Refine the Filter action
3.Toggle the Completed button to check/uncheck
