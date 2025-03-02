import streamlit as st
import pandas as pd

# Converter Functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1,
        'Kilometers': 1000,
        'Centimeters': 0.01,
        'Millimeters': 0.001,
        'Miles': 1609.34,
        'Yards': 0.9144,
        'Feet': 0.3048,
        'Inches': 0.0254
    }
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1,
        'Grams': 0.001,
        'Pounds': 0.453592,
        'Ounces': 0.0283495,
        'Metric Tons': 1000
    }
    kilograms = value * weight_units[from_unit]
    return kilograms / weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return ((value - 32) * 5/9) + 273.15
        return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return ((value - 273.15) * 9/5) + 32
        return value

def volume_converter(value, from_unit, to_unit):
    volume_units = {
        'Liters': 1,
        'Milliliters': 0.001,
        'Cubic Meters': 1000,
        'Gallons (US)': 3.78541,
        'Fluid Ounces (US)': 0.0295735,
        'Cups (US)': 0.236588
    }
    liters = value * volume_units[from_unit]
    return liters / volume_units[to_unit]

def time_converter(value, from_unit, to_unit):
    time_units = {
        'Seconds': 1,
        'Minutes': 60,
        'Hours': 3600,
        'Days': 86400,
        'Weeks': 604800,
        'Months': 2592000,
        'Years': 31536000
    }
    seconds = value * time_units[from_unit]
    return seconds / time_units[to_unit]

def main():
    st.set_page_config(
        page_title="Professional Unit Converter",
        page_icon="🔄",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS
    st.markdown("""
        <style>
        .main-title {
            background: linear-gradient(45deg, #2193b0, #6dd5ed);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .subtitle {
            color: #666;
            text-align: center;
            font-style: italic;
            margin-bottom: 30px;
        }
        .result-container {
            background: linear-gradient(to right, #f8f9fa, #e9ecef);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            text-align: center;
        }
        .result-text {
            font-size: 24px;
            font-weight: bold;
            color: #2193b0;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
        <div class="main-title">
            <h1>🔄 Professional Unit Converter</h1>
            <p style="font-size: 1.2em; margin-top: 10px;">Convert any unit with precision and ease</p>
        </div>
        <div class="subtitle">
            Accurate conversions for Length, Weight, Temperature, Volume, and Time
        </div>
    """, unsafe_allow_html=True)
    
    # Conversion type selection
    conversion_types = {
        "Length 📏": ("length", length_converter),
        "Weight ⚖️": ("weight", weight_converter),
        "Temperature 🌡️": ("temperature", temperature_converter),
        "Volume 🧊": ("volume", volume_converter),
        "Time ⏰": ("time", time_converter)
    }
    
    conversion_type = st.selectbox(
        "Select Conversion Type",
        list(conversion_types.keys())
    )
    
    # Units dictionary
    units = {
        "length": ['Meters', 'Kilometers', 'Centimeters', 'Millimeters', 'Miles', 'Yards', 'Feet', 'Inches'],
        "weight": ['Kilograms', 'Grams', 'Pounds', 'Ounces', 'Metric Tons'],
        "temperature": ['Celsius', 'Fahrenheit', 'Kelvin'],
        "volume": ['Liters', 'Milliliters', 'Cubic Meters', 'Gallons (US)', 'Fluid Ounces (US)', 'Cups (US)'],
        "time": ['Seconds', 'Minutes', 'Hours', 'Days', 'Weeks', 'Months', 'Years']
    }
    
    current_type, converter_func = conversion_types[conversion_type]
    current_units = units[current_type]
    
    # Input columns
    col1, col2, col3 = st.columns([2, 2, 2])
    
    with col1:
        st.markdown("<h3 style='text-align: center; color: #2193b0;'>Enter Value</h3>", unsafe_allow_html=True)
        value = st.number_input("", value=1.0, format="%.8f")
        
    with col2:
        st.markdown("<h3 style='text-align: center; color: #2193b0;'>From</h3>", unsafe_allow_html=True)
        from_unit = st.selectbox("From Unit", current_units, key="from")
        
    with col3:
        st.markdown("<h3 style='text-align: center; color: #2193b0;'>To</h3>", unsafe_allow_html=True)
        to_unit = st.selectbox("To Unit", current_units, key="to")
    
    # Calculate and display result
    try:
        result = converter_func(value, from_unit, to_unit)
        
        st.markdown(f"""
            <div class="result-container">
                <h3 style='margin-bottom: 20px;'>Conversion Result</h3>
                <div class="result-text">
                    {value:.8f} {from_unit} = {result:.8f} {to_unit}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Conversion Table
        if st.button("📊 Show Conversion Table"):
            st.markdown("<h3 style='text-align: center; color: #2193b0;'>Quick Reference Table</h3>", unsafe_allow_html=True)
            values = [0.1, 1, 10, 100, 1000]
            data = []
            for val in values:
                converted = converter_func(val, from_unit, to_unit)
                data.append([f"{val:,.2f} {from_unit}", f"{converted:,.2f} {to_unit}"])
            df = pd.DataFrame(data, columns=["Original Value", "Converted Value"])
            st.table(df)
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        
    # Help Section
    with st.expander("💡 Need Help?"):
        st.markdown("""
            ### How to use this Professional Unit Converter:
            1. **Select Conversion Type**: Choose from Length, Weight, Temperature, Volume, or Time
            2. **Enter Value**: Input the number you want to convert
            3. **Choose Units**: Select your source and target units
            4. **View Results**: See your conversion result instantly
            5. **Extra Features**: 
                - View the quick reference table for common values
                - Get precise results up to 8 decimal places
                - Easy-to-use interface with visual guidance
        """)

if __name__ == '__main__':
    main() 