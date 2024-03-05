### A voice-interaction English language practice programme developed using Streamlit and the OpenAI API. 

- **User Interface**: Participants interact with the system through a web application (see Figure below), speaking via a 'Record' button, and receiving voice responses. The interface also displays the system's latest response and the conversation history.
- **Language Model**: We employ the 'gpt-3.5-turbo' model, using up to 3 rounds of preceding user-system exchanges (equivalent to 6 preceding speaking turns) as contextual input for generating responses.
<img width="1269" alt="Screenshot of the Designed User Interface 23 33 00" src="https://github.com/liqunhe27/Kelly/assets/52518024/864fc828-f445-4bb4-bdb1-f59decb6a8dc">
#### Identified Limitations:
- **ASR language misidentification**. During speech-to-text conversion, the system may wrongly identify languages, resulting in non-English text output. Consider checking if the ASR model allows language selection (parameters).
- **Non-English response**. When interacting, mentioning China or its cities might trigger Chinese responses. Consider stressing the use of English in prompts, and asking user to repeat if receiving non-English text (probably due to speech recognition issues).
- **Off-Topic response**. For evaluation, additionally consider ‘off-topic’ responses since the model may sometimes deviate from the current topic and only respond to a part of the input.
