# Language Translator using deep-translator and Tkinter

from tkinter import *
from deep_translator import GoogleTranslator

def translate_text():
    try:
        input_text = text_input.get("1.0", END).strip()
        src_lang = src_lang_var.get()
        dest_lang = dest_lang_var.get()
        
        translator = GoogleTranslator(source=src_lang, target=dest_lang)
        translated = translator.translate(input_text)
        
        text_output.delete("1.0", END)
        text_output.insert(END, translated)
    except Exception as e:
        text_output.delete("1.0", END)
        text_output.insert(END, f"Error: {e}")

root = Tk()
root.title("Language Translation Tool")
root.geometry("500x400")
root.configure(bg="#e6f2ff")

# Language Selection
Label(root, text="Source Language:", bg="#e6f2ff").pack()
src_lang_var = StringVar(value='en')
OptionMenu(root, src_lang_var, 'en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ja', 'ko', 'zh-CN').pack()

Label(root, text="Target Language:", bg="#e6f2ff").pack()
dest_lang_var = StringVar(value='es')
OptionMenu(root, dest_lang_var, 'en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ja', 'ko', 'zh-CN').pack()

# Input Text
Label(root, text="Enter Text:", bg="#e6f2ff").pack()
text_input = Text(root, height=5, width=50)
text_input.pack()

Button(root, text="Translate", command=translate_text, bg="#4da6ff").pack(pady=10)

# Output Text
Label(root, text="Translated Text:", bg="#e6f2ff").pack()
text_output = Text(root, height=5, width=50)
text_output.pack()

root.mainloop()