import streamlit
import pandas
import snowflake.connector
from  urllib.error import URLError
import requests
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard_Boiled Free-Range Egg')
streamlit.text('🥑🍞 Hard_Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index) ,['Avocado' , 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected] 
# Display the table on the page.
streamlit.dataframe( fruits_to_show)                        #my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")
try:
      fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
      if not fruit_choice :  
             streamlit.error()
      else :
             fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")
             fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
             # write your own comment - what does this do?
             streamlit.dataframe(fruityvice_normalized)
      # streamlit.write('The user entered ', fruit_choice)

except :
       streamlit.error("Please select a fruit to get Information")



# streamlit.text(fruityvice_response)
# write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized)
streamlit.stop()
#### snowflake connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
fruit_choice = streamlit.text_input('What fruit would you like to add?','Jackfruit')


streamlit.write(f'Thamsk for adding {fruit_choice}')
my_cur.execute("insert into fruit_load_list values('from streamlit') ")
