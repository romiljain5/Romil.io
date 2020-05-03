# Romil.io
This is personal website made with flask and python 
hope you like it

# Make sure you have install flask and anaconda 

win+r - cmd -(inside command prompt)
1 - to run this file cd /file-location
	- python pain.py or directly from visual studio code
2 - http://localhost:5000/ in any browser

# mail and password
1) In __init__.py file
    app.config['MAIL_USERNAME'] = 'username'
    app.config['MAIL_PASSWORD'] = 'password'

	----- move this to .db file or in environment variable

   & use email and enable "allow less secure apps" or Use two step verification in gmail

# To login as default user 
   - http://localhost:5000/login go to this link
   - Email: test@gmail.com ; password: testpassword
