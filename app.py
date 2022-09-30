import streamlit as st
import awesome_streamlit as ast
import web.src.pages.home
import web.src.pages.predition
import web.src.pages.insights
import web.src.pages.data

ast.core.services.other.set_logging_format()

# create the choices
PAGES = {
    "Home": web.src.pages.home,
    "Data":web.src.pages.data,
    "Insights": web.src.pages.insights,
    "Run Predictions": web.src.pages.predition
}

# render the pages
def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

#     st.sidebar.title("About")
#     st.sidebar.info(
#         """
#         This App is an end-to-end product that enables the Rosemann pharmaceutical company to 
#         view predictions on sales across their stores and 6 weeks ahead of time and the trends expected.
# """
#     )

# run it
if __name__ == "__main__":
    main()