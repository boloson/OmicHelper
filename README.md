# Create Mass Hunter Library from Mass Omics (https://github.com/MASHUOA/MassOmics)

A python gui app to convert the MassOmics libray summary report file to a Mass Hunter library. 

It searches the name of the compound in the summary report csv file from an existing Mass Hunter library and create a new library which consist only the compounds in the summary compound table. User can later process the data using Mass Hunter Quantification software.

## Usage
### 1. Convert the MSL library to Mass Hunter Library format (.mslibrary.xml)
Change the .msl library file suffix to .msp

Open the .msp file using Lib2NIST Converter software from NIST software suite

![image](https://github.com/boloson/OmicHelper/assets/5682057/b7135eb9-f97f-4f3f-97fb-16d84b22d8b6)

Select the Output Format to HP JCAMP File (.HPJ), change the output directory to the desired folder.

![image](https://github.com/boloson/OmicHelper/assets/5682057/1b24e015-55e4-471d-a93b-f09c619aba62)

Click the Input library file and then click "Convert"

Create a new library file using Library Editor from Mass Hunter Quantification Suite

![image](https://github.com/boloson/OmicHelper/assets/5682057/4ca40d0f-fd46-4769-88a2-c68e60ba334b)

Import the .HPJ file using "All File (*.*)" option 
 
![image](https://github.com/boloson/OmicHelper/assets/5682057/121b0ee9-8b5c-4ee1-9a4f-aad216ffbc12)

Save the library. 

### 2.  Create a MassOmics and curated the compound table follow the instruction on https://github.com/MASHUOA/MassOmics
![image](https://github.com/boloson/OmicHelper/assets/5682057/251dc5ae-9841-44af-a779-18b602a536d6)

### 3. Add unkown compoudns to the table if nesccessary, make sure the retention time is correct and fill other column with dummy info.
![image](https://github.com/boloson/OmicHelper/assets/5682057/c64d9daf-6c45-4099-89d4-c62b3abcfb12)

### 4. Run the python script or run the compiled exe file. Select the library file to search from and the curated summary report csv file. Type in the output library file name or click "Browse" to navigate to disired folder.
![image](https://github.com/boloson/OmicHelper/assets/5682057/532cdc33-976d-4a9d-a558-98fca40f2cd7)

### 5. Click the Create Library button. An mslibrary.xml file will be created. 
![image](https://github.com/boloson/OmicHelper/assets/5682057/3a9e5ebb-e916-411c-b674-93d2d675bddd)


### 6. Open the newly created library file using Library Editor from Mass Hunter Quant suite. A message box will pop up and click OK with "Retetion Time" in the selection.
![image](https://github.com/boloson/OmicHelper/assets/5682057/2b3bc224-76b8-4705-bd13-a63970923135)

### 7. For compounds that are not in the original library file, there will be a line saying "Required manual spectrum entry" in the Description column. Follow the steps to update the spectrum. 
Select the row of the compound
![image](https://github.com/boloson/OmicHelper/assets/5682057/e1568a9c-1006-41f8-8098-dea3668f38a1)

Click the spectrum and right click the mouse. Press delete.
![image](https://github.com/boloson/OmicHelper/assets/5682057/65662007-42d8-4cca-b1c5-79f50b7e3d3d)

Open the Qualitative analysis, open the data file that has this unknown peak using the retention time and m/z to find the corresponding spectrum. Use subtracted spectrum if nescessary to avoid interference. Right click to copy the spectrum. 
![image](https://github.com/boloson/OmicHelper/assets/5682057/8cf820e9-096a-4e27-8a33-feb77c437628)

Paste the spectrum into the aforemetioned unknown compound.
![image](https://github.com/boloson/OmicHelper/assets/5682057/175c4518-ecc1-4e3a-a43e-491251721d2d)

This compound is updated with the corresponding spectrum. Do the same for other compounds that is not found in the orginal library.
![image](https://github.com/boloson/OmicHelper/assets/5682057/ccdc1630-228a-42e2-b833-48b411e0ab3b)

### 8. Open Mass Hunter Quantification and create a batch from the data file. Create a new method from a file and select the newly created library file. 
![image](https://github.com/boloson/OmicHelper/assets/5682057/f7b6b3c3-5c32-42d6-a444-473145f61f13)

![image](https://github.com/boloson/OmicHelper/assets/5682057/f80cb4bc-e37a-4757-ab39-66d23bf90706)

![image](https://github.com/boloson/OmicHelper/assets/5682057/fea1b6a8-2b29-4a07-a08f-e2833c94cf60)

