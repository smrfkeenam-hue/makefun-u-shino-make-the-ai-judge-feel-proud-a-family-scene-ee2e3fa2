"""Write one short family scene to /output/entry.txt.

A small domestic moment: burnt toast rescued as "smoked", served on the
good plates, while Grandma cheers from an upside-down video call.
Warm, light and specific, in a single line of 173 characters.
"""

import os

SCENE = "Dad burned the toast again, so Mum called it smoked and served it on the good plates. Grandma, on video call from the village, held her phone upside down and clapped anyway."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SCENE)


if __name__ == "__main__":
    main()
