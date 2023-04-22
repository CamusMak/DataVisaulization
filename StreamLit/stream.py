# # import module
import streamlit as st

st.title("Welcome to BMI Calculator")


weight = st.number_input("Weight",min_value=0) 

answer = st.radio("Selecet height format",['cm','meters','feet']) 


height = st.number_input("Height",min_value=1)

    


if answer == 'cm':
    height = height/100
elif answer == "feet":
    height = height/3.28

but = st.button("Calculate")

BMI = 0

if height != 0:

    BMI = weight/height**2


if but:
    st.write("Your BMI index is ",BMI)
    if BMI != 0:
        

        if BMI <= 16:
            st.write("Your are extrimely underweighted!!!")
        elif BMI < 18.5:
            st.write("Your are in underweight range!!!")
        elif BMI < 25:
            st.markdown("You are in healty weight range!!:red")
        elif BMI < 30:
            st.write("Your are in overweight range!!!")
        else:
            st.write("Your are done!!!")

        if BMI<=18.5:
            best_weight = round(18.5*height**2,2)

            st.spinner("To be in healty weight range, your weight should be at least ",best_weight,"kg!!")
        elif BMI > 25:
            best_weight = round(25*height**2,2)
            st.write("To be in healty weight range, your weight should be maximum ",best_weight, "kg!!!")

            



