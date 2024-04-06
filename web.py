import streamlit as s
s.set_page_config(page_title="super")
s.header("My 1st Website")
s.write("""
# HELLO 
this is my 
**first**
 *website*""")
s.subheader("MY DETAILS")
s.markdown("I AM MUTHU RANJAN 19 YEARS OLD MALE , I AM STUDYING IN AI & DS DEPARTMENT IN KEC")
s.markdown("_A subject called MACHINE LEARNING contains equations like_")
s.latex("y=mx+c")
s.caption("this is the linear equation")
s.text("_check_")
s.code("""import pandas
pandas.DataFrame()""")
submit=s.button("click")
#we use radio in button it refresh because wwe didn't defint any state
box=s.checkbox("press")
if box:
    s.text("welcome")
    s.radio("select gender:",{"male","female","transgender"})
c1,c2=s.columns(2)
with c1:
    a=s.number_input("Enter a number 1:")
with c2:
    b=s.number_input("Enter a number 2:")
submit1=s.button("Add")
if submit1 :
    s.write("the sum is ",a+b)
s.write("___")
col1,col2=s.columns(2)
with col1:
    sl1=s.slider("choose no 1:",0,10)
with col2:
    sl2=s.slider("choose no 2:",0,20)
box2=s.checkbox("sub")
if box2:
    s.write("the difference is:",sl1-sl2)
s.write("___")
