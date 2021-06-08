# Profanity Detector

- Installing:   
`pip install ProfanityDetector`

- Requirements:   
`requests`

# Sample Usage

```python
from ProfanityDetector import detector

sentence = "This is a sample sentence."
word, detected = detector(sentence)

if detected:
    print(f"Profanity detected.\nWord: {word}")
```   

Made with 💕 by [@TeamUltroid](https://t.me/TeamUltroid).