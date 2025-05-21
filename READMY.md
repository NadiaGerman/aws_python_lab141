# AWS Python Lab: Prime Numbers Finder

This project is a part of the AWS Cloud lab.  
It demonstrates using Python and Git with an EC2 Linux instance to automate a simple computational task and track results via GitHub.

## 💻 Overview

- **find_primes.py**: Python script that finds all prime numbers between 1 and 250 and writes them to `results.txt`.
- **results.txt**: Output file containing one prime number per line.

## 🚀 Usage

### Run Locally (Mac/Linux)

1. Clone the repository:
   ```bash
   git clone https://github.com/NadiaGerman/aws_python_lab141.git
   cd aws_python_lab141
Run the script:
python3 find_primes.py
View results:
cat results.txt
Run on AWS EC2
SSH into your EC2 instance:
ssh -i ~/path/to/labsuser.pem ec2-user@<public-ip>
Install git (if needed):
sudo yum install git -y
Clone this repo and run the script:
git clone https://github.com/NadiaGerman/aws_python_lab141.git
cd aws_python_lab141
python3 find_primes.py
cat results.txt
📂 File Structure

aws_python_lab141/
├── find_primes.py
├── results.txt
└── README.md
📝 Author

Nadia German