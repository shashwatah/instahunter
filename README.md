<img alt="Instahunter" src="https://raw.githubusercontent.com/KSSBro/instahunter/gh-pages/public/images/logo.png" height="100">

# Instahunter

[Instahunter](https://kssbro.github.io/instahunter) is a CLI app that can fetch posts and user data from Instagram's frontend API.

## Getting Started

### Prerequisites

To run the app from source - [Git](https://git-scm.com/) is needed to clone the repository on your machine. [Python](https://www.python.org/) and [Click](https://click.palletsprojects.com/en/7.x/) are required to run the app from the source.

### Installing

After installing **git**, clone the repository on your machine

```
git clone https://github.com/KSSBro/instahunter.git
```

After installing **Python**, install **Click** with **pip**

```
pip install click
```

### Usage

Running from the source:

```
python instahunter.py
```

To get help use **--help**:

```
instahunter --help
```

```
instahunter getposts --help
```

#### Getting Posts

Use the command **getposts** to get posts.

Options:

- `-tag`: tag you want to fetch posts with 
- `--post-type` : latest(default) - fetch latest posts, top - fetch top posts

```
instahuter getposts -tag *hashtag* --post-type *latest or top*
```

#### Getting User Data

Use the command **getuser** to get user data.

Options:

- `-username`: username you want to fetch user data with

```
instahunter getuser -username *username*
```

#### Getting User Posts

Use the command **getuserposts** and option **-username** to get posts.

```
instahunter getuserposts -username *username*
```

#### Searching for Users

Use the command **search** and option **-query** to search for users.

```
instahunter search -query *query*
```

> All the above commands will display data in the terminal itself.

#### Creating a file with the data

To create a file with the data retrieved use **-create-file** and **--file-type** options along with any option.

Options:

- `-create-file`: true - will create a file with the data, false(default) - won't create a file
- `--file-type` : json - will create a json file, text(default) - will create a text file

```
instahunter getposts -tag *hashtag* -create-file *true or false* --file-type *json or text*
```

## Release & Changelog

Current Version: v1.6.1

Changelog: 
- Command **gettopposts** removed
- Command **getposts** has ***-post-type*** option now to fetch latest or top posts
- Option ***-via*** removed from Command **getuser** (Deprecated endpoint)
- Some data removed from Command **search** 
- Minor bug fix

## Download

Click here: [Instahunter](https://kssbro.github.io/instahunter/public/bin/instahunter.exe)

## Libraries

- [Click](https://click.palletsprojects.com/en/7.x/) was used to make the CLI
- [Pyinstaller](https://www.pyinstaller.org/)(Executable) was used to build the executable
- A customized version of [termynal](https://github.com/ines/termynal) by [Ines Montani](https://github.com/ines) was used on the [gh-pages website of Instahunter](https://kssbro.github.io/instahunter) to make the animated command line.
 
## Contributing

Fork the repository and open a pull request to contribute.
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- **KSSBro** - [Github](https://github.com/KSSBro)

## License

[MIT](https://choosealicense.com/licenses/mit/)
