from deep_translator import GoogleTranslator

# Function for translation
def translate_text(text, source_lang, target_lang):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return translator.translate(text)

# Test the function
english_text = "Calculate Entropy"
swahili_translation = translate_text(english_text, "en", "sw")
print(f"English: {english_text}")
print(f"Swahili: {swahili_translation}")

swahili_text = "Sifanyi mtihani"
english_translation = translate_text(swahili_text, "sw", "en")
print(f"Swahili: {swahili_text}")
print(f"English: {english_translation}")
