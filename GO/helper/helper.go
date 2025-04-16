package helper

import "strings"

func ValidateUserInput(FirstName string, LastName string, EmailAddress string, UserTickets int, RemainingTickets int) (bool, bool, bool) {
	isValidName := len(FirstName) >= 2 && len(LastName) >= 2
	isValidEmail := strings.Contains(EmailAddress, "@")
	isValidTicketNumber := UserTickets > 0 && UserTickets <= RemainingTickets
	return isValidName, isValidEmail, isValidTicketNumber
}