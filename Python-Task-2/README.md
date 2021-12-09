# User interface - Explained

## User input

For user input we create 3 seperate variables. These variables will store the first, middle and last name of our user. We use `input()` to take in the string and instantly followed by `capitalize()` to ensure that the name is correctly formatted.

</br>

We then create 2 variables for the address and post code. This uses `title()` which capitalises every first letter of every word allowing the address to look clean and correctly formatted. While post code uses `upper()` as that is also the correct formatting for a post code.

</br>

Lastly, we create 3 more variables. National Insurance Number, Course and Education. These 3 variables use the same previous methods. NI Number uses `upper()`, course uses `title()`, while education uses `capitalise()`.

</br>

All the inputs are taken as a string as all the variables contain some text within.

## Display

For display we use a multi-line formatted string (also known as f-string). This allows to easily format variables inside of the string and display all information clealy and concisely. Multi-line string also allows us to easily write exactly how we would like the infromation to be displayed without having to worry about extra formatting (such as `\n` - used for new line breaks).

</br>

NI number has custom formatting through the use of slicing. This allows us to change the input of `AA123456BB` into a more easily to read `AA-123456-B`.
