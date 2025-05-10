def combine_wordlists(wordlists, output_file):
    with open(output_file, 'w', encoding='utf-8') as out:
        for file in wordlists:
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    out.write(line)
    print(f"Combined {len(wordlists)} wordlists into {output_file}")
