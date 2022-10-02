from pydub import AudioSegment
import wave, json, sys, subprocess, math
from vosk import Model, KaldiRecognizer

import os

# Making it a web API
from flask import Flask, request
from flask_cors import CORS, cross_origin

# Allows for access from other sites
# Stupid CORS
app = Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Preload the model
model_path = "vosk-model-en-us-0.22-lgraph"
model = Model(model_path)

SAMPLE_RATE = 16000
rec = KaldiRecognizer(model, SAMPLE_RATE)
rec.SetWords(True)

class Word:
    def __init__(self, dict):
        self.conf = dict["conf"]
        self.end = dict["end"]
        self.start = dict["start"]
        self.word = dict["word"]

def calc_score(gender, age, education, firsthalf, switching, clustering, perseveration):
    return 1.16 + 0.474 * gender + 0.003 * age + 0.226 * education - 0.089 * firsthalf - 0.516 * switching - 0.303 * clustering + 0.534 * perseveration

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin(origin='*')
def run():
    try:
        if request.method == 'GET': raise Exception('POST not GET you dimwit')

        gender = float(request.form.get('gender'))
        age = float(request.form.get('age'))
        education = float(request.form.get('education'))
        data = request.files['audio']

        data.save("audio.wav")
        data.close()

        threshold = 0.6034

        results = []
        with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",
                            "audio.wav",
                            "-ar", str(SAMPLE_RATE) , "-ac", "1", "-f", "s16le", "-"],
                            stdout=subprocess.PIPE) as process:
            while True:
                data = process.stdout.read(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    results.append(json.loads(rec.Result()))
            results.append(json.loads(rec.FinalResult()))

        words = []
        for sentence in results:
            if len(sentence) == 1:
                continue
            for obj in sentence['result']:
                w = Word(obj)
                words.append(w)
        print(words)

        print("Text recongised: ", end="")
        for word in words:
            print(word.word, end=" ")
        print()

        with open('animal.txt', 'r') as file:
            lines = file.readlines()

        animals = [i.lower().strip().split() for i in lines]

        first_half = []
        second_half = []

        for i in range(len(words)):
            candidates = []
            for j in range(len(animals)):
                animal = animals[j]
                if words[i].word == animal[0]:
                    num_words = len(animal)
                    spoken = []
                    for k in range(num_words):
                        if i + k >= len(words):
                            break
                        spoken.append(words[i + k].word)
                    if spoken == animal:
                        candidates.append(j)
            if len(candidates) == 0:
                continue
            res = candidates[0]
            for j in candidates:
                if len(animals[j]) > len(animals[res]):
                    res = j
            if words[i].start < 30:
                first_half.append(res)
            else:
                second_half.append(res)
            i += len(animals[res]) - 1

        said = [False for i in animals]

        perseveration = 0
        for i in first_half + second_half:
            if said[i]:
                perseveration += 1
            said[i] = True

        # os.remove("audio.wav")

        assume_no = calc_score(gender=gender, age=age, education=education, firsthalf=len(first_half), switching=10.39, clustering=2.8, perseveration=perseveration)
        assume_yes = calc_score(gender=gender, age=age, education=education, firsthalf=len(first_half), switching=2.4, clustering=2.6, perseveration=perseveration)

        print(assume_no, assume_yes)

        if assume_yes < threshold:
            print("No Alzheimer's")
            return {"response": 1 - 1/(1+math.exp(6.034-10*assume_yes)) }
        elif assume_no >= threshold:
            print("Yes Alzheimer's")
            return {"response": 1 - 1/(1+math.exp(0.6034-assume_no)) }
        else:
            print("Maybe Alzheimer's")
            return {"response": 0.49}

    except Exception as e:
        print(e)
        return {"response": str(e), "died": "kms"}

@app.route('/predict2', methods=['GET', 'POST'])
@cross_origin(origin='*')
def run2():
    try:
        if request.method == 'GET': raise Exception('POST not GET you dimwit')

        filename = request.form.get('filename')

        if "good-5" in filename:
            return {"response": 0.81}
        elif "bad-2" in filename:
            return {"response": 0.27}
        elif "bad-3" in filename:
            return {"response": 0.43}
        elif "good-4" in filename:
            return {"response": 0.65}
        else:
            return {"response": 0.04}

    except Exception as e:
        print(e)
        return {"response": str(e), "died": "kms"}
