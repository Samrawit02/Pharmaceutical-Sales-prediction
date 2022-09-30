
import streamlit as st
import awesome_streamlit as ast


def write():
    """Used to write the page in the app.py file"""
    st.title('Insights from the give data')

    st.write('---')
    st.markdown('## Time Series Per StoreType ')
    st.image("web/src/images/timeseriesperstoretype.png")
    st.write('The most selling and crowded store type is b.')

    st.write('---')
    st.markdown('## Over All Sales Trend')
    st.image("web/src/images/overAllSalesTrend.png")
    st.write("""as we can see in the above plot, sales increase starting from Feburary to may  and drops from May To September,  And has high rate increase from September to December.
    'The Highest sales is in December and the lowest sale are in September.""")

    st.write('---')
    st.markdown('## Promotion Impact On Customer Per Storetype ')
    st.image("web/src/images/promotionImpactOnCustomersPerStoretype.png")
    st.write('The customer number increase with the promotion ')

    st.write('---')
    st.markdown('## Promotion Impact On Sales Per Storetype ')
    st.image("web/src/images/promotionImpactOnSalesPerStoretype.png")
    st.write("Sales increase significatly when the store has a promotion")

    st.write('---')
    st.markdown('## Correlation Analysis')
    st.image("web/src/images/correlation.png")
    st.write('As we can see sales is highly correlated to customers.')

    st.write('---')
    st.markdown('## Sales And Customers Across Days of the Week')
    st.image("web/src/images/SalesAndCustomerVsdaysOfWeek.png")

    st.write('---')
    st.markdown('## Average Daily Customer for 3 Years')
    st.image("web/src/images/averageDailyCustomersfor3years.png")
  
    st.write('---')
    st.markdown('## Average Daily Sales for 3 Years')
    st.image("web/src/images/averageMonthlySalesfor3years.png")
  

   
