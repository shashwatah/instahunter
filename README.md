# Instahunter
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)]() [![GitHub Release](https://img.shields.io/badge/release-v2.0-blue)]()

A CLI OSINT app that can fetch data from Instagram's Web API without the need of logging in or an API token.
<br/>

Data that can be fetched:
- ***Public Posts***: ***Top*** or ***Latest*** posts under a hashtag.
- ***User Data***: Public data of a user's profile.
- ***User Posts***: Posts by a user whose profile is public.
- ***Search***: Users from instagram search.

<br/>

<img alt="Instahunter GIF" src="https://raw.githubusercontent.com/araekiel/instahunter/main/assets/instahunter.gif">

## Notes

- Instagram has been blocking/rate-limiting IPs that make extensive requests to its web api. For more information on this check out this [forum](https://programmierfrage.com/items/instagram-public-api-a-1-is-banned-any-alternative).
- If after a while of use, you start encountering continuous errors, it's probably because you've either been rate-limited or entirely blocked. There are a couple of work-arounds for this issue:
  - Switch to a different network (You'll have to do this everytime you get blocked).
  - A more permanent fix would be to alter the code to use proxies.
- The JSON file is created at the destination where ***main.py*** or the executable exists.

## Running from Source

### Prerequisites

- Git is need to clone the repository on your machine.
- pip is needed to install the packages.
- Python is needed to run the app.

#### Ubuntu

Run the following commands in a terminal:

```bash
$ sudo apt-get install git-core
$ sudo apt install python3.9
$ sudo apt install python3-pip
```

#### Windows

Use the official links for downloading on Windows:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)

> pip is installed along with python on windows.

Run the following commands to confirm if the installation was successful:

```bash
$ git --version
$ python --version
$ pip --version 
```

### Installation & Configuration

Clone the repo and cd into the directory: 

```bash
$ git clone https://github.com/araekiel/instahunter.git
$ cd instahunter
```

Run the following command to install the required packages:

```bash
$ pip install -r requirements.txt
```

Once the packages are installed, run the following command to start instahunter:

```bash
$ python src/main.py
```

## Release & Changelog

#### v2.0 Changelog: 
- **click** has been replaced with **pyinquirer** for a better interface.
- **rich** has been used for better text formatting.
- Instagram blocking requests on its web api has been partially fixed with user-agent header.
- The only output format available now is **json**.
- Complete code refactor.

#### v2.0 Executable Download:
[Instahunter v2.0](https://github.com/araekiel/instahunter/releases/download/v2.0/instahunter.exe) (.exe)

## Authors

- **araekiel** - [Github](https://github.com/araekiel)

## License

[MIT License](https://github.com/araekiel/instahunter/blob/master/LICENSE) | Copyright (c) 2022 Kumar Shashwat
