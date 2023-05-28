import json
from flask import Flask, render_template
from pkg import bgram, request

app = Flask(__name__)

names_list = request.fetch_names("https://file.notion.so/f/s/fbbe6c40-a3f2-4a58-a90b-d8004f62fdcc/names.txt?id=18b71f91-b725-42c4-8d4c-5bf352a5719d&table=block&spaceId=7c849ae7-f9f9-4efe-9968-3fab523bf9e5&expirationTimestamp=1685354680170&signature=Lq1_-EET4PjIm414xjSm4XxLt89rsOQD2dTX_jzqSh4&downloadName=names.txt")
bigram_probs = bgram.train(names_list)

@app.route('/')
def index():
    data_json = json.dumps(bigram_probs)
    names = []

    for i in range(10):
        names.append(bgram.generate_name(bigram_probs))

    return render_template("index.html", data=data_json, names=names)


if __name__ == '__main__':
    app.run(port=8080,host="0.0.0.0", debug=True)
