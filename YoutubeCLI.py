import argparse
import main

parser = argparse.ArgumentParser(description='Count the videos released by each channel')

parser.add_argument('file', type=str, help='the file of video links')  # 'Rj4jzdV4.txt'
parser.add_argument('output-folder', type=str, help='the output folder for the files')

parser.add_argument('-p', '--pickle', action='store_true',
                    help='output a pickle file')
parser.add_argument('-c', '--csv', action='store_true',
                    help='output a csv file')
parser.add_argument('-j', '--json', action='store_true',
                    help='output a json file')
parser.add_argument('-d', '--disable-progressbar', action='store_true',
                    help='disable the progressbar')

parser.add_argument('-a', '--api-key', type=str, help='use a different api key')

parser.add_argument('--debug', action='store_true',
                    help='debug go Brrrrrrrr')

args = parser.parse_args()

if args.api_key is None:
    args.api_key = 'AIzaSyCSmHxKV9iCwqlSz5q1tnEdP5W7VqUP-IE'

main.run(args)
