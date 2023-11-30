package main

import (
	"encoding/csv"
	"fmt"
	"math/rand"
	"os"
	"strings"
	"time"

	"github.com/icrowley/fake"
)

type SoftwareCompany struct {
	Name      string
	Industry  string
	Employees int
	Revenue   int
	Location  string
}

type Employee struct {
	CompanyName string
	FirstName   string
	LastName    string
	Email       string
	Position    string
	Salary      int
}

type Department struct {
	CompanyName    string
	DepartmentName string
	ManagerID      int
	Budget         int
	Location       string
	StartDate      string
	EndDate        string
	DepartmentSize int
	FunctionalArea string
}

func RandomDate() string {
	min := time.Date(2000, 1, 1, 0, 0, 0, 0, time.UTC).Unix()
	max := time.Date(2023, 1, 1, 0, 0, 0, 0, time.UTC).Unix()
	delta := max - min

	sec := rand.Int63n(delta) + min
	return time.Unix(sec, 0).Format("2006-01-02")
}

func main() {
	startTime := time.Now()
	rand.Seed(time.Now().UnixNano())

	var companySize int
	fmt.Println("Enter Amount of Companies to Create: ")
	fmt.Scan(&companySize)

	// Creating Companies
	companyFile, _ := os.Create("companies_go.csv")
	companyWriter := csv.NewWriter(companyFile)
	companyWriter.Write([]string{"Name", "Industry", "Employees", "Revenue", "Location"})

	var companies []SoftwareCompany
	uniqueNames := make(map[string]bool)

	for i := 0; i < companySize; i++ {
		var name string
		attempts := 0
		for {
			attempts++
			name = fake.Company()
			if _, exists := uniqueNames[name]; !exists {
				break
			}
			if attempts >= 100 {
				name += fmt.Sprintf("-%d", rand.Intn(9999))
				break
			}
		}
		uniqueNames[name] = true

		company := SoftwareCompany{
			Name:      name,
			Industry:  fake.Industry(),
			Employees: rand.Intn(20000),
			Revenue:   rand.Intn(1000000000),
			Location:  fake.City(),
		}
		companies = append(companies, company)
		companyWriter.Write([]string{company.Name, company.Industry, fmt.Sprint(company.Employees), fmt.Sprint(company.Revenue), company.Location})
	}
	companyWriter.Flush()
	companyFile.Close()

	// Creating Employees
	employeeFile, _ := os.Create("employees_go.csv")
	employeeWriter := csv.NewWriter(employeeFile)
	employeeWriter.Write([]string{"Company_Name", "First_Name", "Last_Name", "Email", "Position", "Salary"})

	for _, company := range companies {
		domain := strings.Replace(strings.ToLower(company.Name), " ", "", -1)
		for i := 0; i < company.Employees; i++ {
			firstName := fake.FirstName()
			lastName := fake.LastName()
			email := fmt.Sprintf("%s.%s@%s.com", strings.ToLower(firstName), strings.ToLower(lastName), domain)
			employee := Employee{
				CompanyName: company.Name,
				FirstName:   firstName,
				LastName:    lastName,
				Email:       email,
				Position:    fake.JobTitle(),
				Salary:      rand.Intn(150000),
			}
			employeeWriter.Write([]string{employee.CompanyName, employee.FirstName, employee.LastName, employee.Email, employee.Position, fmt.Sprint(employee.Salary)})
		}
	}
	employeeWriter.Flush()
	employeeFile.Close()

	// Creating Departments
	departmentFile, _ := os.Create("departments_go.csv")
	departmentWriter := csv.NewWriter(departmentFile)
	departmentWriter.Write([]string{"Company_Name", "Department_Name", "Manager_ID", "Budget", "Location", "Start_Date", "End_Date", "Department_Size", "Functional_Area"})

	for _, company := range companies {
		numDepartments := rand.Intn(5) + 1 // Random number of departments
		for i := 0; i < numDepartments; i++ {
			department := Department{
				CompanyName:    company.Name,
				DepartmentName: "Department of " + fake.Industry(),
				ManagerID:      rand.Intn(999999),
				Budget:         rand.Intn(500000),
				Location:       fake.City(),
				StartDate:      RandomDate(),
				EndDate:        RandomDate(),
				DepartmentSize: rand.Intn(100),
				FunctionalArea: fake.Industry(),
			}
			departmentWriter.Write([]string{department.CompanyName, department.DepartmentName, fmt.Sprint(department.ManagerID), fmt.Sprint(department.Budget), department.Location, department.StartDate, department.EndDate, fmt.Sprint(department.DepartmentSize), department.FunctionalArea})
		}
	}
	departmentWriter.Flush()
	departmentFile.Close()

	totalTime := time.Since(startTime)
	fmt.Printf("Total time taken: %s\n", totalTime)
}
