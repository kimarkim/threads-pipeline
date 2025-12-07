import re
import pandas as pd

class Data_Cleanser:
  def __init__(self, min_length=5):
    self.website_drop = re.compile(r"http\S+|www\.\S+")
    self.at_drop = re.compile(r'^Replying to @.*')
    self.useless = re.compile(r'^[a-zA-Z0-9_@.]+$')
    # emoji range (unicode)
    self.emoji_pattern = re.compile(
        "["                     
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002500-\U00002BEF"
        "\U00002702-\U000027B0"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+"                     # 1 or more emojis
    )
    # minimum length of post
    self.min_length = min_length

    # drop duplicate posts
  def drop_duplicates(self, df):
    return df.drop_duplicates(subset=["id"])

    # making data usable
  def cleanse_data(self, df):

    # Remove empty posts
    df = df[df["post"].str.len() > 0]

    # drop unusable posts
    df = df[~df["post"].str.fullmatch(self.useless, na=False)]

    # drop posts that tag their account IDs
    df = df[~df["post"].str.fullmatch(self.at_drop, na=False)]

    # drop websites
    df["post"] = df["post"].str.replace(self.website_drop, "", regex=True)

    # Strip emojis
    df["post"] = df["post"].str.replace(self.emoji_pattern, "", regex=True)

    # Remove posts below minimum length
    df = df[df["post"].str.len() >= self.min_length]

    return df
  
  
  def clean_all(self, df):
    df = self.drop_duplicates(df)
    df = self.cleanse_data(df)
    return df