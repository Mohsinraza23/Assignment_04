import streamlit as st
import requests

def fetch_country_data(country_name):
    url = f'https://restcountries.com/v3.1/name/{country_name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            country_data = data[0]
            name = country_data.get("name", {}).get("common", "N/A")
            capital = country_data.get("capital", ["N/A"])[0]
            population = country_data.get("population", "N/A")
            area = country_data.get("area", "N/A")
            currencies = country_data.get("currencies", {})
            currency_list = [f"{val.get('name')} ({code})" for code, val in currencies.items()]
            currency_str = ", ".join(currency_list) if currency_list else "N/A"
            region = country_data.get("region", "N/A")
            
            return name, capital, population, area, currency_str, region
    return None

def main():
    st.title("Country Information App")
    country_name = st.text_input("Enter a country name:")
    
    if country_name:
        country_info = fetch_country_data(country_name)
        if country_info:
            name, capital, population, area, currency, region = country_info
            
            st.subheader("Country Info")
            st.write(f'**Name:** {name}')
            st.write(f'**Capital:** {capital}')
            st.write(f'**Population:** {population}')
            st.write(f'**Area:** {area} square kilometers')
            st.write(f'**Currency:** {currency}')
            st.write(f'**Region:** {region}')
        else:
            st.error("Error: Country data not found")

if __name__ == "__main__":
    main()