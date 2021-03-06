[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]


## About The Project

One of my friends requested this program to be made to assist with the [TASVideos](http://tasvideos.org/) webpage.
Make sure that you check them out!


### Built With

* Python version: 3.9 (Tested)
* Python version: 3.x


# Recap on How to Build

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Install git and python
  ```
   $ sudo apt-get update
   $ sudo apt-get install git
   $ sudo apt-get install python
  ```

* Create virtual environment
  * #### Linux:
    ```
    $ python -m venv venv
    $ venv/bin/activate
    ```
  * #### Windows:
    ```
    > python -m venv venv
    > venv/Scripts/activate.bat
    ```
 
* Get a YouTube API Key
  * A good website to visit is [here](https://blog.hubspot.com/website/how-to-get-youtube-api-key)
  * Follow these steps to get your API key and make sure that you remember it<br>
    1\. Log in to Google Developers Console<br>
    2\. Create a new project<br>
    3\. On the new project dashboard, click Explore & Enable APIs<br>
    4\. In the library, navigate to YouTube Data API v3 under YouTube APIs<br>
    5\. Enable the API<br>
    6\. Create a credential<br>
    7\. A screen will appear with the API key ⚠️**IMPORTANT** You must remember this key for later⚠️


### Installation

Clone the repo with ```$ git clone https://github.com/BizTecBritain/YouTube-Channel-Name-Counter.git```

Then enter the directory with ```$ cd YouTube-Channel-Name-Counter```

Open the file ```YoutubeCLI.py``` with your preferred text editor or with
* Linux: ```$ nano YoutubeCLI.py```
* Windows: ```> notepad YoutubeCLI.py```

Then navigate to line 26, insert your API Key and close the document.

Then install the python requirements with ```$ pip install -r requirements.txt```


## Usage

First verify you are in the correct directory, if not, run
```
$ cd YouTube-Channel-Name-Counter
```

Then to use this code run
```
$ python YoutubeCLI.py [path to a text file with YT links] [path to an output folder] [optional parameters (see below)]
```

### Optional Parameters
To see some of the parameters in the command line run
```
$ python YoutubeCLI.py -h
```

#### Output file parameters (Multiple can be used)
* [-p] or [--pickle] - output to a python serialsed file (aka [.pickle](https://docs.python.org/3/library/pickle.html))
* [-c] or [--csv]    - output to a csv file
* [-j] or [--json]   - output to a json file

#### Other Parameters
* [-d] or [--disable-progressbar] - disables the progressbar (who knew?)
* [-a] or [--api-key] - allows you to use a new api  key but only when this program is running
* [--debug] - output go brrrrrr


[contributors-shield]: https://img.shields.io/github/contributors/BizTecBritain/YouTube-Channel-Name-Counter.svg?style=for-the-badge
[contributors-url]: https://github.com/BizTecBritain/YouTube-Channel-Name-Counter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BizTecBritain/YouTube-Channel-Name-Counter.svg?style=for-the-badge
[forks-url]: https://github.com/BizTecBritain/YouTube-Channel-Name-Counter/network/members
[issues-shield]: https://img.shields.io/github/issues/BizTecBritain/YouTube-Channel-Name-Counter.svg?style=for-the-badge
[issues-url]: https://github.com/BizTecBritain/YouTube-Channel-Name-Counter/issues
