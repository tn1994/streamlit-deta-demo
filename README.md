---
title: {{ title }}
python_version: 3.10.7
sdk: streamlit
sdk_version: 1.10.0
app_file: src/app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

---

# streamlit-template

## Usage

1. Copy from secrets_config/sample.secrets.toml to .streamlit/secrets.toml, and input value

```toml
env='develop'
hashed_text='5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
```

2. Run build.sh

```shell
sh build.sh
```

3. Run compose_up.sh

```shell
sh compose_up.sh
```

4. Access to localhost:8501

[Access](http://localhost:8501/)

## About requirements.txt

```shell
# Basic
streamlit
pandas
numpy
matplotlib
scikit-learn
```

---

## Setup about Huggingface

```shell
git remote add space https://huggingface.co/spaces/{{ OWNER NAME }}/{{ SPACE NAME}}
git push --force space main

# example:
git remote add space https://huggingface.co/spaces/tn1994/streamlit-template
git push --force space main
```

- Add README.md

https://huggingface.co/docs/hub/spaces-settings#spaces-settings

https://huggingface.co/docs/hub/spaces-config-reference

- Setup github actions

https://huggingface.co/docs/hub/spaces-github-actions

- Get access token

https://huggingface.co/settings/tokens

- Setup github action secrets

https://obel.hatenablog.jp/entry/20220129/1643400000

- Setup space secrets

https://huggingface.co/docs/hub/spaces-overview#managing-secrets

- Theme Settings

https://huggingface.co/settings/theme