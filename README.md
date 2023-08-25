# Tarraing - Digital Art Sharing Site.

## Introduction

This is my coding repository dedicated to the Tarraing website. It is a digital art sharing site for people interested in sharing and learning further about digital art. Originally, the idea for Tarraing was for users to be able to share digital art brushes with each other. However due to scoping limits I had to cut that feature. As it was going to be a dificult task hosting these brush files on Cloudinary.

[Visit the Website Here](https://tarraing-c85f2002eff7.herokuapp.com/)

[Visit the Project's GitHub Repository Here](https://github.com/Stuartpkd/Tarraing)

![Image of site on different platforms]()

# Table of Contents

# UX / UI

The UX or User Experience centers on the website's accessibility and its level of user-friendliness, both of which play a critical role in determining the website's overall success.

These can be made up of 5 layers:

The Strategy Plane
The Scope Plane
The Structure Plane
The Skeleton Plane
The Surface Plane

## Strategy 

After thinking about the strategy for my site. I came up with a target audience, which would influence the features included.

### Target users:

1. 18-40 years old.
2. Interested in digital art.
3. People interested in the sharing of digital art.
4. People interested in discovering new digital artists.
5. People interested in collecting digital artwork.

### What the user would look for:

* A clean and visually appealing site, that does not distract from the artwork.
* A simple and clean site (Easy to navigate).
* A quick and easy way to share their artwork.
* A way to interact with other users of the site.
* A way to collect and save their favourite posts.
\
&nbsp;

### User Stories

#### For This Sprint
| id  |  Content | Label |
| ------ | ------ | ------ |
| [1](https://github.com/Stuartpkd/Tarraing/issues/1) | As a registered user, I can upload my artwork so that I can share them with the community. | Needed |
| [2](https://github.com/Stuartpkd/Tarraing/issues/2) | As a registered user, I can delete my uploaded artwork so that I can remove unwanted artwork from the site. | Needed |
| [3](https://github.com/Stuartpkd/Tarraing/issues/3) | As a registered user, I can update the information and files of my uploaded artwork to reflect any changes or improvements. | Needed |
| [4](https://github.com/Stuartpkd/Tarraing/issues/4) | As a registered user, I can like artwork that I find interesting or inspiring to show my appreciation. | Needed |
| [6](https://github.com/Stuartpkd/Tarraing/issues/6) | As a registered user, I can add artwork to my saved artwork on my profile to collect and discover other artists on the site. | Nice to have |
| [8](https://github.com/Stuartpkd/Tarraing/issues/8) | As a site user, I can search for specific artwork using keywords or filters to discover relevant content. | Needed |
| [9](https://github.com/Stuartpkd/Tarraing/issues/9) | As a site user, I can click on an artwork to view its details, including the title, description, artist and upload date so that I can learn further about the content. | Needed |
| [11](https://github.com/Stuartpkd/Tarraing/issues/11) | As a registered user, I have a profile page where I can view and manage my uploaded artwork, as well as see my saved posts, likes and other profile-related information. | Needed |
| [12](https://github.com/Stuartpkd/Tarraing/issues/12) | As a site user, I can register for an account or log in using my credentials to access the full features of the site and interact with other users so that I can benefit from the full features of the site.| Needed |
| [13](https://github.com/Stuartpkd/Tarraing/issues/13) | As an admin, I have special privileges and permissions to moderate user-generated content and manage users so that I can ensure the overall quality and integrity of the site. | Needed |
| [14](https://github.com/Stuartpkd/Tarraing/issues/14) | As a registered user, I can leave comments on artwork to provide feedback or engage in discussions with other users. | Needed |
| [15](https://github.com/Stuartpkd/Tarraing/issues/15) | As a user I can use the random post feature so that I can discover new artists. | Nice to have |
| [16](https://github.com/Stuartpkd/Tarraing/issues/16) | AA a user I can report a comment so that I can help maintain the friendly sense of community on the site. | Nice to have |

\
&nbsp;
#### For Future Sprints
| id  |  Content | Label |
| ------ | ------ | ------ |
| [10](https://github.com/Grawnya/f1-dublin-race-ticket-booking-system/issues/10) | As a user, I can upload and share digital brushes along side my artwork, to give others the opportunity to use the tools I used. | Could Have |

\
&nbsp;
## Scope
During the creation of the project, it came to my attention that the media management system I had settled on was not viable for the files I wanted to upload. A digital brush file contains an alpha matte (An image of a texture used for the brush). As well as some code that is particular to Photoshop and Procreate. Cloudinary would not accept this type of file unless I went through a complicated process of converting the brush files for Cloudinary. With keeping my minimal viable product in mind I decided to axe the brush sharing feature of the site and leave it for a future project or sprint. 

In being just a digital art sharing site, I believe it still fulfilled its inital goal of allowing digital art enthusiasts to interact and share artwork with each other.
\
&nbsp;

### Sprint 1
This sprint covered the needed basic features of the site, as well as the evaluation crtieria.
* A homepage that shows users posts in a paginated order.
* Navbar allowing the user to access the pages of the site.
* A register/login page for new users and returning ones.
* An upload page that allows users to create and share posts.
\
&nbsp;

### Sprint 2
This sprint builds on Sprint 1:
* Add more features to creating a post, allowing users to customise each one they make.
* Add more defensive programming, to make sure users who have not signed up are not able to access all pages.
* Add a "suprise me" feature, allowing users to discover random posts.
\
&nbsp;

### Future Sprints
Elements to add to the site in the future:
* Add the feature of brush sharing and uploading.
* Incorporate email confirmation.
* Allow user to recover their password if they forget.
\
&nbsp;

## Structure

A carefully planned project structure guarantees a more organized approach to project creation, enabling a smoother adherence to sprint steps. As a result, content was segmented into applications to address diverse tasks, while data collected from users was structured into database tables for efficient organization and storage.
\
&nbsp;

### Project Applications
For this project, 1 application was created:
* brush_app – Please forgive the confusing name convention. At the time of cutting the brush uploading from the project, it would have hurt the project to rename some of the naming conventions. So some file names will recall the brush uploading idea. This app was made for users to create posts and share their artwork. Each post can be liked, commented on and saved to a profile to come back to it another time.
\
&nbsp;

### Project Databases
4 databases can be found in the “brush_app” application, which enable the user to create the profile required to upload posts.

> ![Database Tables]()
\
&nbsp;

#### Post Model
The Post model extends beyond the user's basic details and captures additional aspects such as the user-generated title, a user-friendly slug for readable URLs, the author's identification, post content, uploaded artwork image, creation date, and a feature enabling users to save posts to their profile, making it a comprehensive resource for engaging and sharing creative content.

It can be broken down as follows:
* `title` - A title the user makes for their post.
* `slug` - A slug is a user-friendly text version of a resource's title used in URLs to make them readable and descriptive.
* `author` - An identifier for the specific user who created this post.
* `content` - A description of the post that the user creates.
* `artwork_image` - The artwork the user uploads.
* `created_on` - A date that the user created the post on.
* `saved_artworks` - A feature allowing users to save a post to their profile.
\
&nbsp;

#### SavedArtwork
The Save model involves the specific user who wishes to save a post and the corresponding post they intend to save, forming a connection that enables users to retain and access their chosen content easily.

It can be broken down as follows:
* `user` - The user in question who is saving the post.
* `post` - The post that they would like to save.
\
&nbsp;

#### Comment
Within the Comment model, details encompass the related post being commented upon, the commenter's username (represented as their name), an associated email, and the timestamp denoting when the comment was added.

It can be broken down as follows:
* `post` - The post that the user is commenting on.
* `name` - The name of the commenter (This would be their username).
* `email` - An email associated with the user.
* `created_on` - The date the comment was made on.
\
&nbsp;

#### Profile
The Profile model encompasses the profile's owner, an uploaded picture serving as their profile image, a slug connected to the user's profile page, accumulated counts for likes, posts, and downloads, collectively providing an overview of the user's engagement and activity on the platform.

It can be broken down as follows:
* `user` - The user who owns the profile.
* `profile_picture` - An uploaded picture that the user has for their profile pciture.
* `slug` - A slug that relates to the users profile page.
* `num_likes` - A total number of likes the user has amassed.
* `num_posts` - A total number of posts they have made.
* `num_downloads` - A total number of downloads they have made.
\
&nbsp;

## Skeleton
The skeleton provides a broad initial idea that is further refined and built on. 
\
&nbsp;

### Wirefames
I began by crafting a mobile rendition to align with my mobile-first strategy, subsequently crafting versions for medium and large screens. It's crucial to maintain a straightforward layout that doesn't overshadow the artwork posts while ensuring the website's responsiveness across different screen sizes.

Basic wireframes can be found below (Note that these vary slightly from the final website design):

* [Home Page](docs/wireframes/home_page.png "Home Page")
* [Profile](docs/wireframes/home_page.png "Profile")
* [Upload](docs/wireframes/home_page.png "Upload")
* [Signup](docs/wireframes/home_page.png "Signup")
\
&nbsp;

## Surface
The surface plane primarily pertains to aesthetics and the interface, emphasizing the selection of an appropriate color palette, font, and icons that enhance the website's allure without detracting from the artwork's focal point.
\
&nbsp;

### Font
The fonts used were found from google fonts.  They were sourced from [here]() and were used in suitable sections.

### Colours

### Responsive Screens
The website's construction will commence with a focus on a compact 320px-width mobile screen, after which it will be adapted to fulfill the specifications for medium/tablet, large, and extra-large screens, as illustrated in the following table.

| Screen Size   | Breakpoint |
| -----------   | ---------- |
| small/mobile  |    320px   |
| medium/tablet |    768px   |
| large         |   992px    |
| extra-large   |   1400+px  |

\
&nbsp;

# Features

## Existing Features
### Home 
The home page serves as the initial gateway to the website, presenting a curated collection of engaging artwork posts and providing a glimpse into the platform's vibrant content.
\
&nbsp;

### Profile page
The profile page offers users a personalized space to showcase their creative journey, displaying their uploaded artwork, profile picture, and important metrics like total likes, posts, and downloads.
\
&nbsp;

### Upload page
The upload page empowers users to share their artwork with the community, allowing them to submit images and descriptions that capture the essence of their creations.
\
&nbsp;

### Search 
The search bar grants users quick access to discover specific artwork, artists, or topics, enhancing navigation and facilitating exploration across the platform.
\
&nbsp;

### Nav bar
The navigation bar acts as a navigation hub, offering easy and intuitive access to various sections of the website, ensuring smooth user movement and interaction.
\
&nbsp;

### Post detail
The post detail view offers a comprehensive display of individual artwork posts, including enlarged images, descriptions, artist information, and engagement metrics.
\
&nbsp;

### Comments
The comments section provides a dynamic platform for users to express their thoughts, opinions, and appreciation for artworks, fostering interaction and meaningful conversations within the community.
\
&nbsp;

### Saved artwork 
The saved artwork feature allows users to curate a personal collection of their favorite posts, enabling them to revisit and appreciate chosen pieces conveniently from their profile.
\
&nbsp;

### Delete posts
The "Delete Posts" function empowers users to manage their content by removing specific posts from their profile or the platform, ensuring control and tidiness within their artistic showcase.
\
&nbsp;

### Error Pages
404 and 500 error pages have been created as they are the most common errors that users will come across that the messages cannot account for.
\
&nbsp;

This [404 template]() was created to fit the rest of the website’s style.

# Technologies Used

## Languages
* [HTML](https://en.wikipedia.org/wiki/HTML "HTML") - To create the Django templates for the associated views and models in the project applications.
* [CSS](https://en.wikipedia.org/wiki/CSS "CSS") - To style the website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JavaScript") - To create interactive animations for the site.
* [Python]( https://en.wikipedia.org/wiki/Python_(programming_language) "Python") – Is the primary language of Django and used to create all forms, models and views.
\
&nbsp;

## Tools
* [Django](https://www.djangoproject.com/ "Django") – The framework used in this project to incorporate databases with a website.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Crispy Forms") – Formats the models into forms on webpages using the `|crispy` filter and `{% crispy %}` tag.
* [Cloudinary](https://cloudinary.com/ "Cloudinary") - Used to store website's images.
* [Gitpod](https://www.gitpod.io/ "Gitpod") – Used as the development environment.
* [GitHub](https://github.com/ "GitHub") – The project’s Version Control Management System.
* [Heroku](https://www.heroku.com/ "Heroku") – To deploy the webpage.
* [Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq") – For the creation of associated wireframes.
* [DrawSQL](https://drawsql.app/ "DrawSQL") – For the creation of the database diagrams.
* [CSSgradient](https://cssgradient.io/ "CSSgradient") – For the visualisation of gradients for the sites styling.

## Styling
* [Bootstrap](https://getbootstrap.com/ "Bootstrap") – To provide extra styling and out-of-the-box elements e.g. burger menu.
* [Google Fonts](https://fontawesome.com/ "Google Fonts") – For font used in the site.

## Validation
* [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML") – To validate all the HTML files, including the templates from Django itself, due to editing them.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS") – To validate the “style.css” page as well as the specific css page made to create the Formula 1 teams’ logos.
* [JSHint](https://jshint.com/ "JSHint") – To validate the code within the “script.js” file.
* [Python Syntax Checker PEP8](https://www.pythonchecker.com/ "Python Syntax Checker PEP8") – To validate all the Python files, making sure they align with PEP8.
* [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en "Lighthouse") – To check the website’s performance and accessibility, making sure the best practices are used.

## Databases
* [SQLite](https://sqlite.org/index.html "SQLite") - The default database on Django, utilised for unittesting.
* [ElephantSQL](https://www.elephantsql.com/ "ElephantSQL") – The final database used for the deployed project.

# Testing

## Code Validation 
### W3C HTML Validator

\
&nbsp;

## Responsiveness 
The responsiveness of the design was manually checked using the Chrome Developer Tools for various screens.

This included:
* iPhone SE
* Pixel 5
* Samsung Galaxy S8, S20 Ultra
* iPad Air and Mini
* Galaxy Fold
* Nest Hub and Hub Max

I also opted to use the responsiveness option and checked the screens at the following width sizes:
* 350px
* 768px
* 992px
* 1400px

No issues arose, due to the responsive design of the website with rem and % values.
\
&nbsp;

# Deployment

## Create Application

1. If you don't have a Heroku account, start by signing up and logging in.
2. To establish a new application, click the "new" button located at the top right corner of the dashboard, then select "Create new app."
3. Pick a distinct name for the application, indicate your residing region, and proceed by clicking "Create App."

## ElephantSQL
1. Visit elephantsql.com, log in using GitHub, and establish a fresh instance.
2. Once your project instance is set up, copy the URL. You can store this value as an environment variable to match the DATABASES variable in settings.py.
3. Utilize pip3 install dj_database_url==0.5.0 to install the dj-database-url package version 0.5.0. This will format the URL into a Django-compatible format and necessitate an update to the requirements.txt file.

## Cloudinary

1. Set up a Cloudinary account.
2. Upload relevant project images to the "Media Library."
3. Retrieve the Cloudinary API URL from your dashboard.

## Final Repo Preparations
1. Execute necessary project migrations by entering python3 manage.py makemigrations followed by python3 manage.py migrate in the terminal.
2. Integrate a Procfile into the project, including the line web: gunicorn [project_name].wsgi:application.

## Heroku Deploy
1. Return to Heroku and navigate to the Project’s page. Open the "Settings" tab and locate the "Config Vars" section.
2. Within "Config Vars," input the following key-value pairs:
   Key = PORT : Value = 8000
   Key = SECRET_KEY : Value = Your Django Secret Key from settings.py
   Key = DATABASE_URL : Value = ElephantSQL URL (from step 5)
   Key = CLOUDINARY_URL : Value = Cloudinary API URL (from step 9)
3. Proceed to the "Deploy" tab and scroll to the GitHub deployment method.
4. Search and connect to the appropriate repository by selecting the "Connect" button.
5. Continue scrolling to the bottom of the "Deploy" Page and choose your desired deployment method. Opt for "Automatically Deploy" to 
   trigger deployment with each new code push, or manually deploy by selecting the button at the page's bottom.

Your application is now successfully deployed!

# Credits

## For Code Help and Advice
* [Harry Dhillon](https://github.com/Harry-Leepz)

## Helpful Resources

## For Content and Code

