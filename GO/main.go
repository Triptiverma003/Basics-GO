package main

import (
	"fmt"
	"strings"
	"GO/helper"
)
	const ConferenceTickets int = 50
	var ConferenceName = "Go Conference"
	//uint is used for positive numbers
	//int is used for negative and positive numbers
	var RemainingTickets = 50
	var bookings []string


func main() {
	//Variables

	greetUser()
	fmt.Printf("ConferenceTickets is %T\n,RemainingTickets is %T\n", ConferenceName, RemainingTickets)

	fmt.Printf("Welcome to %v booking application\n", ConferenceName)
	fmt.Printf("We have total of %v tickets and %v are still available\n", ConferenceTickets, RemainingTickets)
	fmt.Println("This is a simple application to book conference tickets")

	for {
		firstName, lastName, emailAddress, userTickets := getUserInput()
		helper.ValidateUserInput(firstName, lastName, emailAddress, userTickets, RemainingTickets)

		//conditional checking
		if userTickets > int(RemainingTickets) {
			fmt.Println("We have only ", RemainingTickets, "tickets available")
			continue
		}
		isValidName, isValidEmail, isValidTicketNumber := helper.ValidateUserInput(firstName, lastName, emailAddress, userTickets, RemainingTickets)
		if isValidName && isValidEmail && isValidTicketNumber {
			bookTickets(&RemainingTickets, userTickets, firstName, lastName, emailAddress, &bookings, ConferenceTickets)

			fmt.Printf("Thankyou  %v %v for buying %v Tickets, You Will get a confirmation email on %v\n", firstName, lastName, userTickets, emailAddress)
			fmt.Printf("We have total of %v tickets and %v are still available\n", ConferenceTickets, RemainingTickets)

			FirstName := getFirstNames()
			fmt.Printf("The first names of bookings are: %v\n", FirstName)

			fmt.Printf("Whole slice: %v\n", bookings)
			fmt.Printf("First value: %v\n", bookings[0])
			fmt.Printf("length of array: %v\n", len(bookings))
			fmt.Printf("Slice Type: %v\n", bookings)

			//noTicketsRemaining := RemainingTickets == 0
			if RemainingTickets == 0 {
				//end the program
				fmt.Println("Our conference is booked out. Come back next year")
				break
			}
		} else {
			if !isValidName {
				fmt.Println("Invalid first or last name: each must be at least 2 characters")
			}
			if !isValidEmail {
				fmt.Println("Invalid email address: must contain '@'")
			}
			if !isValidTicketNumber {
				fmt.Println("Invalid ticket number: must be greater than 0 and not exceed remaining tickets")
			}
			fmt.Println("Please try again")
			continue
		}
	}
}

func greetUser() {
	fmt.Printf("Welcome to %v booking application", ConferenceName)
	fmt.Printf("We have total of %v tickets and %v are still available\n" , ConferenceTickets,RemainingTickets)
	fmt.Println("This is a simple application to book conference tickets")
}

func getFirstNames() []string {
	firstNames := []string{}
	for _, booking := range bookings {
		var names = strings.Fields(booking)
		firstNames = append(firstNames, names[0])
	}
	return firstNames
}



func getUserInput() (string, string, string, int) {
	var firstName string
	var lastName string
	var userTickets int
	var emailAddress string

	fmt.Println("Enter your first name:")
	fmt.Scan(&firstName)
	fmt.Println("Enter your last name:")
	fmt.Scan(&lastName)
	fmt.Println("Enter your email address:")
	fmt.Scan(&emailAddress)
	fmt.Println("Enter number of tickets:")
	fmt.Scan(&userTickets)
	return firstName, lastName, emailAddress, userTickets
}

func bookTickets(RemainingTickets *int, userTickets int, firstName string, lastName string, emailAddress string, bookings *[]string, ConferenceTickets int) {
	*RemainingTickets = *RemainingTickets - userTickets
	*bookings = append(*bookings, firstName+" "+lastName)

	fmt.Printf("Thank you %v %v for buying %v tickets. You will get a confirmation email at %v\n", firstName, lastName, userTickets, emailAddress)
	fmt.Printf("We have a total of %v tickets and %v are still available.\n", ConferenceTickets, *RemainingTickets)
}
