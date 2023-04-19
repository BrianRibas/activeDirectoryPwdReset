# used to work with csv file, subprocess used to run PS commands
import csv, subprocess
def main():
    pwd_reset() #pwd reset call
    run_again_prompt = run_program_again_prompt() #variable takes return value from run_again_prompt() asking if user wants to run the program again
    yes_run_again = please_run_again(run_again_prompt) #variable takes return value that is prompted to user (y or n) to whether programs runs again,
                                                                #argument is passed with user input for processing
def pwd_reset():
    #input number you want to search
    try:
        student_id = input('Enter Student ID: ')
        csv_file = csv.reader(open('SIM_Extract_Test.csv', "r"), delimiter=",") #read csv, and split on "," the line
        for column in csv_file: #loop through the csv list
            if (student_id == column[0]): #if current rows 2nd value is equal to input, print that row
                student_info = column # 0 = student id, 1 = first name, 2 = last name, 3 = user id, 4 = birth date
                first_name = column[1]
                last_name = column[2]
                user_id = column[3]
                birth_date = column[4]
        import datetime
        format_str = '%m/%d/%Y' # The format for the reset
        datetime_obj = datetime.datetime.strptime(birth_date, format_str)
        MMDDYY = datetime_obj.strftime('%m%d%y')
        print('Ask ' + first_name + ' ' + last_name + ' ' + user_id + ' to verify their DOB: ' + birth_date)
        verified = input('Proceed with password reset? (Y/n): ')
        if verified == 'Y':
            #powershell call
            subprocess.call('%SystemRoot%/system32/WindowsPowerShell/v1.0/powershell.exe $pw = ConvertTo-SecureString ' + MMDDYY + ' -AsPlainText -Force; Set-ADAccountPassword -Identity ' + user_id + ' -NewPassword $pw -Reset', shell=True)
            print('Please tell the end-user their password is:', MMDDYY)
            print('Password reset has been completed.')
    except:
        print('Student ID not found.')
def please_run_again(run_again_prompt): 
    while run_again_prompt == 'n':
        print('end of program')
        break
        if run_again_prompt == 'y':
            pwd_reset()      
def run_program_again_prompt(): #ask user if want to run program again > input y or n
    run_again = input('Run this again? y or n? ')
    return run_again     
main()
