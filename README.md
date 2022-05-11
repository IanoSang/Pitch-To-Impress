# Pitch-To-Impress
<p>In life, you only have 60 seconds to impress someone. 1 minute can make or break you. How do we make sure that you use your 1 minute to actually say something meaningful?</p>
<p>This is an application that allows users to use that one minute wisely. You will be able submit your one minute pitches and other users will vote on them and leave comments to give their feedback on them.</p>


### Technologies Used

- Python
- Flask
- Sqlalchemy

### Prerequisites
- git
- Package manager - pip
- Environment manager - virtual env

### Setup Instructions and Installation
- In your preferred location in your file system, create a virtual environment and activate it
- Launch your terminal and paste the following command: `git clone https://github.com/BrianMwevi/news-flash.git`
- Change directory to news-flash `cd news-flash`
- Open the project with your preferred IDE and run the following command in the terminal: `pip install -r requirements.txt`
- Go to [NewsApi](https://newsapi.org/) and generate an API Key for your application
- create a file named `start.py` in the root of your application and change it's permissions: `chmod a+x start.py`
- Create two variables in the start.py file:
    >>> `export NEWS_API_KEY='your apikey'` <br>
    >>> `export SECRET_KEY='your secret key'`
- Run the application by typing the following in the terminal: `./start.py`

### User Stories
<ul>
  <li>The user is able to see the pitches other people have posted.</li>
  <li>The user is also able to vote on the pitch they liked and give it a downvote or upvote.</li>
  <li>The user is able to  to be signed in for me to leave a comment</li>
  <li>The user is to receive a welcoming email once I sign up.</li>
  <li>The user is to view the pitches I have created in my profile page.</li>
  <li>The user is to to comment on the different pitches and leave feedback.</li>
  <li>The user is to to view the different categories.</li>
 
 </ul>

### Known Bugs

No known bugs.


### License

_MIT Licence_
Copyright (c) 2022 **Ian Sang**<br>
Email: ianosang18@gmail.com<br>
[Read More](https://github.com/IanoSang/Pitch-To-Impress/blob/main/LICENSE)


[Go Back To Top](#Pitch-To-Impress-news)
