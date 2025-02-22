using WorkingWithGenerics.Models;
using WorkingWithGenerics.Mappers;

// Using the custom constructor
var customer1 = new Customer(30, 1, "Jon Doe");

// var p = new Person
// {
//     Id = 1,
//     Name = "John Doe Person",
//     Age = 30
// };

//var p = new Person();

var per = new Person { Id = 1, Name = "John Doe", Age = 30 };

var mapper = new CustomerToPersonMapper();
var person = mapper.Map(customer1);
Console.WriteLine($"Person: {person.Name}");