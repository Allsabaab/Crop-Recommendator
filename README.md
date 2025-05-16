# Crop-Recommendator

## Project Overview:

This project is a "Crop Recommendation System" built using Python. The system helps farmers or agricultural enthusiasts determine the best crops to grow in a specific location based on two key factors:

1. **Soil pH level**: The acidity or alkalinity of the soil.
2. **Nitrogen level**: The nitrogen content of the soil, which is crucial for plant growth.

Additionally, it considers the suitability of crops for a specific district, making it a location-specific recommendation system.

## Project Workflow:

1. **User Input Collection:**
   - The system asks the user for the soil pH value.
   - The user is prompted to choose the Nitrogen level (High, Medium, or Low).
   - The user is asked to enter their district name.

2. **Crop Data Loading (Crops.txt):**
   - The `crop_data()` function reads the `Crops.txt` file.
   - Each line in the file contains the following data for a crop:
     - **Crop Name**
     - **Minimum pH Value**
     - **Maximum pH Value**
     - **Required Nitrogen Level (High, Medium, or Low)**
   - This data is stored in a dictionary format for easy access.

3. **Crop Recommendation Based on Soil Data (`recommend1`):**
   - The function `recommend1()` takes the crop dictionary, soil pH, and nitrogen level as input.
   - It filters the crops based on the input pH and nitrogen level.
   - Suitable crops are listed and stored in a list for further filtering.

4. **District-Based Filtering (Districts.txt):**
   - The `recommend2()` function reads the `Districts.txt` file.
   - Each line in the file contains:
     - **District Name**
     - **List of Crops suitable for that district**
   - The user’s district is checked against the list, and suitable crops for that district are identified.
   - Finally, the system provides:
     - All suitable crops for that district.
     - The best suitable crops (from the initial list) for the user's land.
