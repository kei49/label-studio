from label_studio_sdk import Client

from label_studio.config import Config

def create_new_project_with_azure_blob_storage():
    ls = Client(url=Config.label_studio_url, api_key=Config.api_key)
    ls.check_connection()
    
    project = ls.start_project(
        title='Audio Annotation Project from SDK',
        label_config='''
        <View>
        <Audio name="audio" value="$audio" zoom="true" hotkey="ctrl+enter" />
        <Header value="Provide Transcription" />
        <TextArea name="transcription" toName="audio"
                    rows="4" editable="true" maxSubmissions="1" />
        </View>
        ''',
    )
    
    project.connect_azure_import_storage(
        Config.azure_container, use_blob_urls=True, account_name=Config.azure_account_name, account_key=Config.azure_connection_string)
    
    
# audio_data = [
#     "https://sttdatastoredev.blob.core.windows.net/stt-session-audio/w576/u640/20230705174832_5454668_70305FD4184F44B09CA131DE9EA2BBA7.wav",
#     "https://sttdatastoredev.blob.core.windows.net/stt-session-audio/w576/u13047/20230705174959_5457561_1AD4A4971F0C47AC81BED38BF368F9DA.wav",
#     # "azure-blob://stt-session-audio/w576/u9925/20230705175020_5459943_7CB064F139364FFFB9A6D9DBC1FA74C2.wav"
# ]

# tasks = []
# for audio_path in audio_data:
#     tasks.append({"data": {'audio': audio_path, 'meta_info': "this is the infomation as meta"}})

# project.import_tasks(tasks)
