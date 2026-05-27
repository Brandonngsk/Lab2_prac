def display_main_menu():
    print("Enter some numbers seperated by commas")
    
def get_user_input():
    user_input = input()
    string_list = user_input.split(",")
    float_list = []
    for num_str in string_list:
        float_list.append(float(num_str)) 
        
    return float_list

def calculate_average_temperature(num_list):
    total = sum(num_list)
    average = total / len(num_list)
    
    return average

def calculate_min_max_temperature(num_list):
    minimum = min(num_list)
    maximum = max(num_list)
    
    return [minimum, maximum]
    
    
    