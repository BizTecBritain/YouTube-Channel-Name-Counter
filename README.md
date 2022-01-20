[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
<!--[![LinkedIn][linkedin-shield]][linkedin-url]-->



<br />
<p align="center">
  <a href="https://github.com/BizTecBritain">
    <img src="https://github.com/BizTecBritain/BizTecBritain/blob/main/BizTec.png" alt="Logo" width="580" height="300">
  </a>

  <h3 align="center">YouTube Channel Name Counter</h3>

  <p align="center">
    A program that takes a list of YouTube URLs and outputs a file containing the channel names and how many of their videos are in the list
    <br />
    <a href="https://github.com/BizTecBritain/YouTube-Channel-Name-Counter/blob/main/docs/Usage.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/BizTecBritain/YouTube-Channel-Name-Counter">View Demo</a>
    ·
    <a href="https://github.com/BizTecBritain/YouTube-Channel-Name-Counter/issues">Report Bug</a>
    ·
    <a href="https://github.com/BizTecBritain/YouTube-Channel-Name-Counter/issues">Request Feature</a>
  </p>
</p>



<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



## About The Project

One of my friends requested this program to be made to assist with the [TASVideos](http://tasvideos.org/) webpage.
Make sure that you check them out!


### Built With

* Python version: 3.9 (Tested)
* Python version: 3.x



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
$ python YoutubeCLI.py [path to a text file with YT links] [path to an output folder] [optional parameters (see docs)]
```

_For more examples, please refer to the [Documentation](https://github.com/BizTecBritain/YouTube-Channel-Name-Counter/blob/main/docs/Usage.md)_



## Roadmap

See the [open issues](https://github.com/BizTecBritain/YouTube-Channel-Name-Counter/issues) for a list of proposed features (and known issues).



## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## License

Distributed under the MIT License. See `LICENSE` for more information.



## Contact

Alexander Bisland - Twitter: [@BizTecBritain](https://twitter.com/BizTecBritain) - Email: BizTecBritain@gmail.com

Project Link: [https://github.com/BizTecBritain/YouTube-Channel-Name-Counter](https://github.com/BizTecBritain/YouTube-Channel-Name-Counter) 



## Acknowledgements

* Thanks to [othneildrew](https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md) for the blank README.md file
* Thanks to [TASVideos](http://tasvideos.org/) for the inspiration

[contributors-shield]: https://img.shields.io/github/contributors/BizTecBritain/YouTube-Channel-Name-Counter.svg?style=for-the-badge
[contributors-url]: https://github.com/BizTecBritain/YouTube-Channel-Name-Counter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BizTecBritain/YouTube-Channel-Name-Counter.svg?style=for-the-badge
[forks-url]: https://github.com/BizTecBritain/YouTube-Channel-Name-Counter/network/members
[issues-shield]: https://img.shields.io/github/issues/BizTecBritain/YouTube-Channel-Name-Counter.svg?style=for-the-badge
[issues-url]: https://github.com/BizTecBritain/YouTube-Channel-Name-Counter/issues
<!--[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/username-->
