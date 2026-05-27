def calculate_bmi(height, weight):
    
    
    bmi = weight / (height * height)
   
    
    if bmi < 18.5:
        return -1
    elif bmi <= 25:
        return 0
    else:
        return 1
    

