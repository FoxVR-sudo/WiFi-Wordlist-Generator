from tqdm import tqdm

def generate_wordlist_low_ram(base_file, output_file, symbols=False, years=False, phone_numbers=False):
    print(f"Starting LOW RAM mode with progress bar...")

    symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_']
    year_list = [str(year) for year in range(1950, 2026)]
    phone_prefixes = ['088', '089', '087']

    def variations(word):
        return [word, word.lower(), word.upper(), word.capitalize()]

    # Първо броим броя редове, за да знаем общия брой базови думи
    with open(base_file, 'r', encoding='utf-8', errors='ignore') as f:
        total_lines = sum(1 for _ in f)

    with open(output_file, 'w', encoding='utf-8') as out:
        with open(base_file, 'r', encoding='utf-8', errors='ignore') as f:
            for word in tqdm(f, total=total_lines, desc="Generating"):
                word = word.strip()
                if not word:
                    continue
                var_list = variations(word)

                for v in var_list:
                    out.write(f"{v}\n")

                    if symbols:
                        for s in symbol_list:
                            out.write(f"{v}{s}\n")
                            for n in range(10):
                                out.write(f"{v}{s}{n}\n")

                    if years:
                        for y in year_list:
                            out.write(f"{v}{y}\n")
                            out.write(f"{y}{v}\n")

                    if phone_numbers:
                        for prefix in phone_prefixes:
                            for num in range(1000000):
                                phone = f"{prefix}{num:06d}"
                                out.write(f"{v}{phone}\n")
                                out.write(f"{phone}{v}\n")

    print(f"Wordlist (LOW RAM) generated and saved to {output_file}")


def generate_wordlist():
    return None