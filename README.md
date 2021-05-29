# bakery_bot
Simple chatbot for vk.

This is a bakery shop order app prototype. 
There are 4 categories with several products each. 
You can move back and forth through steps and fill the cart with products of different categories.
After all, you can confirm your order or clear the cart and try again.




Quick start.

$pip install -r requirements.txt

You have to own a group in vk.com to use this bot. 
In your group go to Manage -> Settings -> API usage -> create token/copy existing token -> Long Poll API.
You have to enable Long Poll API and set API version at least 5.131.
At the page Event types enable: Message recieved, Message sent, Message button action, Messaging enabled, Messaging disabled. 
Create a new python file in directory "settings".
Insert tocken and ID into the corresponding fields.

-What is group id? 

-vk.com/public<grop_id>

  
