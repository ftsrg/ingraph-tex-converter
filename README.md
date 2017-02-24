# ingraph-tex-converter

[![Build Status](https://travis-ci.org/FTSRG/ingraph-tex-converter.svg?branch=master)](https://travis-ci.org/FTSRG/ingraph-tex-converter)

:warning: **Warning.** This app is intended as a research tool to be run on a single VM. There is zero security involved, i.e. the users might use the web service run malicious scripts.

## Dependencies

### ingraph

Clone the [`ingraph`](https://github.com/FTSRG/ingraph) repository next to the `ingraph-tex-converter` repository.

### Python 3 / Flask

```
sudo apt-get install -y python3-pip python3-setuptools
sudo pip3 install flask
```

### TeX Live

```
sudo apt-get install -y texlive-base texlive-science texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra texlive-xetex latexmk lmodern pgf
```

## Running the server

```
./run.sh
```
