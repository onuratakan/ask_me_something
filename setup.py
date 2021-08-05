from setuptools import setup


setup(name='ask_me_something',
version='0.1.1',
description="""A speak to text library with embedded cache system.""",
long_description="""
# Ask Me Something
A speak to text library with embedded cache system.
# Install
```
pip3 install ask-me-something
```
# Using
## In another script
```python
from ask_me_something import ask

# ask(text = "Say something to mic", language = "en-en")

print(ask())
```
## In command line
```console
  -h, --help            show this help message and exit
  -t TEXT [TEXT ...], --text TEXT [TEXT ...]
                        Text
  -l LANGUAGE, --language LANGUAGE
                        Language
  -nc, --nocache        No cache
  -r, --reset           Reset (removing the caches)
  -ns, --nospeak        No speak
```

```console
say -t Hello
```
""",
long_description_content_type='text/markdown',
url='https://github.com/onuratakan/ask_me_something',
author='Onur Atakan ULUSOY',
author_email='atadogan06@gmail.com',
license='MIT',
packages=["ask_me_something"],
package_dir={'':'src'},
install_requires=[
    "SpeechRecognition==3.8.1",
],
entry_points = {
    'console_scripts': ['ask=ask_me_something.ask_me_something:ask'],
},
python_requires=">= 3, <= 3.6",
zip_safe=False)
