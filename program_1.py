def kilometer_conversion(kilometers):
    miles = 0.0

    miles = kilometers * 0.6214
    print("The distance in miles is ", format(miles ,',.3f'))
    # Return the variable to the calling function
    return miles


#### This piece of the code has been done for you,
#### you only need to worry about the actual temp
#### conversion logic in the temp_conversion function
if __name__ == '__main__':
    # Get User Input
    kilometers = float(input("Please enter a distance in kilometers: "))


kilometer_conversion(kilometers)
    # Call kilometer_conversion

    # Display the miles