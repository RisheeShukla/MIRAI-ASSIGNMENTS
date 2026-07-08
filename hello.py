import streamlit as st

st.title('👤  :rainbow[My Profile]')
st.write('Enter the name and message you want to send to the system. The system will respond with a confirmation message and an estimate of the number of tokens your message will consume from the context window.')
name=st.text_input('Enter your name')
message=st.text_area('Enter your message')

if st.button('Submit'):
    if name and message:
        st.success(f'Transmission successful! Greetings, :rainbow[{name}]. We received your message: :rainbow[{message}]')
        count=len(message)
        st.info(f'System Check: Your message will consume approximately :rainbow[{count/4}] tokens from our context window.')
    elif not name:
        st.error('Please enter your name.') 
    elif not message:
        st.warning('Please enter your message.')
    else :
        st.error('Please enter your name and message.')

