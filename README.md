# BipVote

This is the project made for ICT4D by group 13

## Installation

It is recommended to create a virtual environment for this project and install all packages using

```sh
pip install -r requirements.txt
```

Furthermore we used [ngrok](https://dashboard.ngrok.com/login) to host our local files. To install it is easy as you need to follow the installation process once signed in

To make it easy to grade we created the following accounts to test the application with ngrok

- **Username:** `bipvote@outlook.com`
- **Password:** `UGuDN69DqYCrK3v`

## Running the application

Once everything is installed you will need to first start the flask application

```sh
flask --app main run
```

Following this you must start ngrok in a different terminal (the default local host used by flask)

```sh
ngrok http http://localhost:5000
```

Ngrok will give you a link where your localhost is being forwarded to. Then you just need to point Voxeo to the routes that host the vxml files.

```plaintext
_urlBeingForwarded_/vxml_yes
_urlBeingForwarded_/vxml_no
_urlBeingForwarded_/vxml_organizers
