<div align="center" class="row">
  <img src="logo_trans.png" width="200"/>
</div>
<h3 align="center">You own your idea!</h3>
<br>

### Problem Statement
We love making new projects and working on new ideas. During the current scenario of online classes what we miss the most is the constant support of our teachers and professors. Imagine having a noble idea which you can't find on the internet but after working for so long on your idea, you  find that someone has already worked on the idea and published his work in a foreign language journal.
Even after you implement your idea, patenting something in India takes 4 to 6 years. Moreover the process is long enough to make it impossible for new ones to complete without any support.
There needs to be a platform where one can share their research and project idea so that others can check if someone is working on idea before they can start. The platform needs to store data in an immutable manner so that if there is any day some issue regarding ownership of the intelectual property records can be checked to ensure who came up the idea first.

### How we plan to solve the problem
We present to you Meridio Chain. Meridio means 'To Share' in greek and as the name suggests we present a platform to share, to share your ideas.
We propose a solution based on Ethereum Blockchain to post project and research ideas by the users. Ideas will be stored in the Ethereum Blockchain network in order to maintain immutability. Data will be stored on the Ethereum blockchain by smart contracts written in Solidity through transactions. User’s unique ethereum address is fetched using Web3js and it is used as an unique key to retrieve complete profile details from MongoDB database. Apart from checking if someone is already working on a project idea, users can also support other projects by sending Ethereum to the author’s ethereum address. Under the Profile section, users can check their profile details and also previous posts made by them.
Using our solution, the users can look if someone is already working on their idea and if not they can post their idea. Users can support other projects or even contact authors of various projects.

### Technologies used

##### Distributed App - [Visit the repository](https://github.com/subhasishgosw5/Meridio-Chain) 

* ReactJS
* Solidity
* Web3JS
* Truffle

##### Server App

* Flask
* MongoDB

### Steps to run the application

1. `cd meridio-chain-backend`
   
2. `pip3 install -r requirements.txt` (only for the first time) then `python3 app.py`

3. Add or Edit the routes and functions in the file run_model.py

### Testing the API

1. Locally, eg: http://localhost:3434/run_model/get_users
2. With LIVE Heroku Server, eg: https://meridio-chain-backend.herokuapp.com/run_model/get_users
3. Test the API with POSTMAN. 

Example for GET USERS : 

* Set the URL TO `https://meridio-chain-backend.herokuapp.com/run_model/get_users` to get all the users.
* Set the URL TO `https://meridio-chain-backend.herokuapp.com/run_model/get_users/<_id>` to get a user for an ID.


Example input for ADD USERS:
* Set the URL TO `https://meridio-chain-backend.herokuapp.com/run_model/add_users`

INPUT:
```json
    {
    "name":"Subhasish Goswami",
    "image":"https://asdasdasd/asdasd.png",
    "email":"asdasdasd@gmail.com",
    "address":"123981239127317237",
    "tagline":"Hey this is me testing"
    }
```

Example input for UPDATE USERS :
* Set the URL TO `https://meridio-chain-backend.herokuapp.com/run_model/update_users` to Update Single Record 

INPUT:
```json
    {   
        "address":"123981239127317237",
        "name": "Aavishkar Mishra"
    }
```
Example input for DELETE USERS :
* Set the URL TO `https://meridio-chain-backend.herokuapp.com/run_model/delete_users` to Delete User Record

INPUT:
```json
    {

        "address":"123981239127317237"
    
    }
```

<hr>

### Authors

##### [Subhasish Goswami](https://github.com/subhasishgosw5)
##### [Aavishkar Mishra](https://github.com/aavishkarmishra)
##### [Rabijit Singh](https://github.com/rabijitsingh)
##### [Adittya Dey](https://github.com/adiXcodr) 
