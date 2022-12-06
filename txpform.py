
import streamlit as st
import datetime
import psycopg2


spllunch = False
nmllunch = False
nmlbf = False
splbf = False
nmldinner = False
spldinner = False


bfsplquantity = 0
normalbfquantity = 0
speciallunchquantity = 0
normallunchquantity = 0
specialdinnerquantity = 0
normaldinnerquantity = 0

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                password="admatic123",
                                host="localhost",
                                port="5432",
                                database="postgres")
    connection.autocommit = True

    cursor = connection.cursor()
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")


except Exception as error:
    print(error)
    print("index error passing now")
    st.write("Warning : Content Not Updating Contact Admin")
   

    



# tittle
st.title('Tasty Express 247')
st.text('Customer Orders Form')

col1, col2, col3 = st.columns(3)

with col1:
    customername = st.text_input('Name', '',key='aaa')
contact = st.text_input('Delivery Contact Number', '',key='bbb')

with col2:
    location = st.selectbox('Location',('Alandur', 'Adambakkam', 'Adyar','Velacherry','Tharamani','Guindy','Guindy Industrial Estate','Ekkaduthangal','Madipakkam','Pallikaranai','Nanganallur','Madhya kailash','Thiruvanmayiur'),key='aa')

customerregularornew = st.selectbox('Customer Type',('Regular','New'),key='hh')


with col1:
    breakfast = st.checkbox('Breakfast',key='11')
    if breakfast :
        splbf = st.checkbox('Special Breakfast',key='12')
        if splbf :
                specialbreakfastoption = st.selectbox('Suscription Type',('Weekly','Montly','Occasionally','Custom'),key='bb')
                if specialbreakfastoption == 'Weekly' :
                    bfsplquantity = st.text_input('Quantity', '6',key='b') 
                elif specialbreakfastoption == 'Montly' :
                    bfsplquantity = st.text_input('Quantity', '26',key='c') 
                elif specialbreakfastoption == 'Occasionally' :
                    bfsplquantity = st.text_input('Quantity', '1',key='d') 
                elif specialbreakfastoption == 'Custom' :
                    bfsplquantity = st.text_input('Quantity', '',key='e') 

        nmlbf = st.checkbox('Normal Breakfast',key='13')
        if nmlbf :
                normalbreakfastoption = st.selectbox('Suscription Type',('Weekly','Montly','Occasionally','Custom'),key='cc')
                if normalbreakfastoption == 'Weekly' :
                    normalbfquantity = st.text_input('Quantity', '6',key='f') 
                elif normalbreakfastoption == 'Montly' :
                    normalbfquantity = st.text_input('Quantity', '26',key='g') 
                elif normalbreakfastoption == 'Occasionally' :
                    normalbfquantity = st.text_input('Quantity', '1',key='h') 
                elif normalbreakfastoption == 'Custom' :
                    normalbfquantity = st.text_input('Quantity', '',key='i') 


    lunch = st.checkbox('Lunch')
    if lunch :
        
        spllunch = st.checkbox('Special lunch',key='14')
        if spllunch :
                speciallunchoption = st.selectbox('Suscription Type',('Weekly','Montly','Occasionally','Custom'),key='dd')
                if speciallunchoption == 'Weekly' :
                    speciallunchquantity = st.text_input('Quantity', '6',key='j') 
                elif speciallunchoption == 'Montly' :
                    speciallunchquantity = st.text_input('Quantity', '26',key='k') 
                elif speciallunchoption == 'Occasionally' :
                    speciallunchquantity = st.text_input('Quantity', '1',key='l') 
                elif speciallunchoption == 'Custom' :
                    speciallunchquantity = st.text_input('Quantity', '',key='m')

        nmllunch = st.checkbox('Normal lunch',key='15')
        if nmllunch :
                normallunchoption = st.selectbox('Suscription Type',('Weekly','Montly','Occasionally','Custom'),key='ee')
                if normallunchoption == 'Weekly' :
                    normallunchquantity = st.text_input('Quantity', '6',key='n') 
                elif normallunchoption == 'Montly' :
                    normallunchquantity = st.text_input('Quantity', '26',key='o') 
                elif normallunchoption == 'Occasionally' :
                    normallunchquantity = st.text_input('Quantity', '1',key='p') 
                elif normallunchoption == 'Custom' :
                    normallunchquantity = st.text_input('Quantity', '',key='q') 


    dinner = st.checkbox('Dinner')
    if dinner :
        spldinner = st.checkbox('Special dinner',key='16')
        if spldinner :
                specialdinneroption = st.selectbox('Suscription Type',('Weekly','Montly','Occasionally','Custom'),key='ff')
                if specialdinneroption == 'Weekly' :
                    specialdinnerquantity = st.text_input('Quantity', '6',key='r') 
                elif specialdinneroption == 'Montly' :
                    specialdinnerquantity = st.text_input('Quantity', '26',key='s') 
                elif specialdinneroption == 'Occasionally' :
                    sploccasionallyquantity = st.text_input('Quantity', '1',key='t') 
                elif specialdinneroption == 'Custom' :
                    splcustomquantity = st.text_input('Quantity', '',key='u')

        nmldinner = st.checkbox('Normal dinner',key='17')
        if nmldinner :
                normaldinneroption = st.selectbox('Suscription Type',('Weekly','Montly','Occasionally','Custom'),key='gg')
                if normaldinneroption == 'Weekly' :
                    normaldinnerquantity = st.text_input('Quantity', '6',key='v') 
                elif normaldinneroption == 'Montly' :
                    normaldinnerquantity = st.text_input('Quantity', '26',key='w') 
                elif normaldinneroption == 'Occasionally' :
                    normaldinnerquantity = st.text_input('Quantity', '1',key='x') 
                elif normaldinneroption == 'Custom' :
                    normaldinnerquantity = st.text_input('Quantity', '',key='y') 


# using now() to get current time
current_time = datetime.datetime.now()
     
# # Printing attributes of now().
# print ("The attributes of now() are : ")
     
# print ("Year: ", end = "")
# print (current_time.year)
     
# print ("Month: ", end = "")
# print (current_time.month)
     
# print ("Day: ", end = "")
# print (current_time.day)




d = st.date_input(
    "Delivery Start Date",
    datetime.date(current_time.year, current_time.month, current_time.day))
st.write('Delivery Start Date is:', d)


deliveryaddress = st.text_input('Delivery Address and Landmark', '',key='ccc')
googlelocation = st.text_input('Google Location Link', '',key='ddd')

if st.button('CONFIRM ORDER'):
    if breakfast or lunch or dinner == True :
        # if nmldinner or spldinner or nmllunch or spllunch or nmlbf or splbf == True :
            if len(str(customername))>= 3 :
                print(len(str(contact)))
                if len(str(contact)) > 8 :
                    try:
            #             cursor.execute(f"""INSERT INTO public.customer_data(
	        #           "Name", "Location", breakfast, lunch, dinner, special_breakfast, normal_breakfast, special_lunch, normal_lunch, special_dinner, normal_dinner, delivery_contact_number, customer_type, delivery_date, delivery_address, google_location,order_value)
	        #   VALUES ('{customername}', '{location}', '{breakfast}', '{lunch}', '{dinner}', '{splbf}', '{nmlbf}', '{spllunch}', '{nmllunch}', '{spldinner}', '{nmldinner}', '{contact}', '{customerregularornew}', '{d}','{deliveryaddress}', '{googlelocation}', NULL);""")
                        cursor.execute(f"""INSERT INTO public.customer_data(
	                   "Name", "Location", breakfast, lunch, dinner, special_breakfast, special_breakfast_quantity, normal_breakfast, normal_breakfast_quantity, special_lunch, special_lunch_quantity, normal_lunch, normal_lunch_quantity, special_dinner, special_dinner_quantity, normal_dinner, normal_dinner_quantity, delivery_contact_number, customer_type, delivery_date, delivery_address, google_location, order_value)
	VALUES ('{customername}', '{location}', '{breakfast}', '{lunch}', '{dinner}', '{splbf}','{bfsplquantity}', '{nmlbf}','{normalbfquantity}', '{spllunch}', '{speciallunchquantity}','{nmllunch}','{normallunchquantity}', '{spldinner}', '{specialdinnerquantity}'       ,'{nmldinner}', '{normaldinnerquantity}','{contact}', '{customerregularornew}', '{d}','{deliveryaddress}', '{googlelocation}', NULl);""")
                    
                    
                    
                    except Exception as error1 :
                        print("db update failure")
                        print(error1)

                    st.write('Order Placed Successfully')
                else :
                    st.write('Please Check Contact Number')
            else :
                st.write('Please Check Name minimum 3 letters Required')
        # else :
        #         st.write('Please select Normal or Special Categories')
  
    else :
        st.write('Please Select Breakfast or Lunch or Dinner')
        
else:   
    st.write('Fill all the Important Fields and Press Submit ')