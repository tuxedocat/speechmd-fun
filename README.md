Fun with Google TTS using SpeechMarkdown
===============================

Prerequisites
--------------

Enable TTS API on your GCP project, and get service account key or set default account, then:

### Setup required packages

```sh
yarn install

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


Usage
------

Convert `textfile.speechmarkdown` to SSML as Google Assistant's dialect.

```sh
node sm2ssml.js input.speechmarkdown > input.ssml
```

Use python API to get generated MP3 file.

```sh
python speech.py input.ssml spoken.mp3
```


Notice
------

```
Example dialogue is taken from the game "Bloodborne" manually. (c) 2014-2020 FROMSOFTWARE Inc.
```
