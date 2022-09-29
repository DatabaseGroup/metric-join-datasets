#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("USAGE: ./blowup.py <dataset> <blowup-factor>")

    dataset = sys.argv[1]
    blowup_factor = int(sys.argv[2])

    records = []
    frequencies = {}

    with open(dataset) as f:
        for line in f.readlines():
            record = [int(x) for x in line.strip().split(" ")]

            for token in record:
                if token in frequencies:
                    frequencies[token] += 1
                else:
                    frequencies[token] = 1

            records.append(record)

    ordered_freq_keys = [k for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)]
    universe_size = len(ordered_freq_keys)

    def next_of(token):
        global ordered_freq_keys, universe_size

        next_idx = ordered_freq_keys.index(token) + 1

        if next_idx >= universe_size:
            ordered_freq_keys.append(universe_size + 1)
            universe_size += 1

        return ordered_freq_keys[next_idx]

    for record in records:
        print(" ".join(map(str, record)))

        for i in range(blowup_factor - 1):
            new_record = []
            for token in record:
                new_record.append(next_of(token))

            print(" ".join(map(str, new_record)))
            record = new_record
