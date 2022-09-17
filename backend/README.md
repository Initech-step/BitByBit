# BACKEND SETUP

system requiremnents
- Rabbit MQ, installed and running.

Package requirements can be found in the requirements.txt file

1. Create and activate virtual env in the 'backend' folder
2. install requirements using 'pip install -r requirements.txt'
3. In the backend folder where 'manage.py' is located run 'python manage.py makemigrations'
4. Then run 'python manage.py migrate'
5. directly in the backend folder run 'python manage.py runserver'.
8. By now the backend server will be up and running.
9. In the requiremnents we installed celery. 
10. open another terminal and activate the venv We can now run the celery worker from the backend directory. use this command for windows 'celery -A bitbybit worker -l INFO -P gevent'
11. The backend is successfully set up




# API Documentation

- Base url: 'http://127.0.0.1:8000/'
- Note: Every endpoint has an ending slash attached to it.
- 'xxxx' is a placeholder for values that should be replaced by you

#### Authentication API's

#### POST 'user_auth/create_user/'
Request body
```
{
    "first_name": "xxxx",
    "last_name": "xxxx",
    "email": "xxx@gmail.com",
    "department": "xxxx",
    "school": "xxxx",
    "school_short_form": "xxxx",
    "set_year": "xxxx",
    "password": "xxxx"
}
```
Response: status.HTTP_201_CREATED




#### POST 'user_auth/get_token/'
Request body

```
{
    "email": "xxx@gmail.com",
    "password": "xxxx"
}
```

Sample Response
```
{
    "token": "xxxxxxxxxxx"
}
```




#### POST 'creator_apis/group/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'


Request body

```
{
    "group_name":"Uniuyo 3",
    "group_description": "yeah we best",
    "group_department":"Management",
    "group_school":"Uniuyo"
}
```

Sample response
```
{
    "group_name":"xxxxxx",
    "group_description": "xxxxx",
    "group_department":"xxxxx",
    "group_school":"xxxxx"
}
```
status_code: 201



#### GET 'creator_apis/view_my_created_groups/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to display groups you have created so you can choose your current workspace.

Sample response

```
{
  "id": 20,
  "first_name": "xxxx",
  "last_name": "xxxx",
  "department": "xxxx",
  "school": "xxxx",
  "set_year": 2019,
  "groups_created": [
    {
      "id": 8,
      "group_name": "Uniuyo 3",
      "group_description": "yeah we best",
      "group_department": "Management",
      "group_school": "Uniuyo",
      "group_creator": {
        "id": 20,
        "first_name": "xxxx",
        "last_name": "xxxx",
        "department": "xxxx",
        "school": "xxxx",
        "set_year": 2019
      },
      "group_admins": [
        {
          "id": 20,
          "first_name": "xxxx",
          "last_name": "xxxx",
          "department": "xxxx",
          "school": "xxxx",
          "set_year": 2019
        }
      ],
      "subscribers": []
    }
  ]
}

```
main concern is on the 'groups_created' key.
From this point that your group has been created people can subscribe to your group.



#### PUT 'creator_apis/set_managing/${group_id}/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

Since users can create multiple groups the purpose of this endpoint is to set one of the groups you created as the current workspace. Actions you take from here will affect the group that is set as the current workspace.

Sample request: ``` PUT 'creator_apis/set_managing/${group_id}/' ```

Sample response
```
{
  "status": true,
  "currently_managing": 8
}

```
The key 'currently_managing' is the id of the group that is set as the current workspace.




##### The API endpoints from here help you to take managerial actions in your group


#### PUT 'creator_apis/toggle_application/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to decide if other admins can apply to your group as a sub-admin.

Request body
```
{
    "state": "on/off"
}
```
The state value can only have "on" or "off" value at a particular time, any other value will generate an error.

Sample response
```
{
  "status": true,
  "admission_state": true/false
}
```

"on" state value will produce an "admission_state" of true
"off" state value will produce an "admission_state" of false




#### POST 'creator_apis/set_new_sub_admin_email/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to set a custom email message that new subscribers will see immediately they are subscribed to your group.

Request body
```
{
    "message": "xxxxxxxx"
}
```

Response code: HTTP_202_ACCEPTED





#### POST 'creator_apis/set_new_sub_admin_email/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to set a custom email message that newly accepted sub-admins will see immediately their application is accepted.

Request body
```
{
    "message": "xxxxxxxx"
}
```

Response code: HTTP_202_ACCEPTED



#### GET 'creator_apis/view_my_sub_admins/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to view all your sub-admins

Sample response
```
[
  {
    "id": 20,
    "first_name": "xxxx",
    "last_name": "xxxx",
    "department": "xxxx",
    "school": "xxxx",
    "set_year": 2019
  }
]
```



#### POST 'creator_apis/expel_sub_admin/${admin_id}/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to expel a sub-admin. 
Note: expulsion does not work on the group creator

Request: 'creator_apis/expel_sub_admin/${admin_id}/'
Response code: HTTP_202_ACCEPTED




##### The API endpoints from here help you to make posts in your group


#### GET 'creator_apis/view_all_my_posts/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

Request: 'creator_apis/view_all_my_posts/'

Response sample
```
{
  "id": 20,
  "email": "xxx@gmail.com",
  "first_name": "xxxx",
  "last_name": "xxxx",
  "department": "xxxx",
  "school": "xxxx",
  "set_year": 2019,
  "writter": []
}

```
focus is on the 'writter' key. This key will contain all posts made by a particular user.




#### GET 'creator_apis/view_all_pending_posts_for_group/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to display all pending posts. Pending posts are made by sub-admins. Pending posts must be approved by the main admin 
Request: 'creator_apis/view_all_pending_posts_for_group/'

Sample response
```
[
    {
        "letter_title": "xxxxx",
        "body": "xxxx",
        "b3_group": 1,
        "approved": false,
        "written_by": {
            "id":1,
            "first_name": "xxxxx",
            "last_name": "xxxxx",
            "department": "xxxxx",
            "school": "xxxxx",
            "set_year": 2019
        }
    },
    
    {
        "letter_title": "xxxxx",
        "body": "xxxx",
        "b3_group": 1,
        "approved": false,
        "written_by": {
            "id":1,
            "first_name": "xxxxx",
            "last_name": "xxxxx",
            "department": "xxxxx",
            "school": "xxxxx",
            "set_year": 2019
        }
    }
]
```



#### PUT 'creator_apis/approve_post/${post_id}/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'


The purpose of this endpoint is to approve a post made by a subadmin. This sends the post as a newsletter to the subscribers of the group.

Request: 'creator_apis/approve_post/${post_id}/'

Sample response




#### POST 'creator_apis/send_newsletter/${ group_id }/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'


The purpose of this endpoint is to make a post. This endpoint can be accessed by the group creator and group admins. 
Though implementations will be different

- it takes in 'group_id' as a route parameter

Request body sample
```
{
    "letter_title": "xxxxxxx",
    "body": "xxxxx"
}
```

Sample Response
```
{
    "status": true,
    "message": "xxxxx"
}
```

Response status: 201 CREATED



##### The following endpoint from here are for the general wellbeign of the application.

#### POST 'creator_apis/subscribe/'
##### This request doesn't need a token.

The purpose of this endpoint is to subscribe to a group.

Request body
```
{
    "email": "xxx@gmail.com",
    "b3_group": 1
}
```

Response code: HTTP_201_CREATED



#### GET 'creator_apis/view_my_managed_groups/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to show the user all the groups he has administrative powers in.

Response sample
```
{
  "id": 20,
  "first_name": "xxxx",
  "last_name": "xxxx",
  "department": "xxxx",
  "school": "xxxx",
  "set_year": 2019,
  "group_sub_admins": [
    {
      "id": 8,
      "group_name": "Uniuyo 3",
      "group_description": "yeah we best",
      "group_department": "Management",
      "group_school": "Uniuyo",
      "group_creator": {
        "id": 20,
        "first_name": "xxxx",
        "last_name": "xxxx",
        "department": "xxxx",
        "school": "xxxx",
        "set_year": 2019
      },
      "group_admins": [
        {
          "id": 20,
          "first_name": "xxxx",
          "last_name": "xxxx",
          "department": "xxxx",
          "school": "xxxx",
          "set_year": 2019
        }
      ],
      "subscribers": []
    }
  ]
}
```

Focus is on the 'group_sub_admins' key. this lists all the groups the user administrative power in.




#### GET 'creator_apis/view_myself/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to display user profile.

Response sample
```
{
  "id": 20,
  "email": "xxx@gmail.com",
  "first_name": "xxxx",
  "last_name": "xxxx",
  "department": "xxxx",
  "school": "xxxx",
  "set_year": 2019,
  "groups_created": [
    {
      "id": 8,
      "group_name": "Uniuyo 3",
      "group_description": "yeah we best",
      "group_department": "Management",
      "group_school": "Uniuyo",
      "group_creator": {
        "id": 20,
        "first_name": "xxxx",
        "last_name": "xxxx",
        "department": "xxxx",
        "school": "xxxx",
        "set_year": 2019
      },
      "group_admins": [
        {
          "id": 20,
          "first_name": "xxxx",
          "last_name": "xxxx",
          "department": "xxxx",
          "school": "xxxx",
          "set_year": 2019
        }
      ],
      "subscribers": []
    }
  ],
  "group_sub_admins": [
    {
      "id": 8,
      "group_name": "Uniuyo 3",
      "group_description": "yeah we best",
      "group_department": "Management",
      "group_school": "Uniuyo",
      "group_creator": {
        "id": 20,
        "first_name": "xxxx",
        "last_name": "xxxx",
        "department": "xxxx",
        "school": "xxxx",
        "set_year": 2019
      },
      "group_admins": [
        {
          "id": 20,
          "first_name": "xxxx",
          "last_name": "xxxx",
          "department": "xxxx",
          "school": "xxxx",
          "set_year": 2019
        }
      ],
      "subscribers": []
    }
  ],
  "writter": [],
  "user_applying": [],
  "currently_managing": 8
}

```

'groups_created' key lists the groups created by the user.
'group_sub_admins' key lists all the groups the user created and also the groups he is a sub admin of.





#### GET 'creator_apis/view_user/${user_id}/'
##### This request will not require a token.

The purpose of this endpoint is to show the public profile of a user.

Response sample
```
{
  "id": 20,
  "first_name": "xxxx",
  "last_name": "xxxx",
  "department": "xxxx",
  "school": "xxxx",
  "set_year": 2019
}
```



#### GET 'creator_apis/search_group/?axis=${ xx }&search_text=xxxxx'
Note: do not add an ending slash
##### This request will not require a token.

The purpose of this endpoint is to search for groups.

'axis' query parameter can contain any of the following values at a certain time, 'group_name' or 'group_school' or 'group_department'.

Response sample
```
[
  {
    "id": 7,
    "group_name": "First Group",
    "group_description": "good",
    "group_department": "tech",
    "group_school": "University of imagination",
    "is_open_for_application": false,
    "message_for_new_subscriber": "You have subscribed to the first group",
    "message_for_accepted_applicant": "You are accepted to be an admin",
    "group_creator": 18,
    "group_admins": [
      18
    ]
  }
]
```



#### GET 'creator_apis/view_group_detail/${ group_id }/'
##### This request will not require a token.

The purpose of this endpoint is to view the details concerning a particular group.

Response sample
```
{
  "id": 7,
  "group_name": "First Group",
  "group_description": "good",
  "group_department": "tech",
  "group_school": "University of imagination",
  "group_creator": {
    "id": 18,
    "first_name": "Mr. Boma",
    "last_name": "Douglas",
    "department": "Accounting",
    "school": "University of uyo",
    "set_year": 2019
  },
  "group_admins": [
    {
      "id": 18,
      "first_name": "Mr. Boma",
      "last_name": "Douglas",
      "department": "Accounting",
      "school": "University of uyo",
      "set_year": 2019
    }
  ],
  "subscribers": [
    {
      "email": "ietim13@yahoo.com"
    },
    {
      "email": "etimi5319@gmail.com"
    }
  ]
}
```


##### The following API's concern application


#### GET 'creator_apis/view_group_open_for_apply/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to show you the groups that are currently taking in applications for sub-admins.


Response sample
```
[
  {
    "id": 8,
    "group_name": "Uniuyo 3",
    "group_description": "yeah we best",
    "group_department": "Management",
    "group_school": "Uniuyo",
    "is_open_for_application": true,
    "message_for_new_subscriber": "I and the admins welcome you.",
    "message_for_accepted_applicant": "This is a test",
    "group_creator": 20,
    "group_admins": [
      20
    ]
  }
]
```




#### GET 'creator_apis/view_applications/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to view all applications sent to the Group creator





#### POST 'creator_apis/view_applications/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

The purpose of this endpoint is to accepted a certain application

Request body
```
{
    "id": 1
}
```
the 'id' key represents the application id.

Response status: 200 OK




#### POST 'creator_apis/apply_for_admin/'
##### This request will need a token in this pattern 'Token xxxxxxxxx'

This endpoint is used to apply to a group in order to be a sub-admin

Request body
```
{
    "application_message": "xxxxxx",
    "b3_group": 4 
}
```

Request code: HTTP_201_CREATED