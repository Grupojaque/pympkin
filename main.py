import time

REFRESH_MS = 7
current_time_ms = lambda: int(round(time.time() * 1000))

def show(word, char_on_ms, char_off_ms, word_on_ms):
    [type_char(char, char_on_ms, char_off_ms) for char in word]
    word_on(word, word_on_ms)

def type_char(char, on_ms, off_ms):
    char_on(char)
    time.sleep(on_ms)
    char_off(char)
    time.sleep(off_ms)

def word_on(word, on_ms):
    i = 0
    end_time_ms = current_time_ms + on_ms
    while current_time_ms < end_time_ms:
        char_on(word[i])
        time.sleep(REFRESH_MS)
        char_off(word[i])
        i = (i + 1) % word.len

def char_on(char):
    # Encender la letra.
    pass

def char_off(char):
    # apagar la letra.
    pass
