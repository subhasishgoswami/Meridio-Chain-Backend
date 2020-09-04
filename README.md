<h1 align="center" >MERIDIO CHAIN BACKEND</h1>
<h3 align="center">An API for handling GET/POST requests </h3>

## Technologies used
* Python
* MongoDB
* FLASK

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

## Author

## -[Aavishkar Mishra](https://github.com/aavishkarmishra)
[<img src="https://image.flaticon.com/icons/svg/185/185964.svg" width="35" padding="10">](https://www.linkedin.com/in/aavishkarmishra/)
[<img src="https://image.flaticon.com/icons/svg/185/185981.svg" width="35" padding="10">](https://www.facebook.com/aavishkarmishra)
[<img src="https://image.flaticon.com/icons/svg/185/185985.svg" width="35" padding="10">](https://www.instagram.com/aavishkar_mishra/)
