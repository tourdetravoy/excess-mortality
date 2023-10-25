import streamlit as st
import inspect
import textwrap
import pandas as pd
import altair as alt

st.set_page_config(layout="wide", page_title="Excess Mortality", page_icon="📊", initial_sidebar_state="collapsed")
st.markdown("# Excess Mortality 2020 - 2023")
st.write(
"""(Data courtesy of the [Economist](https://github.com/TheEconomist/covid-19-excess-deaths-tracker).)"""
)

def data_frame():
    @st.cache_data
    def get_excess_weekly_data():
        df = pd.read_csv("https://github.com/TheEconomist/covid-19-excess-deaths-tracker/raw/master/output-data/excess-deaths/all_weekly_excess_deaths.csv")
        return df.set_index("country")

    try:
        df = get_excess_weekly_data()
        countries = st.multiselect(
            "Choose country", list(df.index.unique()), ["Ireland"]
        )
        if not countries:
            st.error("Please select at least one Country.")

        else:
            data2 = df.loc[countries]

            # Body
            st.title('Excess Mortality 2023')

            df23 = data2[(data2['year']==2023)]

            bar_chart_23 = alt.Chart(df23).mark_bar().encode(
            x="week:O",
            y=alt.Y("excess_deaths:Q"),
            tooltip=['week', 'end_date', 'total_deaths', 'expected_deaths', 'excess_deaths', 'excess_deaths_pct_change*100'],).properties(
                width=1200,
                height=600
            ).interactive()

            st.altair_chart(bar_chart_23)

            # Body
            st.title('Excess Mortality 2022')

            df22 = data2[(data2['year']==2022)]

            bar_chart_22 = alt.Chart(df22).mark_bar().encode(
            x="week:O",
            y=alt.Y("excess_deaths:Q"),
            tooltip=['week', 'end_date', 'total_deaths', 'expected_deaths', 'excess_deaths'],).properties(
                width=1200,
                height=600
            ).interactive()

            st.altair_chart(bar_chart_22)

            # Body
            st.title('Excess Mortality 2021')

            df21 = data2[(data2['year']==2021)]

            bar_chart_21 = alt.Chart(df21).mark_bar().encode(
            x="week:O",
            y=alt.Y("excess_deaths:Q"),
            tooltip=['week', 'end_date', 'total_deaths', 'expected_deaths', 'excess_deaths'],).properties(
                width=1200,
                height=600
            ).interactive()

            st.altair_chart(bar_chart_21)

            # Body
            st.title('Excess Mortality 2020')

            df20 = data2[(data2['year']==2020)]

            bar_chart_20 = alt.Chart(df20).mark_bar().encode(
            x="week:O",
            y=alt.Y("excess_deaths:Q"),
            tooltip=['week', 'end_date', 'total_deaths', 'expected_deaths', 'excess_deaths'],).properties(
                width=1200,
                height=600
            ).interactive()

            st.altair_chart(bar_chart_20)

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

data_frame()
