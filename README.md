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

- _urlNgrokForwardedLocalHostTo_/vxml_yes
- _urlNgrokForwardedLocalHostTo_/vxml_no
- _urlNgrokForwardedLocalHostTo_/vxml_organizers

## Running the frontend

First install yarn on your pc, see tutorial (https://classic.yarnpkg.com/lang/en/docs/install/#debian-stable).
After that install the packages

```sh
yarn install
```

To add a reference to BipVote API add in the environment or change in the variable in the .env.development file.

```sh
VITE__API__URL=REFERENCE__API
```

After that with you can start the run the frontend with

```sh
yarn dev
```
