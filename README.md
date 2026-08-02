# Emotion Detection with Embedded AI

A small web application that analyzes text and detects the emotions expressed in it (anger, disgust, fear, joy, sadness) using IBM Watson NLP's Emotion Predict service.

## How it works

- `emotion_detection.py` — sends the input text to the Watson NLP Emotion Predict endpoint (`sn-watson-emotion.labs.skills.network`) and returns the raw JSON response containing per-emotion scores.
- `templates/index.html` — the web page. It has a text box, a "Run Sentiment Analysis" button, and a results area, styled with Bootstrap.
- `static/mywebscript.js` — sends the text from the page to a server endpoint (`/emotionDetector`) via an XHR GET request and renders the response in the page.

## Project structure

```
.
├── emotion_detection.py   # Core function that calls the Watson NLP emotion API
├── templates/
│   └── index.html         # Front-end page
├── static/
│   └── mywebscript.js     # Front-end logic (calls /emotionDetector)
├── LICENSE
└── README.md
```

## Requirements

- Python 3.x
- [`requests`](https://pypi.org/project/requests/)

Install dependencies:

```bash
pip install requests
```

## Usage

`emotion_detector` in `emotion_detection.py` can be used directly:

```python
from emotion_detection import emotion_detector

result = emotion_detector("I am so happy with this project!")
print(result)
```

The front end (`templates/index.html` + `static/mywebscript.js`) expects a server route `GET /emotionDetector?textToAnalyze=<text>` that calls `emotion_detector` and returns the result, so a Flask (or similar) server exposing that route is required to run the web UI end to end.

## License

Licensed under the [Apache License 2.0](LICENSE).
