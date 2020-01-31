import random


def read():
    audio_id = []
    with open('audio.txt') as f:
        for line in f:
            line = line.replace('\n', '')
            audio_id.append(line)
    audio = []
    for i in range(1, 10):
        index = random.randint(1, len(audio_id) - 10)

        for i in range(index, index + 1):
            audio.append(audio_id[i])
    attachment = ','.join(audio)
    return attachment