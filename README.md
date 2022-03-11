# Project Overview

### Project Name

### [directorsUncut](https://kirkemmons.github.io/directors_client/)

### Project Description

#### directorsUncut is an online database where you can keep track of your favorite directors and movies. The application will feature information on each director and details about their films. The site is authenticated, which allows users to access Director and Film information. Users will also be able to add, update and delete directors and films from the list.

### Links

 * [Front-end repo](https://github.com/kirkemmons/directors_client)
 * [Back-end repo](https://github.com/kirkemmons/directors_api)
 * [Deployed Client](https://kirkemmons.github.io/directors_client/)
 * [Deployed API](https://directors-api2.herokuapp.com/)

### Planning

#### I started the project by brainstorming multiple wireframes and an entity relationship diagram. I planned to stick to those wireframes as closely as I could. I chose to build out the backend with Django and the front end with React. My plan was to hit my goals as a user, identified in the user stories.



### Wireframes

![Sign Up Page](https://i.imgur.com/7eJuJRn.png)
![Directors](https://i.imgur.com/59Ie5Gv.png)

### ERD

![ERD](https://i.imgur.com/FIjZo4n.png)

### User Stories

![User Stories](https://i.imgur.com/sVgpxX0.png)

### Dependencies Used

#### Frond End
 * React
 * React Router
 * CSS

#### Back End

 * django
 * djangorestframework
 * python
 * gunicorn
 * whitenoise
 * django-cors-headers
 
### Application Routes

 * '/' : Home Page
 * '/user/signup/' : Sign Up Page
 * '/user/login/' : Login Page
 * '/user/changepw/' : User Change Password Page
 * '/user/signout/' : Sign Out Page
 * '/directors/' : Takes Users to 'View All' Directors page
 * '/directors/:id' : Takes Users to a Director Detail page by id number
 * '/directors/:id/edit' : Users are able to edit Directors (edit form)
 * '/directors/create' : Users are able to create Directors (create form)
 * '/films/create' : Users are able to create Films (create form)
 * '/films/:id/edit' : Users are able to edit Films (edit form)

### MVP

 * Create a RESTful JSON API in Django with user authentication deployed on Heroku
 * Create a front-end user interface written in React and hosted on GH pages

### Post MVP/Stretch Goals

 * Build out resources with functioning CRUD elements
