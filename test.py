import streamlit as st
import folium

def main():
    st.title("Map with Coordinates")

    # Input coordinates
    lat = st.number_input("Enter latitude:", min_value=-90.0, max_value=90.0)
    lon = st.number_input("Enter longitude:", min_value=-180.0, max_value=180.0)

    # Create a Folium map centered around the input coordinates
    m = folium.Map(location=[lat, lon], zoom_start=12)

    # Add a marker at the specified coordinates
    folium.Marker([lat, lon]).add_to(m)

    # Display the map in Streamlit
    folium_static(m)

if __name__ == "__main__":
    main()
