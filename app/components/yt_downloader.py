import time
from io import BytesIO

import streamlit as st
from pytube import YouTube


def yt_downloader():
    st.title('YouTube Video Downloader')

    with st.form(key='youtube_downloader_form'):
        youtube_url = st.text_input('Paste the YouTube video link here:', '')
        format_select = st.selectbox(
            'Choose the format:', ['mp4', 'mp3', 'audio']
        )
        submit_button = st.form_submit_button('Submit')

    if submit_button and youtube_url:
        if 'youtube.com/watch?v=' in youtube_url:
            try:
                yt = YouTube(youtube_url)

                if format_select == 'mp4':
                    video = yt.streams.filter(file_extension='mp4').first()
                elif format_select in ['mp3', 'audio']:
                    video = yt.streams.filter(only_audio=True).first()

                progress_bar = st.progress(0)

                buffer = BytesIO()
                video.stream_to_buffer(buffer)
                buffer.seek(0)

                for i in range(50):
                    time.sleep(0.1)
                    progress_bar.progress(i + 1)

                file_extension = 'mp3' if format_select == 'mp3' else 'mp4'
                mime_type = (
                    'audio/mp3' if format_select == 'mp3' else 'video/mp4'
                )

                st.download_button(
                    label='Download Video'
                    if format_select == 'mp4'
                    else 'Download Audio',
                    data=buffer,
                    file_name=f'{yt.title}.{file_extension}',
                    mime=mime_type,
                )
            except Exception as e:
                st.error(f'An error occurred while downloading the video: {e}')
        else:
            st.error('Please enter a valid YouTube URL.')
    elif submit_button and not youtube_url:
        st.error('Please enter a valid YouTube URL.')
    else:
        st.info('Please enter a YouTube URL and choose a format.')
