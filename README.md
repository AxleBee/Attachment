This is a system that automates the attachment process essentially doing away with the need for a physical logbook for keeping track of progress enabling a supervisor and coordinator to monitor student progress easily.

This was a project for the course unit Software Engineering Studio. This project was a good challenge to us with and the project is still far from being completed as we would like to deploy it to the school system.

Installation process
Clone this folder into your computer.
Open with your desired editor preferrably Visual Studio Code.
Run the frontend folder on the terminal by npm start.
To run the server folder: npm run server.js
The frontend folder will open on localhost:3000;
The server folder will open on localhost:8080;
To run both together run:npm run dev


How it works : abridged version

The system is supposed to be installed  by an institution. 

The student can register and login during their attachment period and be able to enter records of their daily activities through the logbook. The supervisor in charge of the student can then view the logbook and provide feedback to the student on a weekly basis. The employer from the organization in which the student is attached can also provide feedback on the students' daily work. This feedback is then only viewable by the Supervisor at the institution. The student can also download the logbook entries in case they are required physically.

TODO/Features

•	Should support login for four types of users:

•	Defining working hours outside which entries will not be accepted

•	Whether missed days due to late entries should result in increased internship days

•	Whether old entries should be editable etc etc.

•	Coordinators

•	The teacher/lecturer in who does supervision of all the interns from a certain class and does an on site assessment of the student interns in their placements
•	Supervisors


•	The person who monitors student progress in his/her place of work

•	Intern

•	The student doing the industrial attachment

•	Supervisor


•	Has to key in list of students on internship

•	Support import from csv file, created by the class rep maybe

•	Should be able to see the progress of all the students in the class doing the internship

•	System has an option for sending mass emails to all the students with links that enable them to signup to the system and changing their loggin details

•	Gets notified when an intern under his supervision updates his/her profile e.g changes his name

•	Should show the coordinator list of students whose student email adresses never received the signup invite links

•	Supervisor


•	Has access to progress data of all the interns under his/her supervision

•	Should allow option for defining whether the intern does work on weekends

•	Decides the number of weeks the intern is supposed to be on internship. The minimum should be at least 8 weeks required by all institutions

•	Fills details on the industry/office/firm the intern works in including:

•	The physical location of the firm

•	The department

•	The room name/number each of the interns under his supervision will work in

•	General description of the workplace and what they do

•	Working hours(start and departure date)

•	Give's weekly report on the progress of the intern

•	Should have a form that enables the supervisor to note down the students progress during the internship

•	Gets notified when an intern under his supervision updates his/her profile e.g changes his name

•	Intern

•	Fills logbook daily

•	Should show the intern his/her progess including:

•	The number of days he's done

•	The number of hours completed in general taking into account the working hours defined by the supervisor

•	The number of days left to complete the 8/12 weeks 

•	Signs up in the system only on invite from the email sent by the coordinator to the school email address.

•	System should support reset of lost passwords

•	Show a calendar showing the number of days completed and days left

•	Enhancements

•	Long emails should be ellipsified/truncated with the full address being displayed on hover

•	Login with google accounts since student emails are managed by gmail

•	Records login attempts

•	Ability to search within your log

•	Add gravatar support

•	Logout link should be in a dropdown with the dropbdown showing the truncated email, the avatar

•	Track user logins, record their ips and times maybe show in an account activity tab

•	Show the Course Name when you hover over the registration number

•	Email sender should keep track of the response from sending each email

•	Copy the styling used in Feedreader newsletters

•	A supervisorr should be shown a different looking profile form from a student

•	Internship start date should not be a one-time permanent change to cater for mistakes. Instead the coordinator should be notified when the intern sets his/her start date and maybe the number of times the start date has been changed to monitor people who are trying to misuse the system

•	Add list of provinces and districts


Show entry preview when mouse hovers over date for some seconds the way stackoverflow shows tag description on hover

Disable button until there's an actual change??

Ability to export the whole logbook as a printable pdf with supervisor remarks and student logs all in one

Ability to view diffs when entries are updated??

Prompt user to save before leaving and show an icon that shows that the entry is unsaved

Capture Ctrl+S keypress

Throw error when no date is specified

Clicking on the tabs should change the title of the tab

Stop running sql queries to fetch logbook entries and profiles for the logged in user. Use instead ActiveQuery methods available through the User model since they are connected through a foreign key


DIRECTORY STRUCTURE


