# FB_Spammer

Instructions for setup
------------

- Clone the project

        git clone https://github.com/iamgroot42/FB_Spammer.git Spammer
        cd Spammer
        
- Install following python packages:

        pip install facebook-sdk
        pip install fb
        pip install facepy

Using the Script
------------

        Go to https://developers.facebook.com/tools/explorer
        Click on 'Get Token', then select 'Get Access Token'
        Check all the boxes (including extended permissions)
        Copy the Access Token generated
        Run 'python FB.py'
        Past the access token
        Write any message to accompany the post
        Press enter

Note:<br />
1.[Will be fixed soon] Write "potato" (without quotes) on a new line after you're done  ( when prompted for a 'message'. )Eg,If you want to write :<br />
  pq<br />
  rs<br />
  in the message,then type the following (when asked for 'Enter Message' while running the script) :<br />
  pq (press enter)<br />
  rs (press enter)<br />
  potato (press enter)<br />
2.Uncomment the call to spam() [around line 60] to spam via comments [not recommended]  
