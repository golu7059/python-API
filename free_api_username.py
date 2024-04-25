import requests 
# import json

def fectch_random_user() :
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"  # api url
    response = requests.get(url)    # store data in url into a variable
    all_data = response.json()      # convert into json formate
    
    if all_data["success"] and "data" in all_data : 
        user_data = all_data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username , country
    else : 
        raise Exception("Failed to fetch API data")
    

# writing main function 

def main():
# better to use try and catch method to make code more realible
    try :
        username , country = fectch_random_user()
        print(f"Username is : {username} \t Country name is : {country}")
    except Exception as e :
        print(str(e))        # printing the exception

if __name__ == "__main__" :
    main()