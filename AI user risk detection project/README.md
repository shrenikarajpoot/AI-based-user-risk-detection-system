# **AI-Based User Risk Detection System**

\---

### Overview



This project is built around a simple but important idea — not all online behavior is safe, and small habits can sometimes lead to bigger risks. The system looks at basic user activities like password strength, login attempts, and interaction with unknown links, and tries to identify whether a user’s behavior falls into a safe or risky category.



Instead of just it as a theoretical concept, the project turns it into a working model using machine learning. The aim is to show how classroom concepts can actually be used to solve a real-world problem related to digital safety.



\---



### Problem Statement



Many users unknowingly follow unsafe practices online, such as using weak passwords or clicking suspicious links. These actions increase the chances of data theft, hacking, or fraud. The problem is to identify such risky behavior early and classify users accordingly so that preventive steps can be taken.



\---



### Objective



The main objective of this project is to build a system that can:



* &#x20;Analyze user activity data
* &#x20;Learn patterns from existing examples
* Predict whether a user is safe or risky



\---



### How the System Works



The system follows a clear step-by-step process:



1\. The dataset is loaded, which contains information about user behavior

2\. Relevant features are selected (like password strength, failed logins, etc.)

3\. The data is divided into training and testing parts

4\. A machine learning model is trained using the training data

5\. The model is tested on unseen data to check its performance

6\. Finally, the system can take a new user’s data and predict their risk level



\---

### 

### Machine Learning Approach



This project uses supervised learning, where the model learns from already labeled data.



The algorithm used is Logistic Regression, which is suitable for classification problems. It works by estimating the probability of a user being in a particular class (safe or risky) based on input features.



\---



### Features Used



The prediction is based on the following user attributes:



* &#x20;Password strength
* &#x20;Number of unknown links clicked
* &#x20;Failed login attempts
* &#x20;Use of public WiFi
* &#x20;Downloading unknown files



These features were selected because they directly relate to common unsafe digital practices.



\---



### Output



The system provides:



* Model accuracy
* Confusion matrix (to evaluate performance)
* Prediction for a new user (Safe / Risky)



\---



### Data Visualization



To better understand the dataset, simple graphs are used:



* Histogram to show password strength distribution
* Bar graph to compare safe and risky users
* Scatter plot to observe relation between link clicks and risk



These visualizations help in understanding patterns before and after model training.



\---

### 

### Project Structure





project/

|    │── main.py        

|    │── model.py       

|    │── train.py      

|    │── user\_data.csv 

|    │── README.md     

|───Output Screenshots

\---



### How to Run the Project



1\. Install required libraries:



&#x20;  ```

&#x20;  pip install pandas scikit-learn matplotlib

&#x20;  ```



2\. Make sure all files are in the same folder



3\. Run the program:



&#x20;  ```

&#x20;  python main.py

&#x20;  ```



\---


### Applications



This project can be extended or used in:



* Cybersecurity systems
* Fraud detection platforms
* User behavior monitoring tools
* Awareness tools for safe internet usage



\---



### Limitations



* The dataset is small and simplified
* Only basic features are considered
* Real-world systems would require more complex data



\---



### Learning Outcome



Working on this project helped in understanding how machine learning actually works beyond theory. Concepts like training a model, testing accuracy, and making predictions became much clearer after implementing them practically.



It also showed that even a simple model can be useful when applied to the right problem.



\---



### Conclusion



This project demonstrates how machine learning can be used to identify risky user behavior in a simple and understandable way. It connects theoretical concepts with practical implementation and highlights the importance of safe digital practices.



\---



### Final Note



This project is a small step towards understanding how data and machine learning can contribute to solving real-world problems. The focus was kept on clarity, simplicity, and practical application rather than complexity.



