create a virtual env and activate it:

```shell
virtualenv -p python youtube
. youtube/bin/activate
```

install the Pytube library using pip. Open your command prompt and run the following command:

```shell
pip3 install pytube

```

Now that Pytube is installed, you can use it to download YouTube videos. Here is an example Python script that downloads a video given its URL:

```py
from pytube import YouTube

# Specify the URL of the video to download
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object
yt = YouTube(url)

# Get the first available video stream
stream = yt.streams.first()

# Download the video
stream.download()

```

you can integrate this code into your backend by creating an API endpoint that accepts a YouTube video URL and returns a downloadable link to the video. Here is an example Flask app that does just that:

```py
from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.json['url']
    yt = YouTube(url)
    stream = yt.streams.first()
    download_url = stream.url
    return jsonify({'url': download_url})

if __name__ == '__main__':
    app.run()

```

## quick troubleshoot

### Upgrade Pytube

```shell
pip install --upgrade pytube
```

imports having error even after installing?

`reload your code editor`

in vscode:

- `Ctrl+Shift+P`
- type `Reload`
- click `Developer: Reload Window`
