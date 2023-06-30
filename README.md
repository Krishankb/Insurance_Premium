# Insurance_Premium
This project is a Insurance premium calculator web application built with Flask, HTML, and MongoDB. It allows users to calculate insurance premiums based on age, city tier, sum insured, tenure, and the option to include children. The calculated premium is displayed, and data is stored in MongoDB for future reference.

## Steps to Run:
1. Clone the repository to your local machine using the "git clone" command. 
2. Ensure you have the required dependencies installed (Flask, MongoDB).
3. Open the project directory in your preferred code editor.
4. Run the main.py file using the command "python main.py".
5. Access the application by opening the provided URL(localhost) in a web browser.
6. Interact with the web interface to calculate insurance premiums.
7. View the calculated premium on the result page and other details on the terminal.

API Endpoints : 

1. `/`: The home endpoint that serves the main page of the premium calculator web application. Users can input their age, city tier, sum insured, tenure, and select if they have children.If children checkbox is selected then new input text field is displayed , it takes the number of children as input and based on the number of children a new input text field is displayed for each child age.

2. `/calculate_premium`: This endpoint handles the calculation of the insurance premium based on the user inputs. It collects data such as adult ages, city tier, sum insured, tenure, and optional child ages. The premium is calculated using a custom logic and displayed on the result page.

These endpoints provide the core functionality of the premium calculator web application, allowing users to input their information and receive the calculated premium.

Screenshot of working Project : 

2 Adults - 1 child 

Input : ![Insurance_Premium1](https://github.com/Krishankb/Insurance_Premium/assets/30771097/9664b017-936f-4052-b0bd-6cea50814e41)
Output : ![Insurance_Premium12](https://github.com/Krishankb/Insurance_Premium/assets/30771097/328a8d19-56eb-4fb8-afc2-bbcc83226de6)

1 Adult

Input : ![Insurance_Premium2](https://github.com/Krishankb/Insurance_Premium/assets/30771097/922eef81-b572-4981-8fce-edc64c44364d)
Output : ![Insurance_Premium22](https://github.com/Krishankb/Insurance_Premium/assets/30771097/9380fe72-536b-4330-a486-dc3dca0a02c4)

2 Adults - 4 children 

Input : ![Insurance_Premium3](https://github.com/Krishankb/Insurance_Premium/assets/30771097/855bae29-eda5-406e-b2d3-8b933e613714)
Output : ![Insurance_Premium32](https://github.com/Krishankb/Insurance_Premium/assets/30771097/4fa05a6d-7dae-448e-a277-ed06f2147f82)
