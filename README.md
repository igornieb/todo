# todo
Simple todo app made in Django with Bootsrap frontend and rest api

![image](https://user-images.githubusercontent.com/66256669/217812720-97e96de0-1ce0-40af-9872-0d32d9236517.png)

![image](https://user-images.githubusercontent.com/66256669/217812274-138657d2-81c3-4f9c-a376-69242fbf8c99.png)

# Table of Contents
1. [Live website](#2-live-website)
2. [Api endpoints](#3-api-endpoints)
   1. [/api/login/](#apilogin)
   2. [/api/token/refresh/](#apitokenrefresh)
   3. [/api/active](#apiactive)
   4. [/api/archive](#apiarchive)
   5. [/api/account](#apiaccount)
## 1. Live Website
[SOON](https://web-production-b4d0.up.railway.app/)
## 2. API endpoints
### /api/login/
#### POST
Returns refresh and access token.

Success code: ```200```

Error code: 

```400``` - bad request

``401`` - bad credentials

Example input:

```
{
   "username":"admin",
   "password":"admin"
}
```



Example return:

```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NjIwMjY3NCwiaWF0IjoxNjczNjEwNjc0LCJqdGkiOiJkMjg4MmVmODA5Yzk0NGRkYmUxNTQwOWEwYzhjYTE0NSIsInVzZXJfaWQiOjJ9.yyGHVqFi1EJDEfcL4VyaF7uhfVdHX4xf7jglsGZ3YIA",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjczNjEwOTc0LCJpYXQiOjE2NzM2MTA2NzQsImp0aSI6IjUwZWFlYmYwZTVlYjQ3ZGU4ZTZhYjE3ZGFjMmVkMWYxIiwidXNlcl9pZCI6Mn0.PpngohnD7247WFIHAeKMjbq593YAvqSQRc26QyDHlQQ"
}
```

### /api/token/refresh/
#### POST
Refreshes user token

Success code: ```200```

Error code: 

```400``` - bad request

``401`` - bad credentials

Example input:

```
{
    "refresh": "your_refresh_token"
}
```

Example return:

```
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjczNjExNDk2LCJpYXQiOjE2NzM2MTExMzMsImp0aSI6IjQ0YjZiMzQzMTk5ZTQ4MmZhOGZiOGU3YmYzMGYyN2MzIiwidXNlcl9pZCI6Mn0.Ooi-CjNAG193w2LEaGHkNwYi1AoEpqV2MBze4Z_hFYA",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NjIwMzE5NiwiaWF0IjoxNjczNjExMTk2LCJqdGkiOiI1OWIzM2NmNjc4MzA0MTgzYTgyNjg0YjQzZDc5ZTBmOSIsInVzZXJfaWQiOjJ9.Zrl09OfHO_ipqgIrrmcb5D7L8VT4YZUmPQBMrX-0Y0E"
}
```


### /api/active/
#### GET
   Returns list of active tasks.
   
   Success: ```200```

Error code: 
   
```401``` - unauthorized
   
   Example:
   
          ```[
    {
        "pk": 1,
        "owner": {
            "user": 2,
            "first_name": "",
            "last_name": "",
            "profile_picture": "/media/media/blank.png"
        },
        "title": "test task",
        "task": "test task descrypption",
        "date": "2023-01-13T12:21:05.465054Z",
        "is_done": false
    },
      ...
    ]```
#### POST
Adds new task if user is authenticated.
   
Success code: ```200```
   
Error code: 

```404``` - user not found

```400``` - bad request

```401``` - unauthorized 
   
Example:
```
{
   "title": "test",
   "task": "test task"
}
```

### /api/archive/
#### GET
Returns list of done tasks.
   
Success: ```200```

Error code: 
   
```401``` - unauthorized

```404``` - user not found
   
Example:
   
```[
    {
        "pk": 1,
        "owner": {
            "user": 2,
            "first_name": "",
            "last_name": "",
            "profile_picture": "/media/media/blank.png"
        },
        "title": "test task",
        "task": "test task descrypption",
        "date": "2023-01-13T12:21:05.465054Z",
        "is_done": true
    },
      ...
      ]
 ```
      
### /api/task/{id}/
#### GET
Returns task with given id.
   
Success: ```200```

Error code: 

```404``` - task not found
```401``` - unauthorized
   
Example:
```
{
    "pk": 1,
    "owner": {
        "user": 2,
        "first_name": "",
        "last_name": "",
        "profile_picture": "/media/media/blank.png"
    },
    "title": "test task",
    "task": "test task descrypption",
    "date": "2023-01-13T12:21:05.465054Z",
    "is_done": false
}
```
#### PATCH
Updates task with given id.

Success code: ```200```

Error code:

```404``` - task does not exist

```400``` - bad request

Example:
```
{
    "title": "test task",
    "task": "descryption change",
    "is_done": true
}
```
#### DELETE
Deletes task with given id.

Success code: ```200```

Error code:

```404``` - task does not exist

```401``` - user is not authorized

### /api/account/
#### GET
Returns data of logged-in user.

Success code: ```200```

Error code:

```404``` - user not found

```401``` - user is not authorized

Example:
```
{
    "user": 2,
    "first_name": "",
    "last_name": "",
    "profile_picture": "/media/media/blank.png"
}
```

#### PATCH
Lets user change personal settings.

Success code: ```200```

Error code:

```404``` - user not found

```401``` - user is not authorized

```404``` - bad request

Example:
```
{
    "first_name": "new name",
    "last_name": "new last name",
    "profile_picture": "newprofile.png"
}
```

#### DELETE
Deletes user account.

Success code: ```204```

Error code:

```404``` - user not found

```401``` - user is not authorized

```404``` - bad request
