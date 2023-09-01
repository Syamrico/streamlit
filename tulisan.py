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
            "https://github.com/Syamrico/streamlit/blob/bunga/tere3.jpeg",
            "https://github.com/Syamrico/streamlit/blob/bunga/tere3.jpeg",
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

# Cache the dataframe so it's only loaded once
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "KOLOM PERTAMA": [1, 2, 3, 4],
            "KOLOM KEDUA": [10, 20, 30, 40],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()
st.dataframe(df, use_container_width=st.session_state.use_container_width)


df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
