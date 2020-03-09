import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', required=True, type=str, help='path to input')
    parser.add_argument('--score_file', required=True, type=str, help='path to input')
    parser.add_argument('--origin_file', required=True, type=str, help='path to input')
    parser.add_argument('--threshold', required=True, type=float, help='path to input')
    parser.add_argument('--output', default=None, type=str, help='path to input')
    args = parser.parse_args()

    # path = os.path.abspath(args.output)
    # dirname = os.path.dirname(path)
    # filenames = os.listdir(dirname)
    # # print(filenames, os.path.basename(path))
    # assert os.path.basename(path) not in set(filenames)

    # "train_LSTMword.txt"
    valid_list = []
    with open(args.score_file, newline="", encoding="utf-8") as f:
        if args.type == "lstm":
            for s in f.readlines():
                data = s.split('\t')
                text = data[0]
                score = float(data[1])
                if score <= args.threshold:
                     valid_list.append(text)
        elif args.type == "bleu":
            for s in f.readlines():
                data = s.split('\t')
                text = data[0]
                score = float(data[1])
                if (score >= args.threshold):
                    valid_list.append(text)

    with open(args.origin_file, newline="", encoding="utf-8") as f:
        for s in f.readlines():
            data = s.split('\t')
            label = data[0].strip('\n')
            premise = data[1].strip('\n')
            hypothesis = data[2].strip('\n')
            if premise in valid_list:
                if hypothesis in valid_list:
                    if args.output:
                        with open(args.output, "a") as out:
                            out.write('{}\t{}\t{}'.format(label, premise, hypothesis) + '\n')


if __name__ == '__main__':
    main()

