# oot-extended-charmap
A base mod with extended character support for all in-game text in the [Legend of Zelda: Ocarina of Time decompilation project](https://github.com/zeldaret/oot).

## Feature info
The newly supported characters in this version are:
- The remaining acute accent characters not included in the original game (Í/í, Ó/ó, and Ú/ú)

Contributions adding other characters welcome.

## Setup
Note: because of how regularly OOT code changes are merged, it is recommended you apply this mod to the tree on which it
was last successfully tested. In this case, you can get it by simply running:
```bash
git clone https://github.com/zeldaret/oot.git
cd oot
git checkout a9284494f2b6f53a0e8f95b5567faf1b2162e91c
```

#### 1. Follow the README.md instructions from the OOT repo
#### 2. In a fresh terminal, run:
``` bash
git clone https://github.com/caffalaughrey/oot-extended-charmap.git
cd oot-extended-charmap
./add_to_project.py /path/to/oot
```
#### 3. Modify some easy-to-find text in /oot/assets/text/message_data.h to use extended characters
#### 4. In your OOT terminal, re-run the final `make` or `gmake` command, depending on your OS
#### 5. Play the game and find your text
