import google.generativeai as genai

genai.configure(api_key="AIzaSyDspE7CCk_QywF7-jwZsnJc5TEktukE6wo")

for m in genai.list_models():
    print(m.name)