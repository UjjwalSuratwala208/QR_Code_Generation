# Import the qrcode library to generate the QRCodes.
import qrcode

# -- Step 1: define the data :
#Define the data for which you want to create a QRCode
#This data can be any text, URL or any string data

data =  "https://www.bioxsystems.com/"

# -- Step 2: Define the file name :
#Define the name for the output image file
img_outputfilename = "biox_systems_qr.png"

#Defied the try and exception block for error handling
try:
    # -- Step 3: Configure and Create the QRCode object : 
    # - version = 1: which controls the size of the QR code matrix(1 is 21*21) which can be increased for more data
    # - error_correction: This will determines how much code can be damaged and still readable,
    #   ERROR_CORRECT_L - will allow about the 7% of the data can be restored.
    # - box_size = 10: This will set the number of pixels for each "box" in the QR Code
    # - border = 4: this will set the width (in boxes) of the border around the QR code, and 4 is by default size   

     qr = qrcode.QRCode(
        version=1, # 1 is the smallest size which is good for short url
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10,  # each box will be 10*10 pixels
        border= 6 ,  # A border of 6 boxes for clear readibility
     )

    # -- Step 4: Add  and fit the URL data to the QRCode object so that QR code can adjust size automatically.
     qr.add_data(data)
     qr.make(fit = True) # fit the data to QR code and will adjust the size automatically

    # -- Step 5: Create the Image of QR Code object
    # - fill_color:   the color of the QR code itself (black is standard) 
    # - back_color: the background color (white for best contrast) 
     img = qr.make_image(fill_color="black", back_color="white")

     # -- Step 6: Save the generated image to the specified file
     img.save(img_outputfilename)
    
    # -- Step 7: Print a success message to the console to confirm that the file was created.
     print(" QR code successfully generated and saved as '{img_outputfilename}'")
     
except Exception as e:
    # If any error occur while running the script, print an error message
    print("An error occured while generating the QR code: {e}")