import uuid
import logging

import pandas as pd
import streamlit as st

from ..services.deta_service import DetaService

logger = logging.getLogger(__name__)


class DetaModel:
    df: pd.DataFrame = None


class DetaView:
    title = "Deta Service"

    df = DetaModel().df

    __key1: str = str(uuid.uuid1())
    __key2: str = str(uuid.uuid1())
    __key3: str = str(uuid.uuid1())
    __key4: str = str(uuid.uuid1())
    __key5: str = str(uuid.uuid1())
    __key6: str = str(uuid.uuid1())

    def main(self, project_key: str, db_name: str):
        st.title(self.title)

        self.deta_service = DetaService(
            project_key=project_key, db_name=db_name)

        if st.button(label='Fetch') or True:
            self.fetch()

        cols = st.columns(3)

        with cols[0]:
            with st.expander(label='Create', expanded=True):
                name: str = st.text_input(key=self.__key1, label='name')
                age: str = st.selectbox(
                    key=self.__key2, label='age', options=[
                        27, 28, 29])
                hometown: str = st.text_input(
                    key=self.__key3, label='hometown')

                if name and age and hometown and st.button(label='Create'):
                    result = self.deta_service.create(
                        name=name, age=age, hometown=hometown)
                    if result:
                        st.json(result)

        with cols[1]:
            with st.expander(label='Update', expanded=True):
                _key: str = st.selectbox(
                    label='Select Update Key', options=self.df.key)

                name: str = st.text_input(
                    key=self.__key4,
                    label='name',
                    value=self.df.query(f'key == "{_key}"').name.values[0])
                age: str = st.selectbox(
                    key=self.__key5, label='age', options=[
                        27, 28, 29], index=1)
                hometown: str = st.text_input(
                    key=self.__key6,
                    label='hometown',
                    value=self.df.query(f'key == "{_key}"').hometown.values[0])
                if name and age and hometown and st.button(label='Update'):
                    result = self.deta_service.update(
                        dict(name=name, age=age, hometown=hometown), key=_key)
                    if result:
                        st.json(result)

        with cols[2]:
            with st.expander(label='Delete', expanded=True):
                if self.df is not None:
                    _key: str = st.selectbox(
                        key='', label='Select Delete Key', options=self.df.key)

                    if _key and st.button(label='Delete item'):
                        result = self.deta_service.delete(key=_key)
                        if result:
                            st.table(result)

        with st.expander(label='Fetch', expanded=True):
            result = self.fetch()
            if self.df is not None or result:
                st.table(self.df)

    def fetch(self):
        result = self.deta_service.fetch()
        if result:
            self.df = pd.DataFrame(result.items)[
                ['key', 'name', 'age', 'hometown']]
        return result
