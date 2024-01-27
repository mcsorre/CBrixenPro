import streamlit as st
import random
from PIL import Image
from gtts import gTTS
from translate import Translator


if "page" not in st.session_state:
  st.session_state.page = 0
if "user_input" not in st.session_state:
  st.session_state.user_input = None
if "rand_item" not in st.session_state:
  st.session_state.rand_item = None

#Define functions
def nextpage():
  st.session_state.page += 1
def restart():
  st.session_state.page = 0
  st.session_state.rand_item = random.choice(['chair', 'cold', 'earth', 'friend', 'heart', 'mountain', 'mouse', 'snow', 'woman'])

placeholder = st.empty()

if st.session_state.page == 0:
  items = ['chair', 'cold', 'earth', 'friend', 'heart', 'mountain', 'mouse', 'snow', 'woman']   
  if 'item' not in st.session_state:
    st.session_state.rand_item = random.choice(items)
    st.session_state.item = st.session_state.rand_item
  else:
    rand_item = st.session_state.item
  with placeholder.container():
    st.header(':red[The English IPA Quiz:] :blue[_Decoding Words_]', divider='rainbow')
    st.write("\n")
    st.write("\n")
    st.subheader(':blue[Embark on a linguistic adventure with the _immersive IPA (International Phonetic Alphabet) Quiz_] :red[designed to challenge and enhance your understanding of _British English pronunciation_]')
    st.write("\n")
    st.write("\n")
    expander = st.expander("As a brief recall, click here to check what symbols mean in the IPA ")
    expander.write("""
        This table shows the phonemic chart of English sounds:
    """)
    expander.image("https://www.englishclub.com/images/pronunciation/Phonemic-Chart.jpg")
    st.write("\n")
    st.write("\n")
    st.subheader(":uk: :uk: :uk: Let's go! :uk: :uk: :uk:", divider='grey')
    st.subheader(':blue[Decipher the] :red[IPA symbol]')
    st.write("\n")
    st.write("\n")
  picture = "image/" + st.session_state.rand_item + '.jpg'
  img = Image.open(picture)
  st.image(img, width=300)
  st.session_state.user_input = st.text_input("Type in the English word you see in the IPA symbol. **Remember to first press Enter and then click on Continue.**", key=1)
  st.button("Continue",on_click=nextpage,disabled=(st.session_state.page > 1))
  

elif st.session_state.page == 1:
  if st.session_state.user_input:
    if st.session_state.user_input.lower() == str(st.session_state.rand_item):
      text_to_translate = str(st.session_state.rand_item)
      translator = Translator(to_lang='it')
      result = Translator.translate(translator, text_to_translate)
      picture = "image/" + st.session_state.rand_item + '.jpg'
      img = Image.open(picture)
      st.image(img, width=300)
      placeholder.header("Great job! That is correct!.")
      st.write("The word '",st.session_state.rand_item,"' translates to '",result,"' in italian.")
      st.write("Now you can practice the pronunciation of this word")
      tts=gTTS(text= st.session_state.rand_item, lang='en', tld='co.uk')
      tts.save('user.mp3')
      st.audio('user.mp3')
      st.write("Well done! If you want to keep practising, refresh the page.")

    else:      
      text_to_translate = str(st.session_state.rand_item)
      translator = Translator(to_lang='it')
      result = Translator.translate(translator, text_to_translate)
      picture = "image/" + st.session_state.rand_item + '.jpg'
      img = Image.open(picture)
      st.image(img, width=300)
      placeholder.header("Unfortunately, that is not correct.")
      st.write("The correct word was '",st.session_state.rand_item,"'.")
      st.write("The word '",st.session_state.rand_item,"' translates to '",result,"' in italian.")
      st.write("Now you can practice the pronunciation of this word")
      tts=gTTS(text= st.session_state.rand_item, lang='en', tld='co.uk')
      tts.save('user.mp3')
      st.audio('user.mp3')
      st.write("Well done! If you want to keep practising, refresh the page.")
