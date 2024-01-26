from io import BytesIO

import streamlit as st
from PIL import Image
from rembg import remove


def convert_image(img):
    buf = BytesIO()
    img.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload, col1, col2):
    try:
        image = Image.open(upload)

        col1.image(image, caption='Original Image')

        processing_text = col2.empty()

        processing_text.markdown(
            '<p style="text-align: center;">Processing...</p>',
            unsafe_allow_html=True,
        )

        fixed = remove(image)
        processing_text.empty()

        col2.image(fixed, caption='Processed Image')

        st.download_button(
            'Download',
            convert_image(fixed),
            'new_image.png',
            'image/png',
            type='primary',
        )
    except Exception as e:
        st.error(f'An error occurred: {e}')


def remove_background():
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

    st.markdown(
        """
        # Remove Background
        <br/>
        <br/>
        """,
        unsafe_allow_html=True,
    )

    my_upload = st.file_uploader(
        'Upload an image',
        type=['png', 'jpg', 'jpeg'],
        help='Only PNG and JPG are supported.',
    )

    st.markdown('---')

    col1, col2 = st.columns(2)

    if my_upload:
        if my_upload.size > MAX_FILE_SIZE:
            st.error(
                'The uploaded file is too large. Please upload an image smaller than 5MB.'
            )
        else:
            fix_image(upload=my_upload, col1=col1, col2=col2)
    else:
        st.error('Please upload an image.')
