<img alt="Instahunter" src="https://raw.githubusercontent.com/Araekiel/instahunter/gh-pages/public/images/logo.png" height="100">

# Instahunter
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)]() [![GitHub Release](https://img.shields.io/badge/release-v1.6.1-blue)]() [![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

[Instahunter](https://araekiel.github.io/instahunter) is an Open-Source CLI app, that can fetch posts and user data from Instagram's frontend API in JSON or text format. I built it while fiddling around with the Instagram API for my other project, [Orion](https://github.com/Araekiel/orion).
<br/>
<br/>
Commands Insthaunter currently supports:
- **getposts**: Fetch latest or top public posts with a Hashtag
- **getuser**: Fetch public user data with a Username
- **getuserposts**: Fetch recent public posts of a user with a Username
- **search**: Search for users on Instagram

<br/>
<img alt="Screenshot" src="https://raw.githubusercontent.com/Araekiel/instahunter/gh-pages/public/images/screenshot.jpg">

## Prerequisites

- Git is need to clone the repository on your machine.
- pip is needed to install packages.
- Python is needed to run the app.

### Ubuntu

Install git, python and pip on your machine running Ubuntu:

```
$ sudo apt-get install git-core
$ sudo apt install python3.7
$ sudo apt install python3-pip
```

### Windows

Use the official links for downloading on Windows:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)

> pip comes with the installation of Python on Windows


To run the app from source - [Git](https://git-scm.com/) is needed to clone the repository on your machine. [Python](https://www.python.org/) and [Click](https://click.palletsprojects.com/en/7.x/) are required to run the app from the source.

## Installation & Configuration

Clone the repo and cd into the directory: 

```
$ git clone https://github.com/Araekiel/instahunter.git
$ cd instahunter
```

Instahunter was built with click package and needs it to run. Install click:

Windows:
```
pip install click
```

Ubuntu: 
```
$ pip3 install click
```

## Usage

Running from the source:

```
$ python instahunter.py
```

To get help use **--help**:

```
instahunter --help
```

```
instahunter getposts --help
```

### Getting Posts

Use the command **getposts** to get posts.

Options:

- `-tag`: tag you want to fetch posts with 
- `--post-type` : latest(default) - fetch latest posts, top - fetch top posts

```
instahuter getposts -tag *hashtag* --post-type *latest or top*
```

### Getting User Data

Use the command **getuser** to get user data.

Options:

- `-username`: username you want to fetch user data with

```
instahunter getuser -username *username*
```

### Getting User Posts

Use the command **getuserposts** and option **-username** to get posts.

```
instahunter getuserposts -username *username*
```

### Searching for Users

Use the command **search** and option **-query** to search for users.

```
instahunter search -query *query*
```

> All the above commands will display data in the terminal itself.

### Creating a file with the data

To create a file with the data retrieved use **-create-file** and **--file-type** options along with any option.

Options:

- `-create-file`: true - will create a file with the data, false(default) - won't create a file
- `--file-type` : json - will create a json file, text(default) - will create a text file

```
instahunter getposts -tag *hashtag* -create-file *true or false* --file-type *json or text*
```

## Release & Changelog

Latest Release: v1.6.1

Changelog: 
- Command **gettopposts** removed
- Command **getposts** has ***-post-type*** option now to fetch latest or top posts
- Option ***-via*** removed from Command **getuser** (Deprecated endpoint)
- Some data removed from Command **search** 
- Minor bug fix

> Currently only the Windows executable is available in the Release section

## Download

Click here: [Instahunter](https://araekiel.github.io/instahunter/public/bin/instahunter.exe)

## Libraries

- [Click](https://click.palletsprojects.com/en/7.x/) was used to make the CLI
- [Pyinstaller](https://www.pyinstaller.org/) was used to build the executable
- A customized version of [termynal](https://github.com/ines/termynal) by [Ines Montani](https://github.com/ines) was used on the [gh-pages website](https://araekiel.github.io/instahunter) to display the output 
 
## Contribution

Fork the repository and open a pull request to contribute.
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- **Araekiel** - [Github](https://github.com/Araekiel)

## License

[MIT](https://choosealicense.com/licenses/mit/)
