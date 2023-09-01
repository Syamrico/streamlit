import streamlit as st
from datetime import datetime
import pandas as pd

st.write("buku tulis 1")
st.markdown("buku tulis 2")
st.title("buku tulis 3")
st.header("buku tulis 4")
st.subheader("buku tulis 5")
st.caption("buku tulis 6")
st.code("buku tulis 7")
st.text("buku tulis 8")
st.latex("buku tulis 9X^2")
st.divider()



data_df = pd.DataFrame(
    {
        "apps": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.ImageColumn(
            "Preview Image", width="large", help="Streamlit app preview screenshots"
        )
    },
    hide_index=True,
)
