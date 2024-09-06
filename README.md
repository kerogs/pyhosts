# pyhosts
configuration auto for hosts files for windows / linux

> [!IMPORTANT]
> the exe file must always be launched as administrator on windows!

## Install
```
git clone https://github.com/kerogs/ksp.git
cd ksp
pip install -r requirements.txt
```

## build
```sh
.\.venv\Scripts\activate
cd .\[windows or linux]
pip install pyinstaller
pyinstaller --onefile main.py
```