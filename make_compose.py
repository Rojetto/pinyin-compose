LETTER_ACCENTS = {
    "a": "āáǎà",
    "e": "ēéěè",
    "i": "īíǐì",
    "o": "ōóǒò",
    "u": "ūúǔù",
    "ü": "ǖǘǚǜ"
}

# now let's read the list of syllable line by line, writing the compose entries for each syllable into a file
with open("syllables.txt", "r", encoding="utf-8") as syllables:
    with open("pinyin.module", "w", encoding="utf-8") as pinyin:
        for line in syllables:
            # remove the newline character
            line = line.rstrip()
            # find "-" position
            dash_pos = line.find("-")
            # find vowel to apply accent to
            vowel = line[dash_pos + 1]
            before_vowel = line[:dash_pos]
            after_vowel = line[dash_pos + 2:]
            syllable_without_tone_mark = before_vowel + vowel + after_vowel

            # generate entries for all four tones
            for tone in range(0, 4):
                syllable_with_tone_mark = before_vowel + LETTER_ACCENTS[vowel][tone] + after_vowel
                letter_keys = ["dead_lowline"] + ["udiaeresis" if letter=="ü" else letter for letter in list(syllable_without_tone_mark)]

                key_lists = [letter_keys + [str(tone + 1)], letter_keys + [f"KP_{tone + 1}"]]
                if "udiaeresis" in letter_keys:  # enable typing v instead of ü
                    letter_keys_with_v = ["v" if key=="udiaeresis" else key for key in letter_keys]
                    key_lists.append(letter_keys_with_v + [str(tone + 1)])
                    key_lists.append(letter_keys_with_v + [f"KP_{tone + 1}"])

                for key_list in key_lists:
                    pinyin.write(" ".join(f"<{key}>" for key in key_list) + ' : "' + syllable_with_tone_mark + '"\n')
