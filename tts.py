import gtts
import re

#####################################
##    TTS                          ##
#####################################

def text_to_speech_problem(text):
  """Converts Text To Speech, plus cleans text to shortern and remove back ticks"""
  problem = extract_and_clean_problem_text(text)
  
  lang = "en"
  tts_file_name = "problem"

  gtts.gTTS(problem, lang=lang).save("static/audio/{}.mp3".format(tts_file_name))

def extract_and_clean_problem_text(text):
  """Cleans text to shortern and remove back ticks"""
  
  # Find the text from the beginning to "Example:" or "Note" (whichever is shorter)
  match = re.search(r'(.*?)(?:(Example:|Note:)|$)', text, re.DOTALL | re.MULTILINE)

  if match:
      # Get the matched text
      intro_description = match.group(1).strip()
      # Remove backticks
      intro_description = intro_description.replace('`', '')
      return intro_description
  else:
      return "sorry, no audio is available"


def text_to_speech(text):
  """Converts Text To Speech"""
  
  lang = "en"
  tts_file_name = "feedback"

  gtts.gTTS(text, lang=lang).save("static/audio/{}.mp3".format(tts_file_name))