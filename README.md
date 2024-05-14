# BipVote

This is the project made for ICT4D by group 13

## Installation

It is recommended to create a virtual environment for this project and then you can simply install all necessary packages using

```sh
pip install -r requirements.txt
```

Furthermore we used [ngrok](https://dashboard.ngrok.com/login) to host our local files. To install ngrok follow the installation process shown once signed in to the site.

To make it easy to grade we created the following account

- **Username:** `bipvote@outlook.com`
- **Password:** `UGuDN69DqYCrK3v`

## Running the application

Once everything is installed you will need to first start the flask application

```sh
flask --app main run
```

Following this you must start ngrok in a different terminal (port 5000 is the default port used by flask and must be changed to accordingly)

```sh
ngrok http http://localhost:5000
```

Ngrok will give you a link where your localhost is being forwarded to. Then you just need to point Voxeo to the routes that host the vxml files.

- _urlBeingForwarded_/vxml_yes
- _urlBeingForwarded_/vxml_no
- _urlBeingForwarded_/vxml_organizers
