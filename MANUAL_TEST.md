# Manual Tests

[Go Back to README.md](https://github.com/Stuartpkd/Tarraing)

## Epic 1: Core Website Functionality (Needed features)

[1](https://github.com/Stuartpkd/Tarraing/issues/1) - As a registered user, I can upload my artwork so that I can share them with the community.

![Upload page](docs/manual_test/User_story_upload_1.png)
\
&nbsp;
![File type error](docs/manual_test/User_story_upload_2.png)
\
&nbsp;
![File size error](docs/manual_test/User_story_upload_3.png)
\
&nbsp;
![Successful Post](docs/manual_test/User_story_upload_4.png)
\
&nbsp;


This user story is met on the upload page, which can be navigated to through the nav. The upload page details the dile types and sizes that it accepts and will show a warning box if the user tries to break them. The user is also warned on the page which file types and sizes are accepted. Upon a successful upload, the user is brought to the post detail of their post.
\
&nbsp;

[2](https://github.com/Stuartpkd/Tarraing/issues/2) - As a registered user, I can delete my uploaded artwork so that I can remove unwanted artwork from the site.

![Profile page](docs/manual_test/User_story_delete_1.png)
\
&nbsp;

![Delete edit page](docs/manual_test/User_story_delete_2.png)
\
&nbsp;

![Profile page](docs/manual_test/User_story_delete_3.png)
\
&nbsp;

This user story is met on the edit post section of the site. This can be navigated to by going to your user profile page and pressing edit on the post container. They may then press delete on the post which will remove it from the site. There is also a warning displayed in case the user changes their mind. If they choose to delete it, they are redirected to their profile page.
\
&nbsp;

[3](https://github.com/Stuartpkd/Tarraing/issues/3) - As a registered user, I can update the information and files of my uploaded artwork to reflect any changes or improvements.

![Profile page](docs/manual_test/User_story_edit_1.png)
\
&nbsp;

![Edit page](docs/manual_test/User_story_edit_2.png)
\
&nbsp;

![Post detail page](docs/manual_test/User_story_edit_3.png)
\
&nbsp;

This user story is met on the edit post section of the site. This can be navigated to by going to your user profile page and pressing edit on the post container. The user is then able to update the title, content and image of their post. Upon submitting these changes the user is brought to the post detail page with their changes made. 
\
&nbsp;

[4](https://github.com/Stuartpkd/Tarraing/issues/4) - As a registered user, I can like artwork that I find interesting or inspiring to show my appreciation.

![Post link](docs/manual_test/User_story_like_1.png)
\
&nbsp;

![Post not liked](docs/manual_test/User_story_like_1.png)
\
&nbsp;

![Post unliked](docs/manual_test/User_story_like_1.png)
\
&nbsp;

This user story is met by navigating to a post detail page of a post that a user likes. They can then click on the like button which then changes its icon to show that it has been liked by the user. The user is also able to unlike the post if they wish to do so.
\
&nbsp;

[8](https://github.com/Stuartpkd/Tarraing/issues/8) - As a site user, I can search for specific artwork using keywords or filters to discover relevant content.

![Home page nav](docs/manual_test/User_story_search_1.png)
\
&nbsp;

![Search bar](docs/manual_test/User_story_search_2.png)
\
&nbsp;

![Search results](docs/manual_test/User_story_search_3.png)
\
&nbsp;

This user story is met by navigating to the search menu at the top of the screen in the nav bar. The search query is based on the title of posts and will look for keywords that the user enters. The user is also warned when there were no search results for their query. The user is also able to use this feature anywhere in the site, once authenticated.
\
&nbsp;

[9](https://github.com/Stuartpkd/Tarraing/issues/9) - As a site user, I can click on an artwork to view its details, including the title, description, artist and upload date so that I can learn further about the content.

![Home page](docs/manual_test/User_story_postdetail_1.png)
\
&nbsp;

![Post detail](docs/manual_test/User_story_postdetail_2.png)
\
&nbsp;

This user story is met by clicking on any post link to be brought to its post detail page. It will contain the users name, the upload date, comment section, likes, a download button and a description. The user may also return to the home page by clicking on the back button found at the top of the post detail page.
\
&nbsp;

[11](https://github.com/Stuartpkd/Tarraing/issues/11) - As a registered user, I have a profile page where I can view and manage my uploaded artwork, as well as see my saved posts, likes and other profile-related information.

![Profile page](docs/manual_test/User_story_profile_1.png)
\
&nbsp;

This user story is met by navigating to the profile page from the nav at the top of the screen. It will contain their uploads and their saved artworks, with a switch to toggle between the two. It also contains a count of their likes and uploads as well as a section for them to upload a profile picture. A user can also click on another users name in a post detail to view their uploads.
\
&nbsp;

[12](https://github.com/Stuartpkd/Tarraing/issues/12) - As a site user, I can register for an account or log in using my credentials to access the full features of the site and interact with other users so that I can benefit from the full features of the site.

![Home page](docs/manual_test/User_story_register_1.png)
\
&nbsp;

![Sign up](docs/manual_test/User_story_register_2.png)
\
&nbsp;

![Sign in](docs/manual_test/User_story_register_3.png)
\
&nbsp;

![Home page](docs/manual_test/User_story_register_4.png)
\
&nbsp;

This user story is met by checking if the user is authenticated apon arriving to the home page. If the user is not signed in the hero section will have a button asking them to sign up. The user is able to view the posts, however will be asked to sign up / in upon trying to visit the post details or use the search function. Parts of the nav are also not rendered if the user is not signed in.
\
&nbsp;

[13](https://github.com/Stuartpkd/Tarraing/issues/13) - As an admin, I have special privileges and permissions to moderate user-generated content and manage users so that I can ensure the overall quality and integrity of the site.

![Admin page](docs/manual_test/User_story_admin_1.png)
\
&nbsp;

This user story is met by creating a super user through the terminal. This account had special privileges to access the admin panel to manage and moderate site content. From here the admin or super user is capable of changing or removing anything from the site. This could be comments, posts, images, users etc.
\
&nbsp;

[14](https://github.com/Stuartpkd/Tarraing/issues/14) - As a registered user, I can leave comments on artwork to provide feedback or engage in discussions with other users.

![Admin page](docs/manual_test/User_story_comment_1.png)
\
&nbsp;

![Admin page](docs/manual_test/User_story_comment_2.png)
\
&nbsp;

![Admin page](docs/manual_test/User_story_comment_3.png)
\
&nbsp;

![Admin page](docs/manual_test/User_story_comment_4.png)
\
&nbsp;

This user story is met by navigating to a post detail and scrolling below to see the comment section. The user is able to make a comment which then appears below the post. The comment shows the user who made it and the date it was made on. As well as the body of the comment they created. The user can also edit and delete their comment should they wish. They are also warned below the comment on how many characters the comment can take.
\
&nbsp;

[14](https://github.com/Stuartpkd/Tarraing/issues/14) - As a registered user, I can leave comments on artwork to provide feedback or engage in discussions with other users.

![Admin page](docs/manual_test/User_story_comment_4.png)
\
&nbsp;

This user story is met by navigating to a post detail and scrolling below to see the comment section. The user is able to make a comment which then appears below the post. The comment shows the user who made it and the date it was made on. As well as the body of the comment they created. The user can also edit and delete their comment should they wish. They are also warned below the comment on how many characters the comment can take.
\
&nbsp;

## Epic 2: Secondary features (Nice to haves)

[6](https://github.com/Stuartpkd/Tarraing/issues/6) - As a registered user, I can add artwork to my saved artwork on my profile to collect and discover other artists on the site.

![Admin page](docs/manual_test/User_story_save_1.png)
\
&nbsp;

![Admin page](docs/manual_test/User_story_save_2.png)
\
&nbsp;

![Admin page](docs/manual_test/User_story_save_3.png)
\
&nbsp;

This user story was met by navigating to a post detail of a post and then selecting the save icon underneith the artwork. The user can then navigate to their profile page to view their saved artworks with the switch provided. The page opens with their uploads by default when going to the profile page. The user can remove the post from their saved posts by navigating to the post detail and clicking on the save button again.
\
&nbsp;

[6](https://github.com/Stuartpkd/Tarraing/issues/6) - As a registered user, I can add artwork to my saved artwork on my profile to collect and discover other artists on the site.


![Admin page](docs/manual_test/User_story_save_1.png)
\
&nbsp;

This user story was met by navigating to a post detail of a post and then selecting the save icon underneith the artwork. The user can then navigate to their profile page to view their saved artworks with the switch provided. The page opens with their uploads by default when going to the profile page.
\
&nbsp;

[15](https://github.com/Stuartpkd/Tarraing/issues/15) - As a user I can use the random post feature so that I can discover new artists.

![Admin page](docs/manual_test/User_story_random_1.png)
\
&nbsp;

![Admin page](docs/manual_test/User_story_random_2.png)
\
&nbsp;

This user story was met by having a button in the hero section that will bring a user to a random post so that they can discover a new artist. 
\
&nbsp;

[16](https://github.com/Stuartpkd/Tarraing/issues/16) - As a user I can report a comment so that I can help maintain the friendly sense of community on the site.

![Admin page](docs/manual_test/User_story_report_1.png)
\

&nbsp;
![Admin page](docs/manual_test/User_story_report_2.png)
\

&nbsp;
![Admin page](docs/manual_test/User_story_report_3.png)
\
&nbsp;

This user story is met by having the report comment button below all comments made. This will bring the user to a report page. Here they can provide a reason for the comment being offensive. This will then notify the admin by marking the comment with a tick in the admin panel as well as the reason as to why it was reported. They are then able to take action.
\
&nbsp;

