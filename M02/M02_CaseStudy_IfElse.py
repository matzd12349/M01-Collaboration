# Author: David A Matz
#File Name: M02_CaseStudy_IfElse
#Description:
#   This app accepsts student names and GPA's, 
#   and checks if the student qualifies for either
#   the Dean's List or the Honor Roll.
#
#   Also to practice string literals such as print(f'{first_name}')
#
#Note: normally I name my fariables firstName,
#   where the first part is lowercase and each name is uppercase
#   to better match std naming I see in assignment and resources
#   I am chaning to the more common first_name with lowercasing
#   and underscores.

#define gpa and statement in a dictionary
qualifications: dict[float, str] = {
    3.5: "has made the Dean's List.",
    3.25: "has made the Honor Role."
}

#check student gpa to see qualifications
def check_qualifications(last_name: str, first_name: str, gpa: float) -> None:
    #for each float/str pair in the dictionary, iterate
    for num, msg in qualifications.items():
        #determine matches for Dean's and Honor Roll then return
        if gpa >= num:
            print(f'{first_name} {last_name} {msg}')
            return #assume student in Dean's list is already honor roll
    print(f"{first_name} {last_name} did not qualify for the Dean's or Honor Roll")
    return #sad student

#funcntion to get user data
def get_input() -> dict:
    #start by getting information about student
    try:
        last_name: str = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            raise SystemExit() #exit program safely
        first_name: str = input("Enter the student's first name: ")
        gpa: float = float(input("Enter the students's GPA: "))
        #return as dictionary type
        return {"last_name": last_name, "first_name": first_name, "gpa":gpa}

    except ValueError: #throw error if input goes wrong
        print("Invalid input. Try again.")
        return get_input() #recursion until proper input

#begin the main function of the program
def main() -> None: #keep forgetting python void is none
    while True:
        student_info: dict = get_input()
        check_qualifications(student_info['last_name'], student_info['first_name'], student_info['gpa'])


main()



