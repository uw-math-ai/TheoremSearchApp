"""Retired demo — a pointer to theoremsearch.com, nothing more.

This Space was the original Streamlit search demo over the v1 corpus. Search
now lives at https://theoremsearch.com, so everything that queried the
database or the embedding provider is gone: no search, no filters, no
feedback form, no query logging, no Google Analytics.

Because nothing here talks to a backend any more, the Space needs no secrets.
NEBIUS_API_KEY, RDS_SECRET_ARN, RDS_WRITER_HOST, RDS_DB_NAME and any AWS
credentials should be deleted from its settings.
"""
import streamlit as st

NEW_URL = "https://theoremsearch.com"

st.set_page_config(page_title="Theorem Search has moved", page_icon="📚")

st.logo(
    image="images/math-ai-logo.jpg",
    size="large",
    link="https://sites.math.washington.edu/ai/",
)

st.title("Theorem Search has moved")

st.markdown(
    f"""
This demo is retired and no longer searches anything.

## → [theoremsearch.com]({NEW_URL})

The active site searches a larger corpus, including formal Lean statements,
and adds dependency graphs and richer filters.
"""
)

st.link_button("Go to theoremsearch.com", NEW_URL, type="primary")
