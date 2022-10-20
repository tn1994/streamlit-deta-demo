import logging

import streamlit as st

from applications.views.sidebar import Sidebar

logger = logging.getLogger(__name__)


class APP:
    st.set_page_config(
        page_title='tn1994/streamlit-template',
        layout='wide'
    )

    @staticmethod
    def main():
        sidebar = Sidebar()
        sidebar.main()


def main():
    app = APP()
    app.main()


if __name__ == '__main__':
    main()
