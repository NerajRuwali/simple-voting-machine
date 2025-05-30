from users import User, register_user, login_user
from votes import VotingSystem


def main():
	voting_system = VotingSystem()
	while True:
		print("1. Register")
		print("2. Login")
		print("3. Vote")
		print("4. View Results")
		print("5. Exit")
		choice = input("Enter your choice: ")
		if choice=="1":
			register_user()
		elif choice=="2":
			login_user()
		elif choice=="3":
			voting_system.vote()
		elif choice=="4":
			voting_system.view_results()
		elif choice=="5":
			print("Exiting the system and Thank you for using our system.")
			break
		else:
			print("Invalid Choice Please try again.")


if __name__=="__main__":
	main()