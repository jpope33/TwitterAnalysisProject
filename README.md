# Twitter Analysis Project

## Installation

### Python

This application uses Python 3.5. The code has several dependencies which may be installed by
running the following commands:

```bash
pip3 install Flask
pip3 install MySQL-python
pip3 install python-twitter-tools
pip3 install twitter
```

### Web client

To set up the web client, ensure you have node.js and NPM installed, and run the following commands:

```bash
cd client

npm install
```

To build the front-end code, run the following command:
```bash
npm run build
```

## Twitter API Tokens

The application fetches data from Twitter using the Twitter API. Doing so requires a set of access
tokens. To generate these follow the instructions from the following link:
https://dev.twitter.com/oauth/overview/application-owner-access-tokens and 

For the server to run, you must open `FinalScript/TweetAnalyzer.py` and change the tokens to the ones you
received.

## Server

Finally, to start the server, run the following from the root project folder:

```bash
python3 main.py
```

## Useful links

Twitter Python tools https://github.com/sixohsix/twitter
