import requests
import gzip
import shutil
from pathlib import Path

# make sure data folder exists
Path("data").mkdir(exist_ok=True)

# TinyStories train and valid
urls = {
    "data/TinyStoriesV2-GPT4-train.txt": "https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStoriesV2-GPT4-train.txt",
    "data/TinyStoriesV2-GPT4-valid.txt": "https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStoriesV2-GPT4-valid.txt",
    "data/owt_train.txt.gz": "https://huggingface.co/datasets/stanford-cs336/owt-sample/resolve/main/owt_train.txt.gz",
    "data/owt_valid.txt.gz": "https://huggingface.co/datasets/stanford-cs336/owt-sample/resolve/main/owt_valid.txt.gz",
}

# download files
for local_path, url in urls.items():
    print(f"Downloading {url} ...")
    r = requests.get(url, stream=True)
    with open(local_path, "wb") as f:
        shutil.copyfileobj(r.raw, f)

# unzip the .gz files
for gz_file in ["data/owt_train.txt.gz", "data/owt_valid.txt.gz"]:
    out_file = gz_file.replace(".gz", "")
    print(f"Unzipping {gz_file} -> {out_file}")
    with gzip.open(gz_file, "rb") as f_in:
        with open(out_file, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
