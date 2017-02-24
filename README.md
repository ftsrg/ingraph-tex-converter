# ingraph-tex-converter

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
export FLASK_APP=ingraph.py && flask run
```
