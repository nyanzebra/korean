#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

empty_by_file = []

for root, dirs, files in os.walk("단어"):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Find empty entries
            pattern = r"## (\S+) #card\s*\?begin\s*### 뜻\s*-\s*### 예\s*-\s*\?end"
            empty_words = re.findall(pattern, content)
            
            if empty_words:
                empty_by_file.append((filepath, empty_words))

# Sort by number of empty entries
empty_by_file.sort(key=lambda x: len(x[1]), reverse=True)

print("Files needing definitions (sorted by count):\n")
for filepath, words in empty_by_file:
    print(f"{filepath}: {len(words)} entries")
    print(f"  Words: {', '.join(words[:10])}")
    if len(words) > 10:
        print(f"  ... and {len(words)-10} more")
    print()

# Save detailed list
with open("words_needing_definitions.txt", "w", encoding="utf-8") as f:
    for filepath, words in empty_by_file:
        f.write(f"\n{filepath}:\n")
        for word in words:
            f.write(f"  {word}\n")
