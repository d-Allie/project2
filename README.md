#CS50 Final Project Read Me, Vehicle Information Website, Daniel Allie, 10/17/2024

##Video Demo: https://youtu.be/kRoG8qUGvFQ

###Description: My final project will be a web application that serves to provide
people a place with a feature to look up your car's information by a VIN decoder,
provide knowledge, and be helpful in the purchase of a used car. My webpage
will help people find specific information on their car and provide a
VIN verification of a car before making a second hand purchase. Verifying
the VIN number will protect people from purchasing used cars that could have
been stolen, have inaccurate origins, or changes done to the car that were
not described by the manufacturer. The information provided is helpful in
providing vehicle safety and reporting. I chose to make my application with
Python, Flask, Jijna, HTML, and CSS because Python and it's syntax is
intuitive to read, write, and maintain with Flask.

I chose to use SQLite3 as the database to store users logins with a hashed
password from the Finance problem set (werkzeug.security), because it's
important to keep user's accounts private and secure.

My web application uses CSS to style the pages, including margins and a navbar
to have spacing between sections of HTML displaying a good looking layout. To make
the lettering aestetically pleasing, I chose to have the fonts in the login page
be grey in the Username and Password forms and the links to change to grey when
hovering over them with the mouse. The text in the forms changes to white when
filling in the form. I included a navigation bar with links because I wanted
the users to easily navigate the web application and reach different pages.
While a user is on any of the pages, this provides a good accessibility of
the application.

The application homepage allows users to create an account name and password
for users to access their created accounts. Once a user is logged in,
they will be directed to the main page, the VIN Decoder. The user will
now be able to access the pages of the application and the
@login_required decorator ensures the security of the user's account and webpage
prior to rendering the page. I have made error handling statements to check for
a username that doesn't exist in the database and an incorrect password was
entered.

I wanted to make this application without the use of the CS50 SQL library,
so I utilized the SQL library to connect and query my database. In order to
use SQLite, I needed to learn how to use the SQL library in Python. I found
resources and guides online to import the SQL library, connect to the database,
use the execute function, execute the cursor function, and use the fetch all
function to return the data from the database. I chose to use the login and
page access using the @login_required function with SQLite because of the
effective ability to store user information from the Finance problem set and
improve security of the application. The sessions package from Flask is used
to store the user's session id in the database as well their account name
and password. SQLite is also used for the History page that creates a log of
each VIN Decoder search a user has made, effectively storing the VIN number,
year, and the time it was sent. I wanted to implement this feature because
the user could have a reference for searching multiple cars and access to the
VIN numbers to run the search again, avoiding inputting the long VIN number
repeatedly, and quickly be able to access previous vehicle information.
While using Sqlite3, the default format of data returned is a tuple; however
I felt that dictionaries are easier to use and more applicable to my
database and information because they contain key and value pairs. I
implemented the row function in Python to return values similar to a
dictionary. This was helpful for when I am retrieving and displaying
query results, I could access the values in the same syntax as a
dictionary. I also learned how to use tuple parameters with SQLite in my
database query parameters.

The car VIN decoder is implemented by calling the NHTSA Product Information
Catalog Vehicle Listing (vPIC) Application Programming Interface (API). This
API is provided by the National Highway Traffic Safety Administration as an
operating administration of the United States Department of Transportation.
I chose to use this API because I was inspired by the look up function in
the Finance problem set and wanted to find a way to retrieve data from an
API feature. I chose this feature because it is a common and helpful way
to get specific and large amounts of data. To implement this API, I had to
learn how to retrieve values from the JSON search results that are given
in a key-value pair format. Each valueID and variableID within each pair,
represent a unique ID for that value or variable. Inputting the model year
allows the API to return results for the current model year or older
(pre-1980) model years. The API results were given as a JSON dictionary
with entries and most of the relevant car information was given as a list
of dictionaries in the last dictionary key. I learned to access the list
and the values of each key in the dictionaries by iterating over the
dictionary value of the "results" key. The values were appended to a list
as dictionaries for each row of data containing the values from the JSON
data, selecting the Variable and Value keys as these provided the most
useful and relevant car information.

### My web application will implement a text translator using Azure Cognitive
### Services with AI.

