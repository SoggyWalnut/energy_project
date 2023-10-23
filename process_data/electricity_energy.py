import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib settings
sns.set_style('whitegrid')
plt.rcParams["patch.force_edgecolor"]= True

# Read CSV cleaned data file
df = pd.read_csv("../output/cleaned_energy_data.csv", low_memory=False)
# Drop mostly empty column
df.drop(['quantity_footnotes'], axis=1,inplace=True)

# List of EU countries will be used in the code
EU_countries = ['France', 'Germany', 'Italy', 'Netherlands', 'Norway', 'Poland', 'Spain', 'Sweden', 'Switzerland', 'Turkey']

# Data frames of related countries
US = df[df['country_or_area'].isin(["United States"])].sort_values('year')
CAN = df[df['country_or_area'].isin(["Canada"])].sort_values('year')
CHI = df[df['country_or_area'].isin(["China"])].sort_values('year')
IND = df[df['country_or_area'].isin(['India'])].sort_values('year')
UK = df[df['country_or_area'].isin(['United Kingdom'])].sort_values('year')

VN_df = df[df['country_or_area'].isin(['Viet Nam'])].sort_values('year')
# Write VN energy data to csv file
VN_df.to_csv('../output/vn_energy_data.csv',encoding='utf-8', index=False, lineterminator='\n')

def extract_eu_dataframes(energy_type):
    if (energy_type == 'wind'):
        end_name = '_Wind'
        category = 'wind_electricity'
    elif (energy_type == 'solar'):
        end_name = '_Solar'
        category = 'solar_electricity'
    elif (energy_type == 'nuclear'):
        end_name = '_Nuclear'
        category = 'nuclear_electricity'
    elif (energy_type == 'hydro'):
        end_name = '_Hydro'
        category = 'hydro' 

    index = 0
    for eu_country in EU_countries: 
        country_name = eu_country
        energy_df_name = eu_country + end_name
        country_name = df[df['country_or_area'].isin([eu_country])].sort_values('year')
        energy_df_name = country_name[country_name['category'] == category].sort_values("year")
        if index == 0:
            EU_energy = energy_df_name
        else:
            EU_energy = pd.concat([EU_energy,energy_df_name])
        index +=1 
    return EU_energy

# Function to extract and visualize wind energy
def wind_energy():
    # Filter to only wind electricity data frame
    US_Wind = US[US['category'] == "wind_electricity"].sort_values("year")
    CAN_Wind = CAN[CAN['category'] == "wind_electricity"].sort_values("year")
    CHI_Wind = CHI[CHI['category'] == "wind_electricity"].sort_values("year")
    IND_Wind = IND[IND['category'] == "wind_electricity"].sort_values("year")
    UK_Wind = UK[UK['category'] == "wind_electricity"].sort_values("year")
    VN_Wind = VN_df[VN_df['category'] == "wind_electricity"].sort_values("year")
    EU_Wind = extract_eu_dataframes('wind')

    # Initialize data for graph
    y0 = US_Wind.quantity
    x0 = US_Wind.year
    y2 = CAN_Wind.quantity
    x2 = CAN_Wind.year
    y3 = CHI_Wind.quantity
    x3 = CHI_Wind.year
    y4 = IND_Wind.quantity
    x4 = IND_Wind.year
    y6 = UK_Wind.quantity
    x6 = UK_Wind.year
    y7 = EU_Wind[EU_Wind['country_or_area'] == 'Germany'].quantity
    x7 = EU_Wind[EU_Wind['country_or_area'] == 'Germany'].year
    y8 = EU_Wind[EU_Wind['country_or_area'] == 'France'].quantity
    x8 = EU_Wind[EU_Wind['country_or_area'] == 'France'].year
    y9 = EU_Wind[EU_Wind['country_or_area'] == 'Italy'].quantity
    x9 = EU_Wind[EU_Wind['country_or_area'] == 'Italy'].year
    y10 = VN_Wind.quantity
    x10 = VN_Wind.year

    # Initialize graph
    f = plt.figure(figsize=(15,10))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.plot(x0,y0,label="USA")
    plt.plot(x2,y2,'y',label="Canada")
    plt.plot(x3,y3,'k',label="China")
    plt.plot(x4,y4,'g',label="India")
    plt.plot(x6,y6,'m',label="UK")
    plt.plot(x7,y7,'crimson',label="Germany", linestyle = 'dashed')
    plt.plot(x8,y8,'navy',label="France", linestyle = 'dashed')
    plt.plot(x9,y9,'darkgoldenrod',label="Italy", linestyle = 'dashed')
    plt.plot(x10,y10,'k',label="Viet Nam", linestyle = 'dashed')

    plt.legend(fontsize=16)
    plt.ylabel("Millions of Kilowatts-Hour",fontsize=20)
    plt.xlabel('Year',fontsize=20)
    plt.title('Total Wind Production',fontsize=24)
    plt.xlim(1990, 2014.2)
    plt.show()

    # Save figure as png file
    f.savefig("../output/images/result_wind.png", bbox_inches='tight')

    # Concat into wind-only dataframe from all of the countries
    wind_df = pd.concat([EU_Wind, US_Wind, CAN_Wind, CHI_Wind, IND_Wind, UK_Wind, VN_Wind])
    # Write all wind data to a csv file
    wind_df.to_csv('../output/wind_energy_data.csv',encoding='utf-8', index=False, lineterminator='\n')

    return wind_df

# Function to extract and visualize solar energy
def solar_energy():
    # Filter to only solar electricity data frame
    US_Solar = US[US['category'] == "solar_electricity"].sort_values("year")
    CAN_Solar = CAN[CAN['category'] == "solar_electricity"].sort_values("year")
    CHI_Solar = CHI[CHI['category'] == "solar_electricity"].sort_values("year")
    IND_Solar = IND[IND['category'] == "solar_electricity"].sort_values("year")
    UK_Solar = UK[UK['category'] == "solar_electricity"].sort_values("year")
    EU_Solar = extract_eu_dataframes('solar')

    # Initialize data for graph
    y0 = US_Solar.quantity
    x0 = US_Solar.year
    y2 = CAN_Solar.quantity
    x2 = CAN_Solar.year
    y3 = CHI_Solar.quantity
    x3 = CHI_Solar.year
    y4 = IND_Solar.quantity
    x4 = IND_Solar.year
    y6 = UK_Solar.quantity
    x6 = UK_Solar.year
    y7 = EU_Solar[EU_Solar['country_or_area'] == 'Germany'].quantity
    x7 = EU_Solar[EU_Solar['country_or_area'] == 'Germany'].year
    y8 = EU_Solar[EU_Solar['country_or_area'] == 'France'].quantity
    x8 = EU_Solar[EU_Solar['country_or_area'] == 'France'].year
    y9 = EU_Solar[EU_Solar['country_or_area'] == 'Italy'].quantity
    x9 = EU_Solar[EU_Solar['country_or_area'] == 'Italy'].year

    # Initialize graph
    f = plt.figure(figsize=(15,10))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.plot(x0,y0,label="USA")
    plt.plot(x2,y2,'y',label="Canada")
    plt.plot(x3,y3,'k',label="China")
    plt.plot(x4,y4,'g',label="India")
    plt.plot(x6,y6,'m',label="UK")
    plt.plot(x7,y7,'crimson',label="Germany", linestyle = 'dashed')
    plt.plot(x8,y8,'navy',label="France", linestyle = 'dashed')
    plt.plot(x9,y9,'darkgoldenrod',label="Italy", linestyle = 'dashed')

    plt.legend(fontsize=16)
    plt.ylabel("Millions of Kilowatts-Hour",fontsize=20)
    plt.xlabel('Year',fontsize=20)
    plt.title('Total Solar Production',fontsize=24)
    plt.xlim(1990, 2014.2)
    plt.show()

    # Save figure as png file
    f.savefig("../output/images/result_solar.png", bbox_inches='tight')

    # Concat into solar-only dataframe from all of the countries
    solar_df = pd.concat([US_Solar, CAN_Solar, CHI_Solar, IND_Solar, UK_Solar, EU_Solar])
    # Write all solar data to a csv file
    solar_df.to_csv('../output/solar_energy_data.csv',encoding='utf-8', index=False, lineterminator='\n')

    return solar_df

# Function to extract and visualize nuclear energy
def nuclear_energy():
    # Filter to only nuclear electricity data frame
    US_Nuclear = US[US['category'] == "nuclear_electricity"].sort_values("year")
    CAN_Nuclear = CAN[CAN['category'] == "nuclear_electricity"].sort_values("year")
    CHI_Nuclear = CHI[CHI['category'] == "nuclear_electricity"].sort_values("year")
    IND_Nuclear = IND[IND['category'] == "nuclear_electricity"].sort_values("year")
    UK_Nuclear = UK[UK['category'] == "nuclear_electricity"].sort_values("year")
    EU_Nuclear = extract_eu_dataframes('nuclear')

    # Initialize data for graph
    y0 = US_Nuclear.quantity
    x0 = US_Nuclear.year
    y2 = CAN_Nuclear.quantity
    x2 = CAN_Nuclear.year
    y3 = CHI_Nuclear.quantity
    x3 = CHI_Nuclear.year
    y4 = IND_Nuclear.quantity
    x4 = IND_Nuclear.year
    y6 = UK_Nuclear.quantity
    x6 = UK_Nuclear.year
    y7 = EU_Nuclear[EU_Nuclear['country_or_area'] == 'Germany'].quantity
    x7 = EU_Nuclear[EU_Nuclear['country_or_area'] == 'Germany'].year
    y8 = EU_Nuclear[EU_Nuclear['country_or_area'] == 'France'].quantity
    x8 = EU_Nuclear[EU_Nuclear['country_or_area'] == 'France'].year
    y9 = EU_Nuclear[EU_Nuclear['country_or_area'] == 'Italy'].quantity
    x9 = EU_Nuclear[EU_Nuclear['country_or_area'] == 'Italy'].year

    # Initialize graph
    f = plt.figure(figsize=(15,10))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.plot(x0,y0,label="USA")
    plt.plot(x2,y2,'y',label="Canada")
    plt.plot(x3,y3,'k',label="China")
    plt.plot(x4,y4,'g',label="India")
    plt.plot(x6,y6,'m',label="UK")
    plt.plot(x7,y7,'crimson',label="Germany", linestyle = 'dashed')
    plt.plot(x8,y8,'navy',label="France", linestyle = 'dashed')
    plt.plot(x9,y9,'darkgoldenrod',label="Italy", linestyle = 'dashed')

    plt.legend(fontsize=16)
    plt.ylabel("Millions of Kilowatts-Hour",fontsize=20)
    plt.xlabel('Year',fontsize=20)
    plt.title('Total Nuclear Production',fontsize=24)
    plt.xlim(1990, 2014.2)
    plt.show()
    
    # Save figure as png file
    f.savefig("../output/images/result_nuclear.png", bbox_inches='tight')

    # Concat into nuclear-only dataframe from all of the countries
    nuclear_df = pd.concat([US_Nuclear, CAN_Nuclear, CHI_Nuclear, IND_Nuclear, UK_Nuclear, EU_Nuclear])
    # Write all nuclear data to a csv file
    nuclear_df.to_csv('../output/nuclear_energy_data.csv',encoding='utf-8', index=False, lineterminator='\n')

    return nuclear_df

# Function to extract and visualize hydro energy
def hydro_energy():
    # Filter to only hydro electricity data frame
    US_Hydro = US[US['category'] == "hydro"].sort_values("year")
    CAN_Hydro = CAN[CAN['category'] == "hydro"].sort_values("year")
    CHI_Hydro = CHI[CHI['category'] == "hydro"].sort_values("year")
    IND_Hydro = IND[IND['category'] == "hydro"].sort_values("year")
    UK_Hydro = UK[UK['category'] == "hydro"].sort_values("year")
    VN_Hydro = VN_df[VN_df['category'] == "hydro"].sort_values("year") 
    EU_Hydro = extract_eu_dataframes('hydro')

    # Initialize data for graph
    y0 = US_Hydro.quantity
    x0 = US_Hydro.year
    y2 = CAN_Hydro.quantity
    x2 = CAN_Hydro.year
    y3 = CHI_Hydro.quantity
    x3 = CHI_Hydro.year
    y4 = IND_Hydro.quantity
    x4 = IND_Hydro.year
    y5 = VN_Hydro.quantity
    x5 = VN_Hydro.year
    y6 = UK_Hydro.quantity
    x6 = UK_Hydro.year
    y7 = EU_Hydro[EU_Hydro['country_or_area'] == 'Germany'].quantity
    x7 = EU_Hydro[EU_Hydro['country_or_area'] == 'Germany'].year
    y8 = EU_Hydro[EU_Hydro['country_or_area'] == 'France'].quantity
    x8 = EU_Hydro[EU_Hydro['country_or_area'] == 'France'].year
    y9 = EU_Hydro[EU_Hydro['country_or_area'] == 'Italy'].quantity
    x9 = EU_Hydro[EU_Hydro['country_or_area'] == 'Italy'].year

    # Initialize graph
    f = plt.figure(figsize=(15,10))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.plot(x0,y0,label="USA")
    plt.plot(x2,y2,'y',label="Canada")
    plt.plot(x3,y3,'k',label="China")
    plt.plot(x4,y4,'g',label="India")
    plt.plot(x5,y5,'c',label="VietNam")   
    plt.plot(x6,y6,'m',label="UK")
    plt.plot(x7,y7,'crimson',label="Germany", linestyle = 'dashed')
    plt.plot(x8,y8,'navy',label="France", linestyle = 'dashed')
    plt.plot(x9,y9,'darkgoldenrod',label="Italy", linestyle = 'dashed')

    plt.legend(fontsize=16)
    plt.ylabel("Billions of Kilowatts-Hour",fontsize=20)
    plt.xlabel('Year',fontsize=20)
    plt.title('Total Hydro Production',fontsize=24)
    plt.xlim(1990, 2014.2)
    plt.show()
    
    # Save figure as png file
    f.savefig("../output/images/result_hydro.png", bbox_inches='tight')

    # Concat into hydro-only dataframe from all of the countries
    hydro_df = pd.concat([US_Hydro, CAN_Hydro, CHI_Hydro, IND_Hydro, UK_Hydro, EU_Hydro])
    # Write all hydro data to a csv file
    hydro_df.to_csv('../output/hydro_energy_data.csv',encoding='utf-8', index=False, lineterminator='\n')

    return hydro_df

# Function to extract and visualize vietnamese energy 
def vietnam_electricity():
    VN_total = VN_df[(VN_df['metrics'] == 'kilowatt-hours') & (VN_df['calculation_unit'] == 'million') & (VN_df['transaction_type'] == 'total production, main activity')]
    VN_Wind = VN_df[VN_df['category'] == "wind_electricity"].sort_values("year")
    VN_Hydro = VN_df[VN_df['category'] == "hydro"].sort_values("year") 
    VN_Thermal = VN_df[VN_df['category'] == "thermal_electricity"].sort_values("year") 

    y1 = VN_total.quantity
    x1 = VN_total.year
    y2 = VN_Wind.quantity
    x2 = VN_Wind.year
    y3 = VN_Hydro.quantity 
    x3 = VN_Hydro.year 
    y4 = VN_Thermal.quantity 
    x4 = VN_Thermal.year 

    # print(kilowatt_contained['category'].unique())
    f = plt.figure(figsize=(15,10))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.plot(x1,y1,label="VN_total")
    plt.plot(x2,y2,'r',label="VN_wind")
    plt.plot(x3,y3,'y',label="VN_hydro")
    plt.plot(x4,y4,'k',label="VN_thermal")


    plt.legend(fontsize=16)
    plt.ylabel("Millions of Kilowatts-Hour",fontsize=20)
    plt.xlabel('Year',fontsize=20)
    plt.title('Total Energy Production',fontsize=24)
    plt.xlim(1989.8, 2014.2)
    plt.show()

    # Save figure as png file
    f.savefig("../output/images/vn_electricity.png", bbox_inches='tight')

# Call functions
vietnam_electricity()
wind_energy()
solar_energy()
nuclear_energy()
hydro_energy()