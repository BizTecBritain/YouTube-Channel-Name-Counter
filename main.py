from googleapiclient.discovery import build
import pickle
import json
from tqdm import tqdm
import os

output = {}


def request(youtube, YoutubeID, debug):
    resp = youtube.videos().list(
        part='snippet',
        id=YoutubeID
    ).execute()

    resp = youtube.channels().list(
        part='snippet',
        id=resp['items'][0]['snippet']['channelId']
    ).execute()['items'][0]['snippet']['title']

    if debug:
        print(resp)

    if resp in output:
        output[resp] += 1
    else:
        output[resp] = 1


def run(args):
    youtube = build('youtube', 'v3', developerKey=args.api_key)

    text = open(args.file, 'r')

    if not args.disable_progressbar:
        for i in tqdm(text.readlines()):
            value = i[i.rfind("?v=") + 3:].strip()
            if args.debug:
                print(value)
            request(youtube, value, args.debug)
    else:
        for i in text.readlines():
            value = i[i.rfind("?v=") + 3:].strip()
            if args.debug:
                print(value)
            request(youtube, value, args.debug)

    text.close()

    if args.csv:
        with open(args.output_folder+'\\'+'output.csv', 'w') as f:
            for key in output.keys():
                f.write("%s, %s\n" % (key, output[key]))

    if args.pickle:
        with open(args.output_folder+'\\'+'output.pickle', 'wb') as f:
            pickle.dump(output, f)

    if args.json:
        with open(args.output_folder+'\\'+'output.json', 'w') as f:
            json.dump(output, f)
