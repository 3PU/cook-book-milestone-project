# VeggiePedia

<br/>

## Table Of Contents

- General Information
- Demo
- Wireframe Mockups
- Technologies
- UI
- UX
- Database
- Accessibility
- Challenges
- Features
- Testing
- Version control
- Deployment
- Credits

<br/>

## General Information

### Code Institute Coding Bootcamp - Data Centric Development Milestone Project

This is my third milestone project for my Coding Bootcamp at Code Institute.

The idea behind VeggiPedia is to create a huge database of vegeterian recipes with the help of its users similar to wikipedia,
but for vegetarian recipes instead.

Switching to a vegetarian diet can be a challenge for many as most recipes for a long time across the world have included meat.

Thus, finding a large collection/resource of different vegetarian recipes can be a tricky endeavour.

This is where a website like VeggiePedia can make a differency by building one of the largest collections of recipes available with the help of its users.

<br/>

## Demo

A live demo of the website can be found [here](https://codei-cook-book.herokuapp.com/).

## Wireframe Mockups

<table>
   <tr>
    <td>Index Page - Large Screen <img src="#" alt="Wireframe Mockup Index Page - Large Screen" style="width: 200px;"/></td>
    <td>Index Page - Small Screen <img src="#" alt="Wireframe Mockup Index Page - Small Screen" style="width: 200px;"/></td>
    <td>View Recipes Page - Large Screen <img src="#" alt="Wireframe Mockup View Recipes Page - Large Screen" style="width: 200px;"/></td>
    <td>View Recipes Page - Small Screen <img src="#" alt="Wireframe Mockup View Recipes Page - Small Screen" style="width: 200px;"/></td>
    <td>Edit/Add Recipe Page - Large Screen <img src="#" alt="Wireframe Mockup Edit/Add Recipes Page - Large Screen" style="width: 200px;"/></td>
    <td>Edit/Add Recipe Page - Small Screen <img src="#" alt="Wireframe Mockup Edit/Add Recipes Page - Small Screen" style="width: 200px;"/></td>
    </tr>
</table>

<br/>

## Technologies

### Languages

- HTML5
- CSS3
- Javascript
- Python3

### Libraries

- Bootstrap CSS 4.3.1
- Bootstrap JS 4.3.1
- FontAwesome 4.7.0
- jQuery 3.4.1
- Dnspython 1.16.0
- Flask 1.1.1
- Flask-PyMongo 2.3.0
- PyMongo 3.10.1

### Tools

- MongoDB

### Hosting

- Github
- Heroku

<br/>

## UI

### Colors, Fonts & Layout

The overall layout of the page is very minimalistic to give the recipes and forms as much attention and real estate as possible.

The goal of the color combination used was to mimic the colors found in many vegetarian dishes in combination with a font that reminds of a
hand written recipe notebook.

### Responsiveness

The website has been built with a mobile-first approach and is highly responsive.

This is primarily achieved by using bootstrap and custom-written css (for more details see testing section).

<br/>

## UX

The overall goal of the website is to provide the visitors with a large database of vegetarian recipes created by users for users,
enabling visitors to upload their own recipes to the database and browse through recipes added by other users.

### User Stories

As a user, I want to be able to add my own recipes to the database. (Create)
As a user, I want to browse a large collection of vegetarian recipes. (Read)
As a user, I want to be able to edit recipes. (Update)
As a user, I want to be able to delete recipes. (Delete)

To be added (TBA):

As a user, I want to create my own profile/login where I can store my own recipe collection. (TBA)
As a user, I want to be able to vote on recipes in the database. (TBA)
As a user, I want to be able to comment on recipes in the database. (TBA)
As a user, I want to be able to quickly share recipes with my friends on social media. (TBA)
As a returning user, I want to be able to edit and delete my own recipes in my personal recipe collection. (TBA)
As a admin user I want to be able to edit and delete any recipe in the database. (TBA)

<br/>

## Accessibility

To increase accessibility of the website, ALT attributes have been added to carousel images.

<br/>

## Challenges



<br/>

## Features

### Existing Features

- Users can add their favorite vegetarian recipes to the database. (Create)
- Users can browse through all recipes contained in the database. (Read)
- Users can edit  recipes in the database. (Update)
- Users can delete recipes in the database. (Delete)

### Features Left To Implement

Going forward I would like to implement the following features:

- Storing user data: Storing user data for each recipe, connecting the recipe to the user that created it.
- Login feature: Only enabling logged in admins or logged in users owning a recipe to edit/delete them.
- Sharing feature: Create social share buttons for users to share a recipe on social media.
- Rating feature: Enabling users to vote on recipes.
- Comment section: Enabling users to comment on shared recipes.
- Validation: Add further backend validation to further add to defensive design.

<br/>

## Testing

### Code Validation

Filename                    | Code      | Validator                             | Outcome/Comments
----------------------------|-----------|---------------------------------------|-----------------
app.py                      | Python3   | http://pep8online.com/                | First test failed with 30+ errors (Identation, white space, long lins). Second test passed with 0 errors.
style.css                   | CSS3      | https://jigsaw.w3.org/css-validator/  | First test passed with 0 errors.
add_recipe.html             | HTML5     | https://validator.w3.org/             | First test failed with 1 error (unclosed div). Second test passed with 0 errors.
base.html                   | HTML5     | https://validator.w3.org/             | First test failed with 1 error (stray script tag). Second test passed with 0 errors.
edit_recipe.html            | HTML5     | https://validator.w3.org/             | First test failed with 1 error (unclosed div). Second test passed with 0 errors.
index.html                  | HTML5     | https://validator.w3.org/             | First test failed with 1 error ("\" used for image src instead of "/"). Second test passed with 0 errors.
view_recipe_category.html   | HTML5     | https://validator.w3.org/             | First test failed with 1 error (stray span tag). Second test passed with 0 errors.

### Responsive design:

The application has been build with a mobile-first approach and throughout the development process, chrome developer tools, multiple PC's and mobile devices
where used to ensure responsivness across all screen resolutions.

The application was also tested by friends and family accross multiple devices and browsers.

For final testing [Responsinator](https://www.responsinator.com/) was used to test the application accross multiple devices.

### Screen Size & Browser Compability

Screen Size         | Size              | Comments
--------------------|----------------------------
X-Small             | <768px            | Pass
Small               | >=768px           | Pass
Medium              | >=992px           | Pass
Large               | >=1200px          | Pass


Browser             | Version           | Comments


### Navigation


### Testing Tools

The responsivness and all code has been checked for errors using a HTML, CSS, JavaScript validation tool and a responsiveness tester:

- [W3C, HTML Validation](https://validator.w3.org/)
- [W3C, CSS Validation](https://jigsaw.w3.org/css-validator/)
- [Responsinator](https://www.responsinator.com/)
- [PEP8 Online](http://pep8online.com/)

<br/>

## Deployment

The project is stored in a GitHub  [repository](https://github.com/3PU/cook-book-milestone-project) and hosted on [Heroku](https://codei-cook-book.herokuapp.com/).

How to deploy to Github:

1. When logged into GitHub, navigate to the repository you want to host/publish. For this project, click [here](https://github.com/3PU/cook-book-milestone-project).
2. Click on 'Settings' to the far right in navigation menu below your repository name.
3. Scroll down to 'GitHub Pages' and select 'master branch' as the **source**.
4. Click **save**.
5. The link to the site hosted on GitHub Pages should appear at the top of the section.

How to clone this repository in order to run the code locally on your machine:

1. When logged into GitHub, navigate to the repository you want to clone. For this project, click [here](https://github.com/3PU/cook-book-milestone-project).
2. Click on the **'Clone or download'** button which should be displayed above and to the right of the repository files.
3. You are presented with a HTTPs address. Copy this address by pressing the button to the right of the address.
4. Open your terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type **'git clone'** and then paste the URL you copied.
7. Press **Enter** and your local clone will be created.

How to deploy to Heroku using GitPod:

1. Created a new application using the Heroku dashboard.
2. Go to settings tab, click on 'reveal config vars' and add config vars such as IP (0.0.0.0), PORT (5000), MongoDB Name, MongoDB URI (URL with DB name and password).
3. Install Heroku via the console using 'npm install -g Heroku'.
4. Log into Heroku via the console using 'heroku login' and follow the on screen instructions to log in.
5. Create a requirements.txt via the console using 'pip3 freeze > requirements.txt'.
6. Create a Procfile via the console using 'echo web: python app.py > Procfile'.
7. Connect GitHub to Heroku via the console using 'heroku git:remote a codei-cook-book'
8. Commit all files in your project via the console using 'git add .' and 'git commit -m "Message"'.
9. Deploy your project to Heroku via the consol using 'git push heroku master'.

<br/>

## Credits

### Content

All of the text content on the website was written by me.

### Media

The images used accross the page were obtained from [Pexels](https://www.pexels.com/) and [Google Images](https://images.google.com/).

The recipes in the database are borrowed from one of my favorite vegetarian recipes website [Cookie & Kate](https://cookieandkate.com/) 

### Acknowledgements

Massive thanks to my Code Institute Mentor Brian M. for his invaluable support and guidance throughout this project.

### Disclaimer

The content of this website is for educational purposes only.